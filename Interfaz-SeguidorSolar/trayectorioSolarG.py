import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib.image as mpimg

def graphTrayectoriaSolPolar2D(frame_polar, times, azimuths, elevations, beta, phi):
    # Convertir los azimuths de grados a radianes para el gráfico polar
    azimuths_rad = np.radians(azimuths)

    # Cargar la imagen del sol
    sun_img = mpimg.imread('./images/sol4.jpg')

    # Crear la figura y el eje polar
    fig_polar = plt.Figure(figsize=(2, 2), dpi=100)
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

# ---- Función con ventana --------------------------


def graphTrayectoriaSolPolar2DVentana(times, azimuths, elevations, beta, phi):
    # Convertir los azimuths de grados a radianes para el gráfico polar
    azimuths_rad = np.radians(azimuths)

    # Cargar la imagen del sol
    sun_img = mpimg.imread('./images/sol4.jpg')

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
