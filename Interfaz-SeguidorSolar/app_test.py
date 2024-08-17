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
from trayectorioSolarG import graphTrayectoriaSolPolar2D, graphTrayectoriaSolPolar2DVentana

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de seguimiento solar")
root.geometry("1280x720")

datos = []
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
    if(inicio < 6):
        error = True
        message += "No se permite una hora de inicio antes del amanecer 7am - "
    if(fin >18):
        error = True
        message += "No se permite una hora de fin después del anochecer 17pm,"

    if(error):
        messagebox.showinfo("Mensaje", message)
    else:
        times, azimuths, elevations, beta, phi = src.calculate_solar_positions(start_date, start_hour=inicio, end_hour=fin)
        datos = times, azimuths, elevations, beta, phi
        ejecutar_graficos(times, azimuths, elevations, beta, phi)


def ejecutar_graficos(times, azimuths, elevations, beta, phi):
    print("Solar Position Data:\n")

    print("Times: ", end="")
    print(", ".join([f"{time.strftime('%H:%M')}" for time in times]))

    print("\nAzimuths: ", end="")
    print(", ".join([f"{azimuth:.2f}°" for azimuth in azimuths]))

    print("\nElevations: ", end="")
    print(", ".join([f"{elevation:.2f}°" for elevation in elevations]))

    print("\nBeta (Ángulo de Inclinación): ", end="")
    print(", ".join([f"{b:.2f}°" for b in beta]))

    print("\nPhi (Ángulo de Orientación): ", end="")
    print(", ".join([f"{p:.2f}°" for p in phi]))

    graphTrayectoriaSolPolar2D(f_angulos_sol,times, azimuths, elevations, beta, phi)

    def ejecutar_pantalla(event=None):
        graphTrayectoriaSolPolar2DVentana(times, azimuths, elevations, beta, phi)

    f_angulos_sol.bind_all("<Button-1>", ejecutar_pantalla)
    pass



# Cambiar el ícono de la ventana
root.iconbitmap("./icon/icono.ico")

# Cargar imagenes
imagen_panel_solar_tk = cargar_imagen()

# Creación de un Label como título
titulo = tk.Label(root, text="GRUPO 3 - PROYECTO DE SISTEMA DE SEGUIMIENTO SOLAR",
                  font=("Helvetica", 24, "bold"), image=imagen_panel_solar_tk,
                  compound="left", padx=10, pady=0)

titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

f_ingreso_datos, f_angulos_sol, f_angulo_pitch, f_inferior_izquierda, f_inferior_derecha = create_frames(root)

# Agregar contenido temporal en los frames para visualización
data_entry(f_ingreso_datos, root, click_ejecutar)

label_votaciones = tk.Label(f_angulo_pitch, text="Angulo Pitch")
label_votaciones.pack(expand=True)

label_inferior_izquierda = tk.Label(f_inferior_izquierda, text="Inferior Izquierda")
label_inferior_izquierda.pack(expand=True)

label_inferior_derecha = tk.Label(f_inferior_derecha, text="Inferior Derecha")
label_inferior_derecha.pack(expand=True)

# Iniciar el bucle de la aplicación
root.mainloop()