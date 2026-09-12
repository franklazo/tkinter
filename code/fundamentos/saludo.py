import tkinter as tk


def saludar():
    nombre = entrada.get()

    if nombre:
        resultado.config(text=f"Hola, {nombre}")
    else:
        resultado.config(text="Escribe tu nombre")


ventana = tk.Tk()

ventana.title("Saludo")
ventana.geometry("240x160")


formulario = tk.Frame(ventana)

formulario.pack(pady=16)


etiqueta = tk.Label(
    formulario,
    text="Nombre:"
)

etiqueta.grid(row=0, column=0, padx=4)


entrada = tk.Entry(formulario)

entrada.grid(row=0, column=1)


boton = tk.Button(
    ventana,
    text="Saludar",
    command=saludar
)

boton.pack()


resultado = tk.Label(
    ventana,
    text=""
)

resultado.pack(pady=24)


ventana.mainloop()
