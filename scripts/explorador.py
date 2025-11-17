import os
import tkinter as tk
from tkinter import messagebox
from styles.styles import *

class ExploradorArchivos(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.config(bg=COLOR_FONDO)
        self.geometry("1050x450")
        self.title("Explorador de Archivos")
        self.protocol("WM_DELETE_WINDOW", self.regresar)

        self.current_path = os.getcwd()

        tk.Label(self, text="Explorador de Archivos", font=FUENTE_TITULO,
                bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

        self.label_ruta = tk.Label(self, text=f"Directorio actual: {self.current_path}",
                                bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.label_ruta.pack(pady=5)

        self.listbox = tk.Listbox(self, width=85, height=15,
                                font=("Consolas", 10))
        self.listbox.pack(padx=10, pady=10)

        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(pady=10)

        crear_boton(frame, "Refrescar", self.refrescar).pack(side="left", padx=5)
        crear_boton(frame, "Subir Nivel", self.subir_nivel).pack(side="left", padx=5)
        crear_boton(frame, "Abrir Carpeta", self.abrir).pack(side="left", padx=5)
        crear_boton(frame, "Regresar", self.regresar).pack(side="left", padx=5)

        self.refrescar()

    def refrescar(self):
        self.listbox.delete(0, tk.END)

        try:
            elementos = os.listdir(self.current_path)
            if not elementos:
                self.listbox.insert(tk.END, "(La carpeta está vacía)")
            else:
                for e in elementos:
                    self.listbox.insert(tk.END, e)

            self.label_ruta.config(text=f"Directorio actual: {self.current_path}")

        except PermissionError:
            messagebox.showerror("Error", "Acceso denegado.")

    def subir_nivel(self):
        self.current_path = os.path.dirname(self.current_path)
        self.refrescar()

    def abrir(self):
        sel = self.listbox.get(tk.ACTIVE)
        if not sel or sel == "(La carpeta está vacía)":
            return

        ruta = os.path.join(self.current_path, sel)
        if os.path.isdir(ruta):
            self.current_path = ruta
            self.refrescar()
        else:
            messagebox.showinfo("Archivo", f"Archivo seleccionado:\n{sel}")

    def regresar(self):
        self.destroy()
        self.main_window.deiconify()
