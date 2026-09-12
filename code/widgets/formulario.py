import tkinter as tk
from tkinter import ttk


def registrar():
    nombre = var_nombre.get()
    lenguaje = var_lenguaje.get()
    activo = var_activo.get()

    resultado.config(
        text=(
            f"Nombre: {nombre}\n"
            f"Lenguaje: {lenguaje}\n"
            f"Activo: {activo}\n"
        ),
        justify="center"
    )


ventana = tk.Tk()

ventana.title("Formulario")
ventana.geometry("280x280")


formulario = ttk.LabelFrame(
    ventana,
    text="Datos"
)

formulario.pack(
    pady=16,
    padx=16,
    fill="x"
)


var_nombre = tk.StringVar()
var_lenguaje = tk.StringVar()
var_activo = tk.BooleanVar()


ttk.Label(
    formulario,
    text="Nombre:"
).grid(row=0, column=0, padx=8, pady=4)


ttk.Entry(
    formulario,
    textvariable=var_nombre,
    width=24
).grid(row=0, column=1, pady=4)


ttk.Label(
    formulario,
    text="Lenguaje:"
).grid(row=1, column=0, padx=8, pady=4)


ttk.Combobox(
    formulario,
    textvariable=var_lenguaje,
    values=["C++", "JavaScript", "Python"],
    state="readonly"
).grid(row=1, column=1, pady=4)


ttk.Checkbutton(
    formulario,
    text="Activo",
    variable=var_activo
).grid(row=2, column=1, pady=4)


ttk.Button(
    ventana,
    text="Registrar",
    command=registrar
).pack()


resultado = ttk.Label(
    ventana,
    text=""
)

resultado.pack(pady=24)


ventana.mainloop()
