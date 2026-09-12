import tkinter as tk
from tkinter import ttk


def mostrar():
    nombre = var_nombre.get()
    edad = var_edad.get()
    ciudad = var_ciudad.get()
    estudiante = var_estudiante.get()

    mensaje = (
        f"Nombre: {nombre}\n"
        f"Edad: {edad} años\n"
        f"Ciudad: {ciudad}\n"
        f"Estudiante: {'Sí' if estudiante else 'No'}\n"
    )

    var_resultado.set(mensaje)


# Ventana principal -----------------------------------------------------------

ventana = tk.Tk()

ventana.title("Variables")
ventana.geometry("300x300")


# Variables -------------------------------------------------------------------

var_nombre = tk.StringVar(value="")
var_edad = tk.IntVar(value=18)
var_ciudad = tk.StringVar(value="Lima")
var_estudiante = tk.BooleanVar(value=False)
var_resultado = tk.StringVar(value="Escribe tus datos")


# Widgets ---------------------------------------------------------------------

formulario = ttk.Frame(ventana)

lbl_nombre = ttk.Label(formulario, text="Nombre:")
lbl_edad = ttk.Label(formulario, text="Edad:")
lbl_ciudad = ttk.Label(formulario, text="Ciudad:")

ent_nombre = ttk.Entry(formulario, textvariable=var_nombre)
spb_edad = ttk.Spinbox(formulario, textvariable=var_edad, from_=0, to=100)
cbb_ciudad = ttk.Combobox(
    formulario,
    textvariable=var_ciudad,
    values=["Buenos Aires", "Lima", "Santiago"],
)

chk_estudiante = ttk.Checkbutton(
    formulario,
    text="Estudiante",
    variable=var_estudiante
)

btn_mostrar = ttk.Button(ventana, text="Mostrar", command=mostrar)

lbl_resultado = ttk.Label(
    ventana,
    textvariable=var_resultado,
    justify="center",
)


# Interfaz --------------------------------------------------------------------

formulario.pack(padx=16, pady=16)

lbl_nombre.grid(row=0, column=0, padx=4, pady=4, sticky="w")
lbl_edad.grid(row=1, column=0, padx=4, pady=4, sticky="w")
lbl_ciudad.grid(row=2, column=0, padx=4, pady=4, sticky="w")

ent_nombre.grid(row=0, column=1, padx=4, pady=4, sticky="ew")
spb_edad.grid(row=1, column=1, padx=4, pady=4, sticky="ew")
cbb_ciudad.grid(row=2, column=1, padx=4, pady=4, sticky="ew")

chk_estudiante.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=4,
    pady=4,
    sticky="w"
)

btn_mostrar.pack(padx=4, pady=4)

lbl_resultado.pack(padx=4, pady=4)


# Inicio de la aplicación -----------------------------------------------------

ventana.mainloop()
