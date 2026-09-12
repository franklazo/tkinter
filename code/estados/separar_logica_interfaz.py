import tkinter as tk
from tkinter import ttk


def validar_numero(entrada):
    if entrada == "":
        return True

    if entrada == "-":
        return True

    try:
        float(entrada)
        return True
    except ValueError:
        return False


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división entre 0"

    return a / b


def calcular(a, b, operacion):
    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return "Error: entrada no válida"


    if operacion == "+":
        return sumar(a, b)

    elif operacion == "-":
        return restar(a, b)

    elif operacion == "*":
        return multiplicar(a, b)

    elif operacion == "/":
        return dividir(a, b)


# Ventana principal -----------------------------------------------------------

ventana = tk.Tk()

ventana.title("Separar lógica e interfaz")
ventana.geometry("240x192")


# Variables -------------------------------------------------------------------

var_numero1 = tk.StringVar(value=0)
var_numero2 = tk.StringVar(value=0)

var_resultado = tk.StringVar(value="Resultado...")

cmd_validar = ventana.register(validar_numero)


# Estilos ---------------------------------------------------------------------

style = ttk.Style()

style.configure("TButton", width=1)


# Widgets ---------------------------------------------------------------------

formulario = ttk.Frame(ventana)

ent_numero1 = ttk.Entry(
    formulario,
    textvariable=var_numero1,
    validate="key",
    validatecommand=(cmd_validar, "%P"),
    justify="right",
)

ent_numero2 = ttk.Entry(
    formulario,
    textvariable=var_numero2,
    validate="key",
    validatecommand=(cmd_validar, "%P"),
    justify="right",
)

botones = ttk.Frame(ventana)

btn_suma = ttk.Button(
    botones,
    text="+",
    command=lambda: var_resultado.set(
        calcular(
            var_numero1.get(),
            var_numero2.get(),
            "+",
        )
    ),
    style="TButton",
)

btn_resta = ttk.Button(
    botones,
    text="-",
    command=lambda: var_resultado.set(
        calcular(
            var_numero1.get(),
            var_numero2.get(),
            "-",
        )
    ),
    style="TButton",
)

btn_producto = ttk.Button(
    botones,
    text="*",
    command=lambda: var_resultado.set(
        calcular(
            var_numero1.get(),
            var_numero2.get(),
            "*",
        )
    ),
    style="TButton",
)

btn_division = ttk.Button(
    botones,
    text="/",
    command=lambda: var_resultado.set(
        calcular(
            var_numero1.get(),
            var_numero2.get(),
            "/",
        )
    ),
    style="TButton",
)

lbl_resultado = ttk.Label(ventana, textvariable=var_resultado)


# Interfaz --------------------------------------------------------------------

formulario.pack(padx=16, pady=16)

ent_numero1.pack(padx=4, pady=4)
ent_numero2.pack(padx=4, pady=4)

botones.pack(fill="x", padx=16)

btn_suma.pack(side="left", fill="x", expand=True, padx=4)
btn_resta.pack(side="left", fill="x", expand=True, padx=4)
btn_producto.pack(side="left", fill="x", expand=True, padx=4)
btn_division.pack(side="left", fill="x", expand=True, padx=4)

lbl_resultado.pack(padx=16, pady=16)


# Inicio de la aplicación -----------------------------------------------------

ventana.mainloop()
