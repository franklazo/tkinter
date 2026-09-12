import tkinter as tk
from tkinter import ttk


contador = 0


def actualizar():
    global contador

    contador += 1
    var_contador.set(contador)

    ventana.after(1000, actualizar)


ventana = tk.Tk()

ventana.title("Contador de tiempo")
ventana.geometry("320x320")


var_contador = tk.IntVar(value=0)

ttk.Label(
    ventana,
    textvariable=var_contador,
    font=("Arial", 24),
    anchor="center"
).pack(fill="both", expand=True)


ventana.after(
    1000,
    actualizar
)


ventana.mainloop()
