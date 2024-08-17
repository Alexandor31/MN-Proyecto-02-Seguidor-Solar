import tkinter as tk
from calendary import mostrar_calendario
 
def data_entry(f_ingreso_datos, root, funcion_click):
    fecha = ""
    def obtener_fecha():
        fecha = (mostrar_calendario(root))
        l_fecha.config(text=f"Fecha: {fecha}")

    def button_click():
        fecha_l = "".join(l_fecha.cget("text"))
        fecha_l = fecha_l[6::]
        inicio = entry_hora_inicio.get()
        fin = entry_hora_fin.get()
        print(fecha_l, inicio, fin)
        funcion_click(fecha_l, inicio, fin)

    # Añadir subtítulo y campos en el frame "Ingreso Datos"
    subtitulo = tk.Label(f_ingreso_datos, text="Datos de Entrada", font=("Helvetica", 16))
    subtitulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    # Colocar el Label
    l_fecha = tk.Label(f_ingreso_datos, text="Fecha: 0/0/0")
    l_fecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    # Colocar el Button inmediatamente después, en la misma fila
    boton_fecha = tk.Button(f_ingreso_datos, text="Seleccionar Fecha", command=obtener_fecha)
    boton_fecha.grid(row=1, column=1, sticky="e", padx=5, pady=5)

    # Centrar el Frame temporal en el grid
    f_ingreso_datos.grid_columnconfigure(0, weight=1)
    f_ingreso_datos.grid_columnconfigure(1, weight=1)


    label_hora_inicio = tk.Label(f_ingreso_datos, text="Hora inicio:")
    label_hora_inicio.grid(row=2, column=0, sticky="e", padx=5, pady=5)

    entry_hora_inicio = tk.Entry(f_ingreso_datos)
    entry_hora_inicio.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    label_hora_fin = tk.Label(f_ingreso_datos, text="Hora fin:")
    label_hora_fin.grid(row=3, column=0, sticky="e", padx=5, pady=5)

    entry_hora_fin = tk.Entry(f_ingreso_datos)
    entry_hora_fin.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    boton_fecha = tk.Button(f_ingreso_datos, text="Ejecutar", command=button_click)
    boton_fecha.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    return 