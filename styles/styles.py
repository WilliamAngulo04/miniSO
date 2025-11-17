import tkinter as tk
from PIL import Image, ImageTk
import os

COLOR_FONDO = "#ecf0f1"
COLOR_BOTON = "#3498db"
COLOR_HOVER = "#2980b9"
COLOR_TEXTO = "#2c3e50"

FUENTE_TITULO = ("Segoe UI", 14, "bold")
FUENTE_NORMAL = ("Segoe UI", 10)

def crear_boton(master, texto, comando, width=25):
    boton = tk.Button(
        master,
        text=texto,
        font=FUENTE_NORMAL,
        bg=COLOR_BOTON,
        fg="white",
        activebackground=COLOR_HOVER,
        activeforeground="white",
        relief="flat",
        width=width,
        height=2,
        command=comando
    )
    boton.bind("<Enter>", lambda e: boton.config(bg=COLOR_HOVER))
    boton.bind("<Leave>", lambda e: boton.config(bg=COLOR_BOTON))
    return boton

def crear_boton_imagen(master, imagen_path, comando, size=(150, 150)):
    try:
        # Obtener la ruta absoluta de la imagen
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_path, imagen_path)
        
        # Cargar y redimensionar la imagen
        img = Image.open(full_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        # Crear botón con imagen
        boton = tk.Button(
            master,
            image=photo,
            command=comando,
            relief="flat",
            bg=COLOR_FONDO,
            activebackground=COLOR_FONDO,
            bd=0,
            cursor="hand2"
        )
        # Guardar referencia de la imagen para evitar que sea recolectada por el garbage collector
        boton.image = photo
        
        return boton
    except Exception as e:
        print(f"Error cargando imagen {imagen_path}: {e}")
        # Si falla, crear botón de texto como respaldo
        return crear_boton(master, "Módulo", comando, width=15)
