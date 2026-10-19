import tkinter as tk


def saludar():
    nombre = entrada_nombre.get().strip()

    if not nombre:
        resultado.config(text="Escribe tu nombre")
        return

    try:
        edad = int(entrada_edad.get())
    except ValueError:
        resultado.config(text="Edad no válida")
        return

    mensaje = f"Hola, {nombre.capitalize()}.\nTienes {edad} años."
    resultado.config(text=mensaje)


def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    resultado.config(text="")

    entrada_nombre.focus()


ventana = tk.Tk()

ventana.title("Saludar")
ventana.geometry("240x200")


# --- Formulario --------------------------------------------------------------

formulario = tk.Frame(ventana)
formulario.pack(padx=16, pady=16)


campo_nombre = tk.Frame(formulario)
campo_nombre.pack(fill="x", pady=2)

campo_edad = tk.Frame(formulario)
campo_edad.pack(fill="x", pady=2)


tk.Label(
    campo_nombre,
    text="Nombre:",
).pack(side="left", padx=4)

tk.Label(
    campo_edad,
    text="Edad:",
).pack(side="left", padx=4)


entrada_nombre = tk.Entry(campo_nombre)
entrada_nombre.pack(side="right", padx=4)

entrada_nombre.focus()

entrada_edad = tk.Entry(campo_edad)
entrada_edad.pack(side="right", padx=4)


# --- Botones -----------------------------------------------------------------

botones = tk.Frame(ventana)
botones.pack(padx=16)


tk.Button(
    botones,
    text="Saludar",
    command=saludar,
).pack(side="left", padx=4)

tk.Button(
    botones,
    text="Limpiar",
    command=limpiar,
).pack(side="left", padx=4)


# --- Resultado ---------------------------------------------------------------

resultado = tk.Label(
    ventana,
    text="",
)

resultado.pack(padx=16, pady=24)


ventana.mainloop()
