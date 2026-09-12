import tkinter as tk


def convertir():
    try:
        grados = float(entrada.get())
        fahrenheit = grados * 9 / 5 + 32

        resultado.config(
            text=f"Fahrenheit: {fahrenheit}"
        )

    except ValueError:
        resultado.config(text="Entrada incorrecta")


ventana = tk.Tk()

ventana.title("Conversor")
ventana.geometry("240x160")


formulario = tk.Frame(ventana)

formulario.pack(pady=16)


etiqueta = tk.Label(
    formulario,
    text="Celsius:"
)

etiqueta.grid(row=0, column=0, padx=4)


entrada = tk.Entry(formulario)

entrada.grid(row=0, column=1)


boton = tk.Button(
    ventana,
    text="Convertir",
    command=convertir
)

boton.pack()


resultado = tk.Label(
    ventana,
    text=""
)

resultado.pack(pady=24)


ventana.mainloop()
