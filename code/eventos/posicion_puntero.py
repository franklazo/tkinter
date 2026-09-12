import tkinter as tk
from tkinter import ttk


def clic(event):
    posicion.set(f"x = {event.x}\ny = {event.y}")


ventana = tk.Tk()

ventana.title("Posición del puntero")
ventana.geometry("320x320")

ventana.bind(
    "<Button-1>",
    clic
)


posicion = tk.StringVar(value="Clic para mostrar posición")

ttk.Label(
    ventana,
    textvariable=posicion,
    anchor="center"
).pack(fill="both", expand=True)


ventana.mainloop()
