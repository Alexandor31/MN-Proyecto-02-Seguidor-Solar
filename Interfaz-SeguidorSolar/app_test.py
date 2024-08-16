import tkinter as tk
from imagenes import cargar_imagen
from data_entry import data_entry
from frames import create_frames


# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de seguimiento solar")
root.geometry("1280x720")

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
data_entry(f_ingreso_datos, root)

label_votaciones = tk.Label(f_angulos_sol, text="Angulos sol")
label_votaciones.pack(expand=True)

label_votaciones = tk.Label(f_angulo_pitch, text="Angulo Pitch")
label_votaciones.pack(expand=True)

label_inferior_izquierda = tk.Label(f_inferior_izquierda, text="Inferior Izquierda")
label_inferior_izquierda.pack(expand=True)

label_inferior_derecha = tk.Label(f_inferior_derecha, text="Inferior Derecha")
label_inferior_derecha.pack(expand=True)

# Iniciar el bucle de la aplicación
root.mainloop()