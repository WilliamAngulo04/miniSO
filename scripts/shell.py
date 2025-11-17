import os
import tkinter as tk
from styles.styles import *

class ShellEducativa(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.title("Shell Educativa")
        self.geometry("950x450")
        self.config(bg=COLOR_FONDO)
        self.protocol("WM_DELETE_WINDOW", self.regresar)

        tk.Label(self, text="Shell Educativa", font=FUENTE_TITULO,
                bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

        self.texto = tk.Text(self, width=80, height=15, bg="black", fg="lime",
                            font=("Consolas", 10))
        self.texto.pack()

        frame_entrada = tk.Frame(self, bg=COLOR_FONDO)
        frame_entrada.pack(pady=5)

        self.entrada = tk.Entry(frame_entrada, width=85, font=("Consolas", 11))
        self.entrada.pack()

        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(pady=10)

        crear_boton(frame, "Ejecutar", self.ejecutar).grid(row=0, column=0, padx=5)
        crear_boton(frame, "Limpiar", self.limpiar).grid(row=0, column=1, padx=5)
        crear_boton(frame, "Regresar", self.regresar).grid(row=0, column=2, padx=5)

    def ejecutar(self):
        cmd = self.entrada.get().strip()
        self.texto.insert(tk.END, f"$ {cmd}\n")

        if cmd in ["ls", "dir"]:
            for f in os.listdir():
                self.texto.insert(tk.END, f"{f}\n")

        elif cmd == "pwd":
            self.texto.insert(tk.END, os.getcwd() + "\n")

        elif cmd.startswith("echo "):
            self.texto.insert(tk.END, cmd[5:] + "\n")

        else:
            self.texto.insert(tk.END, "Comando no reconocido.\n")

        self.texto.insert(tk.END, "\n")
        self.texto.see(tk.END)
        self.entrada.delete(0, tk.END)

    def limpiar(self):
        self.texto.delete("1.0", tk.END)

    def regresar(self):
        self.destroy()
        self.main_window.deiconify()
