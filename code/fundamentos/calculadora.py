import tkinter as tk


def sumar():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())

        suma = a + b

        resultado.config(
            text=f"Resultado: {suma}"
        )

    except ValueError:
        resultado.config(text="Entrada incorrecta")


ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("240x192")


formulario = tk.Frame(ventana)

formulario.pack(pady=16)


etiqueta1 = tk.Label(
    formulario,
    text="Número 1:"
)

etiqueta1.grid(row=0, column=0, padx=4, pady=4)


entrada1 = tk.Entry(formulario)

entrada1.grid(row=0, column=1)


etiqueta2 = tk.Label(
    formulario,
    text="Número 2:"
)

etiqueta2.grid(row=1, column=0, padx=4, pady=4)


entrada2 = tk.Entry(formulario)

entrada2.grid(row=1, column=1)


boton = tk.Button(
    ventana,
    text="Sumar",
    command=sumar
)

boton.pack()


resultado = tk.Label(
    ventana,
    text=""
)

resultado.pack(pady=24)


ventana.mainloop()
