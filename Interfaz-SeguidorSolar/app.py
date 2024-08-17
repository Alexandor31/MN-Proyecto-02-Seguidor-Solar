# Install pip install tk
# pip install tkcalendar
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
from calendary import mostrar_calendario
from imagenes import cargar_imagen

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de seguimiento solar")

# Configurar el tamaño de la ventana
root.geometry("1280x720")

# Cambiar el ícono de la ventana
root.iconbitmap("./icon/icono.ico")

# Cargar imagenes
imagen_panel_solar_tk = cargar_imagen()

# Creación de un Label como título
titulo = tk.Label(root, text="GRUPO 3 - PROYECTO DE SISTEMA DE SEGUIMIENTO SOLAR",
                  font=("Helvetica", 24, "bold"), image=imagen_panel_solar_tk,
                  compound="left", padx=10, pady=10)

titulo.pack(pady=10)

# Subtítulo o descripción
descripcion = tk.Label(root, text="Un seguidor solar es un sistema de orientación para maximizar la exposición a la luz solar. Esto se consigue cuando el panel solar se orienta perpendicularmente a la luz solar incidente. Cuando el panel no se encuentra perpendicular, la cantidad de energía generada disminuye significativamente. Por eso los sistemas de seguimiento calculando el ángulo correcto para que el panel esté perpendicular al sol.", 
                       wraplength=1000, justify="left", anchor="w", font=("Helvetica", 12))
descripcion.pack(pady=10)

fecha = ""
def obtener_fecha():
    fecha = mostrar_calendario(root)
    l_fecha.config(text=f"Fecha seleccionada: {fecha}")

# Botón para mostrar el calendario
boton_mostrar_calendario = tk.Button(root, text="Seleccionar Fecha", command=obtener_fecha)
boton_mostrar_calendario.pack(pady=50)

# Label para mostrar la fecha seleccionada
l_fecha = tk.Label(root, text="")
l_fecha.pack(pady=20)

# Crear un botón y asignarle una acción
def on_button_click():
    messagebox.showinfo("Mensaje", "Has hecho clic en el botón")

button = tk.Button(root, text="Haz clic aquí", command=on_button_click)
button.pack(pady=40)

# Mantener la ventana abierta
root.mainloop()