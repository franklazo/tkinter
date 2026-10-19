import tkinter as tk
from tkinter import ttk


cronometro = None
segundos = 0
centesimas = 0


def actualizar():
    global cronometro, segundos, centesimas

    centesimas += 1

    if centesimas == 100:
        segundos += 1
        centesimas = 0

    var_tiempo.set(f"{segundos:02}:{centesimas:02}")

    cronometro = ventana.after(
        10,
        actualizar
    )


def iniciar():
    global cronometro

    if cronometro is None:
        cronometro = ventana.after(
            10,
            actualizar
        )


def detener():
    global cronometro

    if cronometro is not None:
        ventana.after_cancel(cronometro)
        cronometro = None


def reiniciar():
    global cronometro, segundos, centesimas

    segundos = 0
    centesimas = 0

    var_tiempo.set(f"00:00")


ventana = tk.Tk()

ventana.title("Cronómetro")
ventana.geometry("240x180")


reloj = ttk.Frame(ventana)
reloj.pack(
    fill="both",
    expand=True,
    padx=16,
    pady=16,
)


var_tiempo = tk.StringVar(value="00:00")

ttk.Label(
    reloj,
    textvariable=var_tiempo,
    font=("Arial", 24)
).pack(side="bottom")


footer = ttk.Frame(ventana)
footer.pack(
    fill="x",
    expand=True,
    padx=16,
    pady=16
)


botones = ttk.Frame(footer)
botones.pack()


ttk.Button(
    botones,
    text="Iniciar",
    command=iniciar
).grid(row=0, column=0, padx=4, pady=4)


ttk.Button(
    botones,
    text="Detener",
    command=detener
).grid(row=0, column=1, padx=4, pady=4)


ttk.Button(
    botones,
    text="Reiniciar",
    command=reiniciar
).grid(row=1, column=0, columnspan=2, padx=4, pady=4)


ventana.mainloop()
