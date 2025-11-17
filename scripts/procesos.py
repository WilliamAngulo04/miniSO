import tkinter as tk
from tkinter import messagebox
import psutil
from styles.styles import *

class GestionProcesos(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.config(bg=COLOR_FONDO)
        self.geometry("1050x450")
        self.title("Gestión de Procesos")
        self.protocol("WM_DELETE_WINDOW", self.regresar)

        tk.Label(self, text="Gestión de Procesos", font=FUENTE_TITULO,
                bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

        self.listbox = tk.Listbox(self, width=85, height=15,
                                font=("Consolas", 10))
        self.listbox.pack(padx=10, pady=10)

        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(pady=10)

        crear_boton(frame, "Refrescar", self.refrescar).pack(side="left", padx=5)
        crear_boton(frame, "Finalizar Proceso", self.terminar).pack(side="left", padx=5)
        crear_boton(frame, "Regresar", self.regresar).pack(side="left", padx=5)

        self.refrescar()

    def refrescar(self):
        self.listbox.delete(0, tk.END)
        for p in psutil.process_iter(['pid', 'name']):
            try:
                self.listbox.insert(tk.END, f"{p.info['pid']}  {p.info['name']}")
            except:
                pass

    def terminar(self):
        sel = self.listbox.get(tk.ACTIVE)
        if not sel:
            messagebox.showwarning("Atención", "Selecciona un proceso.")
            return

        pid = int(sel.split()[0])
        try:
            psutil.Process(pid).terminate()
            messagebox.showinfo("Éxito", f"Proceso {pid} terminado.")
            self.refrescar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def regresar(self):
        self.destroy()
        self.main_window.deiconify()
