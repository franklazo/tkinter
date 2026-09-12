import tkinter as tk
from tkinter import ttk


def mostrar():
    nombre = var_nombre.get()
    edad = var_edad.get()
    pais = var_pais.get()
    estudiante = var_estudiante.get()

    resultado.config(
        text=(
            f"Nombre: {nombre}\n"
            f"Edad: {edad}\n"
            f"País: {pais}\n"
            f"Estudiante: {estudiante}\n"
        ),
        justify="center"
    )


ventana = tk.Tk()

ventana.title("Perfil")
ventana.geometry("280x350")


formulario = ttk.LabelFrame(
    ventana,
    text="Perfil"
)

formulario.pack(
    pady=16,
    padx=16,
    fill="x"
)


var_nombre = tk.StringVar()
var_edad = tk.IntVar()
var_pais = tk.StringVar()
var_estudiante = tk.BooleanVar()


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
    text="Edad:"
).grid(row=1, column=0, padx=8, pady=4)


ttk.Spinbox(
    formulario,
    textvariable=var_edad,
    from_=0,
    to=150
).grid(row=1, column=1, pady=4)


ttk.Label(
    formulario,
    text="País:"
).grid(row=2, column=0, padx=8, pady=4)


ttk.Combobox(
    formulario,
    textvariable=var_pais,
    values=["Argentina", "Bolivia", "Chile", "Ecuador", "Perú"],
    state="readonly"
).grid(row=2, column=1, pady=4)


ttk.Checkbutton(
    formulario,
    text="Estudiante",
    variable=var_estudiante
).grid(row=3, column=1, pady=4)


ttk.Button(
    ventana,
    text="Mostrar",
    command=mostrar
).pack()


resultado = ttk.Label(
    ventana,
    text=""
)

resultado.pack(pady=24)


ventana.mainloop()
