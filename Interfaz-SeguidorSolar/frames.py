import tkinter as tk

def create_frames(root):
    f_primer_fila =       tk.Frame(root)
    # Crear frames para cada sección
    f_ingreso_datos =       tk.Frame(f_primer_fila, borderwidth=2, relief="solid")
    f_angulos_sol =         tk.Frame(f_primer_fila, borderwidth=2, relief="solid")
    f_angulo_pitch =        tk.Frame(f_primer_fila, borderwidth=2, relief="solid")

    f_inferior_izquierda =  tk.Frame(root, borderwidth=2, relief="solid")
    f_inferior_derecha =    tk.Frame(root, borderwidth=2, relief="solid")

    # Colocar frames en la ventana usando grid
    f_primer_fila.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Frames dentro de Primer fila
    f_ingreso_datos.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")
    f_angulos_sol.grid(  row=0, column=1, padx=10, pady=0, sticky="nsew")
    f_angulo_pitch.grid( row=0, column=2, padx=10, pady=0, sticky="nsew")

    f_inferior_izquierda.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    f_inferior_derecha.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Configurar el grid para que los frames se expandan en la ventana principal
    root.grid_rowconfigure(0, weight=0)  # Título
    root.grid_rowconfigure(1, weight=1, minsize=200)  # Fila superior
    root.grid_rowconfigure(2, weight=1, minsize=300)  # Fila inferior
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Configurar el grid para que los frames se expandan en f_primer_fila
    f_primer_fila.grid_rowconfigure(0, weight=1)  # Fila interna que contiene los frames
    f_primer_fila.grid_columnconfigure(0, weight=1, minsize=150)
    f_primer_fila.grid_columnconfigure(1, weight=1, minsize=250)
    f_primer_fila.grid_columnconfigure(2, weight=1, minsize=250)

    # Configurar el grid dentro del frame "f_ingreso_datos"
    f_ingreso_datos.grid_rowconfigure(0, weight=1)
    f_ingreso_datos.grid_rowconfigure(1, weight=1)
    f_ingreso_datos.grid_rowconfigure(2, weight=1)
    f_ingreso_datos.grid_rowconfigure(3, weight=1)
    f_ingreso_datos.grid_rowconfigure(4, weight=1)
    f_ingreso_datos.grid_columnconfigure(0, weight=1)
    f_ingreso_datos.grid_columnconfigure(1, weight=1)
    f_ingreso_datos.grid_columnconfigure(2, weight=1)

    return f_ingreso_datos, f_angulos_sol, f_angulo_pitch, f_inferior_izquierda, f_inferior_derecha