import tkinter as tk
from tkinter import ttk


def tecla(event):
    tecla.set(f"[{event.keysym}]")


ventana = tk.Tk()

ventana.title("Detectar teclas")
ventana.geometry("320x320")

ventana.bind(
    "<Key>",
    tecla
)


tecla = tk.StringVar(value="Presionar cualquier tecla")

ttk.Label(
    ventana,
    textvariable=tecla,
    anchor="center"
).pack(fill="both", expand=True)


ventana.mainloop()
