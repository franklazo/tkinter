import tkinter as tk


contador = 0


def disminuir():
    global contador

    contador -= 1
    resultado.config(text=f"Contador: {contador}")


def aumentar():
    global contador

    contador += 1
    resultado.config(text=f"Contador: {contador}")


ventana = tk.Tk()

ventana.title("Contador")
ventana.geometry("240x160")


resultado = tk.Label(
    ventana,
    text=f"Contador: {contador}"
)

resultado.pack(pady=16)


botones = tk.Frame(ventana)

botones.pack()


boton_menos = tk.Button(
    botones,
    width=8,
    text="-",
    command=disminuir
)

boton_menos.grid(row=0, column=0)


boton_mas = tk.Button(
    botones,
    width=8,
    text="+",
    command=aumentar
)

boton_mas.grid(row=0, column=1)


ventana.mainloop()
