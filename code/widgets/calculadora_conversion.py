import tkinter as tk
from tkinter import ttk


def convertir():
    conversion = var_conversion.get()
    valor = var_valor.get()

    resultado = 0
    unidad = ""

    if conversion == "Celsius":
        resultado = valor * 9 / 5 + 32
        unidad = "ºF"

    elif conversion == "Kilómetros":
        resultado = valor / 1.609
        unidad = "mi"

    elif conversion == "Kilogramos":
        resultado = valor * 2.205
        unidad = "lb"

    mensaje = (
        "Resultado\n"
        "-------------\n"
        f"{resultado} {unidad}"
    )

    var_resultado.set(mensaje)
    entrada.focus()


ventana = tk.Tk()

ventana.title("Calculadora de conversión")
ventana.geometry("320x240")


var_conversion = tk.StringVar(value="Celsius")
var_valor = tk.DoubleVar(value=0.0)
var_resultado = tk.StringVar(value="")


formulario = ttk.Frame(ventana)

formulario.pack(padx=16, pady=16)


ttk.Label(
    formulario,
    text="Conversión:"
).grid(row=0, column=0, padx=4, pady=4)


ttk.Combobox(
    formulario,
    textvariable=var_conversion,
    values=["Celsius", "Kilómetros", "Kilogramos"],
    state="readonly"
).grid(row=0, column=1, padx=4, pady=4)


ttk.Label(
    formulario,
    text="Valor:"
).grid(row=1, column=0, padx=4, pady=4)


entrada = ttk.Entry(
    formulario,
    textvariable=var_valor
)

entrada.grid(row=1, column=1, padx=4, pady=4, sticky="we")


ttk.Button(
    ventana,
    text="Convertir",
    command=convertir
).pack()


ttk.Label(
    ventana,
    textvariable=var_resultado,
    justify="center"
).pack(pady=16)


ventana.mainloop()
