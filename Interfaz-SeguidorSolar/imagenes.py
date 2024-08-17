from PIL import Image, ImageTk

def cargar_imagen():
    # Cargar la imagen usando Pillow
    imagen_panel_solar = Image.open("./images/panel_solar_recortado.png")
    imagen_panel_solar = imagen_panel_solar.resize((50, 50), Image.Resampling.LANCZOS)  # Redimensionar la imagen
    imagen_panel_solar_tk = ImageTk.PhotoImage(imagen_panel_solar)

    return imagen_panel_solar_tk