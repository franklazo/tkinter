import tkinter as tk
from tkinter import ttk


# Lógica ----------------------------------------------------------------------

def validar_numero(entrada):
    if entrada == "":
        return True

    try:
        int(entrada)
        return True

    except ValueError:
        return False


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def calcular(actual, incremento, operacion):
    try:
        actual = int(actual)
        incremento = int(incremento)

    except ValueError:
        return "Entrada inválida"


    if operacion == "+":
        return sumar(actual, incremento)

    elif operacion == "-":
        return restar(actual, incremento)


# Coordinación interfaz / lógica ----------------------------------------------

def actualizar_contador(operacion):
    incremento = var_incremento.get()

    if incremento == "":
        incremento = "0"

    resultado = calcular(
        var_contador.get(),
        incremento,
        operacion,
    )

    var_contador.set(resultado)


# Ventana principal -----------------------------------------------------------

ventana = tk.Tk()

ventana.title("Aplicación con estado")
ventana.geometry("240x192")


# Variables -------------------------------------------------------------------

var_contador = tk.StringVar(value=0)
var_incremento = tk.StringVar(value=0)


cmd_validar = ventana.register(validar_numero)


# Estilos ---------------------------------------------------------------------

style = ttk.Style()

style.configure("Min.TButton", width=1)


# Widgets ---------------------------------------------------------------------

frm_contador = ttk.Frame(ventana)

btn_disminuir = ttk.Button(
    frm_contador,
    text="-",
    command=lambda: actualizar_contador("-"),
    style="Min.TButton",
)

lbl_contador = ttk.Label(
    frm_contador,
    textvariable=var_contador,
    anchor="center",
)

btn_incrementar = ttk.Button(
    frm_contador,
    text="+",
    command=lambda: actualizar_contador("+"),
    style="Min.TButton",
)


btn_reiniciar = ttk.Button(
    ventana,
    text="Reiniciar",
    command=lambda: var_contador.set(0),
)


frm_incremento = ttk.Frame(ventana)

lbl_incremento = ttk.Label(frm_incremento, text="Incremento:")

ent_incremento = ttk.Spinbox(
    frm_incremento,
    textvariable=var_incremento,
    from_=0,
    to=1000,
    validate="key",
    validatecommand=(cmd_validar, "%P"),
    justify="center",
)


# Interfaz --------------------------------------------------------------------

frm_contador.pack(fill="x", padx=16, pady=16)

btn_disminuir.pack(side="left", fill="x", expand=True, padx=4, pady=4)
lbl_contador.pack(side="left", fill="x", expand=True, padx=4, pady=4)
btn_incrementar.pack(side="left", fill="x", expand=True, padx=4, pady=4)


btn_reiniciar.pack(fill="x", padx=20)


frm_incremento.pack(padx=16, pady=32)

lbl_incremento.pack(side="left", padx=4, pady=4)
ent_incremento.pack(side="left", padx=4, pady=4)


# Inicio de la aplicación -----------------------------------------------------

ventana.mainloop()
