import tkinter as tk
from tkcalendar import Calendar

def mostrar_calendario(root):
    # Crear una ventana Toplevel
    ventana_calendario = tk.Toplevel(root)
    ventana_calendario.title("Seleccionar Fecha")
    
    # Centrar la ventana emergente
    ventana_calendario.geometry("300x300")
    
    # Variable para almacenar la fecha seleccionada
    fecha_seleccionada = tk.StringVar()

    # Crear el widget Calendar en la ventana emergente
    cal = Calendar(ventana_calendario, selectmode="day", year=2024, month=8, day=16)
    cal.pack(pady=20)
    
    # Función para manejar la selección de la fecha
    def seleccionar_fecha():
        fecha_seleccionada.set(cal.get_date())
        ventana_calendario.destroy()  # Cierra la ventana del calendario

    # Botón para confirmar la selección de fecha
    boton_confirmar = tk.Button(ventana_calendario, text="Confirmar", command=seleccionar_fecha)
    boton_confirmar.pack(pady=10)

    # Esperar hasta que la ventana del calendario se cierre
    ventana_calendario.wait_window()

    # Retornar la fecha seleccionada
    return fecha_seleccionada.get()
