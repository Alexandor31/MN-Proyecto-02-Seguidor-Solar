from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

import tkinter as tk
from imagenes import cargar_imagen
from data_entry import data_entry
from frames import create_frames
from BackEndSeguidorSolar import src
from tkinter import messagebox
from datetime import datetime, timedelta
from pytz import timezone
from trayectorioSolarG import graphTrayectoriaSolPolar2D, graphTrayectoriaSolPolar2DVentana, graphTrayectoriaSol3D, graphTrayectoriaSol3Ventana
from trayectoriaPanel import graphPanelTrayectory3D, graphPanelTrayectory3DVentana

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de seguimiento solar")
root.geometry("1280x720")

datos = []

# Función para vincular el evento de clic a un Frame y sus hijos
def bind_click_to_frame(frame, callback):
    frame.bind("<Button-1>", callback)  # Vincula al propio Frame
    for widget in frame.winfo_children():  # Vincula a cada hijo del Frame
        widget.bind("<Button-1>", callback)

# Funciones útiles
def click_ejecutar(fecha, inicio, fin):
    error = False
    try:
        inicio, fin = int(inicio), int(fin)
        mes, dia, anio = fecha.split('/')
        start_date = datetime(int(anio), int(mes), int(dia), tzinfo=timezone("America/Guayaquil"))
    except Exception as e:
        messagebox.showinfo("Mensaje", f"Se ha producido un error: {e}")
    message = ""
    print(fecha)
    if(fecha == "0/0/0"):
        error = True
        message += "No se permite una fecha 0/0/0\n - "
    if(inicio < 6 and inicio > 16):
        error = True
        message += "No se permite una hora de inicio antes del amanecer 7am y antes de 17pm - "
    if(fin > 18 and fin < inicio):
        error = True
        message += "No se permite una hora de fin después del anochecer 17pm, y mayor a la de inicio"

    if(error):
        messagebox.showinfo("Mensaje", message)
    else:
        times, azimuths, elevations, beta, phi = src.calculate_solar_positions(start_date, start_hour=inicio, end_hour=fin)
        ejecutar_graficos(times, azimuths, elevations, beta, phi)

def ejecutar_graficos(times, azimuths, elevations, beta, phi):

    # ------ Asignar un espacio para el gráfico ------------------------------------#
    graphTrayectoriaSolPolar2D(f_angulos_sol, times, azimuths, elevations, beta, phi)

    def ejecutar_pantalla_SOL_2D(event=None):
        if event.widget == f_angulos_sol or event.widget in f_angulos_sol.winfo_children():
            graphTrayectoriaSolPolar2DVentana(times, azimuths, elevations, beta, phi)

    bind_click_to_frame(f_angulos_sol, ejecutar_pantalla_SOL_2D)

    # ------ Asignar un espacio para el gráfico ------------------------------------#
    graphTrayectoriaSol3D(f_inferior_izquierda, times, azimuths, elevations, beta, phi)

    def ejecutar_pantalla_SOL3D(event=None):
        if event.widget == f_inferior_izquierda or event.widget in f_inferior_izquierda.winfo_children():
            graphTrayectoriaSol3Ventana(times, azimuths, elevations, beta, phi)
    
    bind_click_to_frame(f_inferior_izquierda, ejecutar_pantalla_SOL3D)

    # -------Asignar espacio para el gráfico -----------------------------------#
    graphPanelTrayectory3D(f_inferior_derecha, times, azimuths, elevations, beta, phi)

    def ejecutar_Panel_3D(event=None):
        if event.widget == f_inferior_derecha or event.widget in f_inferior_derecha.winfo_children():
            graphPanelTrayectory3DVentana(times, azimuths, elevations, beta, phi)

    bind_click_to_frame(f_inferior_derecha, ejecutar_Panel_3D)

# Cambiar el ícono de la ventana
root.iconbitmap("./icon/icono.ico")

# Cargar imagenes
imagen_panel_solar_tk = cargar_imagen()

# Creación de un Label como título
titulo = tk.Label(root, text="GRUPO 3 - PROYECTO DE SISTEMA DE SEGUIMIENTO SOLAR",
                  font=("Helvetica", 24, "bold"), image=imagen_panel_solar_tk,
                  compound="left", padx=10, pady=0)

titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

f_ingreso_datos, f_angulos_sol, f_inferior_izquierda, f_inferior_derecha = create_frames(root)

# Agregar contenido temporal en los frames para visualización
data_entry(f_ingreso_datos, root, click_ejecutar)

label_inferior_derecha = tk.Label(f_inferior_derecha, text="Inferior Derecha")
label_inferior_derecha.pack(expand=True)

# Iniciar el bucle de la aplicación
root.mainloop()