import tkinter as tk
from tkinter import ttk


def mostrar_seleccion():
    lenguaje = var_lenguaje.get()

    resultado.config(text=f"Seleccionado: {lenguaje}")


ventana = tk.Tk()

ventana.title("Selector")
ventana.geometry("280x280")


var_lenguaje = tk.StringVar(value="python")


ttk.Label(
    ventana,
    text="Lenguaje favorito:"
).pack(pady=16)


ttk.Radiobutton(
    ventana,
    text="Python",
    value="python",
    variable=var_lenguaje
).pack()


ttk.Radiobutton(
    ventana,
    text="C++",
    value="cpp",
    variable=var_lenguaje
).pack()


ttk.Radiobutton(
    ventana,
    text="JavaScript",
    value="javascript",
    variable=var_lenguaje
).pack()


ttk.Radiobutton(
    ventana,
    text="Java",
    value="java",
    variable=var_lenguaje
).pack()


ttk.Button(
    ventana,
    text="Mostrar",
    command=mostrar_seleccion
).pack(pady=16)


resultado = ttk.Label(
    ventana,
    text=""
)

resultado.pack(pady=16)


ventana.mainloop()
