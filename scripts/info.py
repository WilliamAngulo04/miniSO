import tkinter as tk
import platform
import getpass
import shutil
from styles.styles import *

class InfoSistema(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.title("Información del Sistema")
        self.geometry("650x350")
        self.config(bg=COLOR_FONDO)
        self.protocol("WM_DELETE_WINDOW", self.regresar)

        tk.Label(self, text="Información del Sistema",
                font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

        usuario = getpass.getuser()
        so = platform.system()
        ver = platform.version()
        d = shutil.disk_usage(".")

        info = f"""
Usuario: {usuario}
Sistema Operativo: {so}
Versión: {ver}
Espacio Total: {d.total // (1024**3)} GB
Espacio Libre: {d.free // (1024**3)} GB
"""

        tk.Label(self, text=info, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                font=("Consolas", 11)).pack()

        crear_boton(self, "Regresar", self.regresar).pack(pady=15)

    def regresar(self):
        self.destroy()
        self.main_window.deiconify()
