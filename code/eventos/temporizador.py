import tkinter as tk
from tkinter import ttk


temporizador = None
segundos = 0


def actualizar():
    global temporizador, segundos

    if temporizador is not None:
        segundos += 1
        var_segundos.set(segundos)

    temporizador = ventana.after(
        1000,
        actualizar
    )


def iniciar():
    global temporizador

    if temporizador is None:
        actualizar()


def detener():
    global temporizador

    if temporizador is not None:
        ventana.after_cancel(temporizador)
        temporizador = None


ventana = tk.Tk()

ventana.title("Temporizador")
ventana.geometry("160x160")


var_segundos = tk.IntVar(value=0)

ttk.Label(
    ventana,
    textvariable=var_segundos,
    font=("Arial", 24),
    anchor="center"
).pack(pady=24)


ttk.Button(
    ventana,
    text="Iniciar",
    command=iniciar
).pack()


ttk.Button(
    ventana,
    text="Detener",
    command=detener
).pack()


ventana.mainloop()
