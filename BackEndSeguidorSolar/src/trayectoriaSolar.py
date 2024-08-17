import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#----------Método para graficar las trayectorias 2D de los ángulos de la posición del sol----------------
def graphTrayectoriaSol2D(times, azimuths, elevations,):
    # Crear la figura 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Convertir los tiempos a números (por simplicidad en la gráfica 3D)
    time_numbers = np.arange(len(times))

    # Graficar los datos en 3D
    ax.plot(time_numbers, azimuths, elevations, label='Solar Position')

    ax.set_xlabel('Time')
    ax.set_ylabel('Azimuth (degrees)')
    ax.set_zlabel('Elevation (degrees)')
    ax.set_title('Solar Trajectory')
    ax.legend()
    plt.show()

#----------Método para graficar las trayectorias 2D de los ángulos POLARES de la posición del sol----------------

def graphTrayectoriaSolPolar2D(times, azimuths, elevations, beta, phi):
    # Convertir los azimuths de grados a radianes para el gráfico polar
    azimuths_rad = np.radians(azimuths)

    # Cargar la imagen del sol
    sun_img = mpimg.imread('./Interfaz-SeguidorSolar/images/sol4.jpg')

    # Configurar la ventana de Tkinter
    root = tk.Tk()
    root.title("Simulación de Ángulos Solares")

    # Crear un marco para la gráfica polar
    frame_polar = tk.Frame(root)
    frame_polar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Crear la figura y el eje polar
    fig_polar = plt.Figure(figsize=(13, 7), dpi=100)
    ax_polar = fig_polar.add_subplot(111, projection='polar')

    # Configurar la dirección del ángulo (en sentido horario y con 0° en la parte superior)
    ax_polar.set_theta_direction(-1)
    ax_polar.set_theta_offset(np.pi / 2.0)

    # Configurar los ejes
    ax_polar.set_title('Trayectoria del sol en Coordenadas Polares')

    # Función de inicialización para la animación polar
    def init_polar():
        ax_polar.set_ylim(min(elevations), max(elevations))
        return []

    # Función de actualización para la animación polar
    def update_polar(frame):
        ax_polar.clear()  # Limpiar el gráfico en cada frame
        ax_polar.set_theta_direction(-1)
        ax_polar.set_theta_offset(np.pi / 2.0)
        ax_polar.set_ylim(min(elevations), max(elevations))
        ax_polar.set_title('Trayectoria del sol en Coordenadas Polares')
        
        theta = azimuths_rad[frame]  # Ángulo actual en radianes
        r = elevations[frame]  # Elevación actual
        
        # Superponer la imagen del sol en la ubicación actual
        ax_polar.imshow(sun_img, extent=(theta - 0.1, theta + 0.1, r - 0.1, r + 0.1), zorder=5)
        
        # Para mantener la trayectoria dibujada, cambiar color a rojo ('r') y el marcador a un punto verde ('go-')
        ax_polar.plot(azimuths_rad[:frame+1], elevations[:frame+1], color='red', marker='o', markerfacecolor='yellow', linestyle='-', markersize=5, label='Trayectoria del Sol')

        return []

    # Crear el lienzo para la figura polar
    canvas_polar = FigureCanvasTkAgg(fig_polar, master=frame_polar)
    canvas_polar.draw()
    canvas_polar.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    interval_time_ms = 500
    ani_polar = animation.FuncAnimation(fig_polar, update_polar, frames=len(times), init_func=init_polar, interval=interval_time_ms, blit=True)

    # Iniciar la interfaz gráfica de Tkinter
    root.mainloop()

#----------Método para graficar la trayectoria 3D de la posición del sol----------------

def graphTrayectoriaSol3D(times, azimuths, elevations, beta, phi):
    # Convertir los tiempos a números (por simplicidad en la gráfica 3D)
    time_numbers = np.arange(len(times))

    # Configurar la ventana de Tkinter
    root = tk.Tk()
    root.title("Simulación de Ángulos Solares")

    # Crear un marco para la gráfica 3D
    frame_3d = tk.Frame(root)
    frame_3d.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Crear la figura y el eje 3D
    fig3 = plt.Figure(figsize=(13, 7), dpi=100)
    ax3 = fig3.add_subplot(111, projection='3d')

    # Configurar los ejes
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Azimuth')
    ax3.set_zlabel('Elevation')
    ax3.set_title('Trayectoria del sol')

    # Configurar límites fijos para evitar redimensionado
    ax3.set_xlim(0, len(times)-1)
    ax3.set_ylim(min(azimuths), max(azimuths))
    ax3.set_zlim(min(elevations), max(elevations))

    # Crear una función para generar la esfera que representa el sol
    def create_sun(ax, center, radius=2.0, color='yellow'):  # Aquí se ajusta el tamaño de la esfera
        # Crear una esfera 3D
        u = np.linspace(0, 2 * np.pi, 50)  # Aumentar la resolución para una mejor apariencia
        v = np.linspace(0, np.pi, 50)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]

        # Añadir la esfera al eje 3D con sombreado
        ax.plot_surface(x, y, z, color=color, shade=True, rstride=1, cstride=1, linewidth=0)

    # Función de inicialización para la animación 3D
    def init_3d():
        return []

    # Función de actualización para la animación 3D
    def update_3d(frame):
        ax3.cla()  # Limpiar el eje antes de actualizar

        # Re-dibujar la trayectoria hasta el punto actual, sin los puntos amarillos
        ax3.plot(time_numbers[:frame+1], azimuths[:frame+1], elevations[:frame+1], 'y-', markersize=0)

        # Crear la esfera 3D para representar el sol en la posición actual
        sun_position = [time_numbers[frame], azimuths[frame], elevations[frame]]
        create_sun(ax3, sun_position, radius=2.0, color='yellow')  # Ajusta el tamaño de la esfera aquí

        # Reestablecer límites para evitar redimensionado
        ax3.set_xlim(0, len(times)-1)
        ax3.set_ylim(min(azimuths), max(azimuths))
        ax3.set_zlim(min(elevations), max(elevations))
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Azimuth')
        ax3.set_zlabel('Elevation')
        ax3.set_title('Trayectoria del sol')

        return []

    # Crear el lienzo para la figura 3D
    canvas3 = FigureCanvasTkAgg(fig3, master=frame_3d)
    canvas3.draw()
    canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    interval_time_ms = 500
    ani3 = animation.FuncAnimation(fig3, update_3d, frames=len(times), init_func=init_3d, interval=interval_time_ms, blit=True)

    # Iniciar la interfaz gráfica de Tkinter
    root.mainloop()