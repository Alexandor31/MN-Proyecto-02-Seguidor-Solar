import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#----------Método para graficar la trayectoria 3D de la posición del panel----------------

def graphPanelTrayectory(times, azimuths, elevations, beta, phi):
    # Supongamos que ya tienes la función calculate_solar_positions y los valores de times, beta, y phi

    # Función para crear los vértices del panel solar
    def create_panel(center, width, height):
        w = width / 2
        h = height / 2
        vertices = np.array([
            [center[0] - w, center[1] - h, center[2]],  # Inferior izquierdo
            [center[0] + w, center[1] - h, center[2]],  # Inferior derecho
            [center[0] + w, center[1] + h, center[2]],  # Superior derecho
            [center[0] - w, center[1] + h, center[2]]   # Superior izquierdo
        ])
        return vertices

    # Función para aplicar ambas rotaciones (pitch y roll) usando matrices combinadas
    def apply_rotations(vertices, pitch_angle, roll_angle):
        pitch_angle = np.radians(pitch_angle)
        roll_angle = np.radians(roll_angle)

        # Matriz de rotación para pitch (alrededor del eje Y)
        rotation_pitch = np.array([
            [np.cos(pitch_angle), 0, np.sin(pitch_angle)],
            [0, 1, 0],
            [-np.sin(pitch_angle), 0, np.cos(pitch_angle)]
        ])

        # Matriz de rotación para roll (alrededor del eje X)
        rotation_roll = np.array([
            [1, 0, 0],
            [0, np.cos(roll_angle), -np.sin(roll_angle)],
            [0, np.sin(roll_angle), np.cos(roll_angle)]
        ])

        # Combinar las matrices de rotación
        combined_rotation = rotation_pitch @ rotation_roll

        # Aplicar la rotación combinada a los vértices
        return vertices @ combined_rotation.T

    # Función para inicializar la animación
    def init():
        panel.set_verts([vertices])
        time_text.set_text('')  # Iniciar con texto vacío
        for scatter in scatters:
            scatter._offsets3d = (vertices[:, 0], vertices[:, 1], vertices[:, 2])
            return [panel] + scatters + [time_text]

    # Función para actualizar la animación con los valores de `beta` y `phi`
    def update(frame):
        if frame < len(times):
            # Aplicar rotaciones combinadas
            rotated_vertices = apply_rotations(vertices, beta[frame], phi[frame])

            # Actualizar las posiciones del panel
            panel.set_verts([rotated_vertices])

            # Actualizar las posiciones de los puntos en los vértices
            for i, scatter in enumerate(scatters):
                scatter._offsets3d = (np.array([rotated_vertices[i, 0]]),
                                    np.array([rotated_vertices[i, 1]]),
                                    np.array([rotated_vertices[i, 2]]))

            # Actualizar la etiqueta de tiempo con el tiempo calculado
            current_time = times[frame].strftime("Tiempo: %H:%M")
            time_text.set_text(current_time)
        
        return [panel] + scatters + [time_text]

    # Configurar la ventana de Tkinter
    root = tk.Tk()
    root.title("Simulación del Movimiento del Panel Solar")

    # Crear un marco para la gráfica 3D
    frame_3d = tk.Frame(root)
    frame_3d.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Crear la figura y el eje 3D dentro de la ventana Tkinter
    fig = plt.Figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111, projection='3d')

    # Definir los parámetros del panel
    center = [0, 0, 0]
    width = 4
    height = 2

    # Crear los vértices del panel
    vertices = create_panel(center, width, height)

    # Inicializar el panel con colores diferentes para cada cara y un borde más grueso
    panel = Poly3DCollection([vertices], facecolors=['blue', 'green'], linewidths=3, edgecolors='black')
    ax.add_collection3d(panel)

    # Agregar marcadores en los vértices para ayudar a guiar la visualización
    scatters = [ax.scatter(vertice[0], vertice[1], vertice[2], color='red', s=50) for vertice in vertices]

    # Configurar los límites de la gráfica
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)

    # Marcar la dirección del Norte (eje Y positivo)
    ax.quiver(0, 0, 0, 0, 5, 0, color='red', linewidth=2)  # Flecha apuntando al norte
    ax.text(0, 5, 0, "Norte", color='red', fontsize=12)    # Etiqueta de "Norte"

    # Añadir texto para mostrar el tiempo
    time_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color='black', fontsize=12)

    # Crear el lienzo para la figura 3D
    canvas3 = FigureCanvasTkAgg(fig, master=frame_3d)
    canvas3.draw()
    canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Crear la animación dentro de la ventana Tkinter, sin blit
    interval_time_ms = 1000  # Un frame por segundo para sincronizar con el tiempo real
    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, len(times)), init_func=init, interval=interval_time_ms, blit=False)

    # Iniciar la interfaz gráfica de Tkinter
    root.mainloop()