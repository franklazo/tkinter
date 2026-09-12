import tkinter as tk
from tkinter import ttk


def mostrar_resultado(event=None):
    nombre = ent_nombre.get().strip()

    if not nombre:
        var_resultado.set("Ingrese un nombre")
        return

    try:
        edad = int(ent_edad.get())

        if edad < 0 or edad > 150:
            var_resultado.set("Edad no válida")
            return

    except ValueError:
        var_resultado.set("Edad no válida")
        return

    mensaje = f"Hola {nombre}, tienes {edad} años."
    var_resultado.set(mensaje)


ventana = tk.Tk()

ventana.title("Formulario con teclado")
ventana.geometry("240x240")


formulario = ttk.Frame(ventana)
formulario.pack(fill="x", padx=16, pady=16)

formulario.columnconfigure(1, weight=1)


ttk.Label(
    formulario,
    text="Nombre:"
).grid(row=0, column=0, padx=4, pady=8)


ttk.Label(
    formulario,
    text="Edad:"
).grid(row=1, column=0, padx=4, pady=8)


ent_nombre = ttk.Entry(formulario)
ent_nombre.grid(
    row=0,
    column=1,
    padx=4,
    pady=8,
    sticky="ew"
)

ent_nombre.focus_set()

ent_nombre.bind(
    "<Return>",
    mostrar_resultado
)


ent_edad = ttk.Entry(formulario)
ent_edad.grid(
    row=1,
    column=1,
    padx=4,
    pady=8,
    sticky="ew"
)

ent_edad.bind(
    "<Return>",
    mostrar_resultado
)


ttk.Button(
    ventana,
    text="Aceptar",
    command=mostrar_resultado
).pack()


var_resultado = tk.StringVar(value="")

ttk.Label(
    ventana,
    textvariable=var_resultado,
    anchor="center"
).pack(
    fill="both",
    expand=True,
    pady=16
)


ventana.mainloop()
