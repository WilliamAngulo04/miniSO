import tkinter as tk
from styles.styles import *
from scripts.explorador import ExploradorArchivos
from scripts.procesos import GestionProcesos
from scripts.shell import ShellEducativa
from scripts.info import InfoSistema

class MiniSO(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Sistema Operativo")
        self.geometry("700x600")
        self.config(bg=COLOR_FONDO)

        tk.Label(self, text="Mini Sistema Operativo Educativo",
                font=("Segoe UI", 16, "bold"),
                bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)

        # Frame para organizar los botones en una cuadrícula
        frame_botones = tk.Frame(self, bg=COLOR_FONDO)
        frame_botones.pack(pady=20)

        # Primera fila - Explorador
        frame_exp = tk.Frame(frame_botones, bg=COLOR_FONDO)
        frame_exp.grid(row=0, column=0, padx=20, pady=10)
        crear_boton_imagen(frame_exp, "imgs/explorador.png",
                        lambda: self.abrir_modulo(ExploradorArchivos)).pack()
        tk.Label(frame_exp, text="Explorador de Archivos", 
                bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_NORMAL).pack(pady=5)

        # Primera fila - Procesos
        frame_proc = tk.Frame(frame_botones, bg=COLOR_FONDO)
        frame_proc.grid(row=0, column=1, padx=20, pady=10)
        crear_boton_imagen(frame_proc, "imgs/procesos.png",
                        lambda: self.abrir_modulo(GestionProcesos)).pack()
        tk.Label(frame_proc, text="Gestión de Procesos", 
                bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_NORMAL).pack(pady=5)

        # Segunda fila - Shell
        frame_shell = tk.Frame(frame_botones, bg=COLOR_FONDO)
        frame_shell.grid(row=1, column=0, padx=20, pady=10)
        crear_boton_imagen(frame_shell, "imgs/shell.png",
                        lambda: self.abrir_modulo(ShellEducativa)).pack()
        tk.Label(frame_shell, text="Shell Educativa", 
                bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_NORMAL).pack(pady=5)

        # Segunda fila - Info
        frame_info = tk.Frame(frame_botones, bg=COLOR_FONDO)
        frame_info.grid(row=1, column=1, padx=20, pady=10)
        crear_boton_imagen(frame_info, "imgs/info.png",
                        lambda: self.abrir_modulo(InfoSistema)).pack()
        tk.Label(frame_info, text="Información del Sistema", 
                bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_NORMAL).pack(pady=5)

        # Botón de salir (texto)
        crear_boton(self, "Salir", self.destroy).pack(pady=20)

    def abrir_modulo(self, modulo):
        self.withdraw()
        modulo(self)

if __name__ == "__main__":
    app = MiniSO()
    app.mainloop()
