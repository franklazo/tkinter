import tkinter as tk
from tkinter import ttk


def agregar():
    nombre = var_nombre.get().strip()
    telefono = var_telefono.get().strip()
    categoria = var_categoria.get()

    if nombre and telefono:
        gestor.insert(
            "",
            tk.END,
            values=(nombre, telefono, categoria)
        )

        var_nombre.set("")
        var_telefono.set("")
        entrada.focus()


def eliminar():
    seleccionados = gestor.selection()

    for seleccion in seleccionados:
        gestor.delete(seleccion)


ventana = tk.Tk()

ventana.title("Gestor de contactos")
ventana.geometry("640x320")


var_nombre = tk.StringVar()
var_telefono = tk.StringVar()
var_categoria = tk.StringVar(value="Amigos")


formulario = ttk.Frame(ventana)

formulario.pack(padx=16, pady=16)


ttk.Label(
    formulario,
    text="Nombre:"
).grid(row=0, column=0, padx=4, pady=4)


entrada = ttk.Entry(
    formulario,
    textvariable=var_nombre
)

entrada.grid(row=0, column=1, padx=4, pady=4, sticky="we")


ttk.Label(
    formulario,
    text="Teléfono:"
).grid(row=1, column=0, padx=4, pady=4)


ttk.Entry(
    formulario,
    textvariable=var_telefono
).grid(row=1, column=1, padx=4, pady=4, sticky="we")


ttk.Label(
    formulario,
    text="Categoría:"
).grid(row=2, column=0, padx=4, pady=4)


ttk.Combobox(
    formulario,
    textvariable=var_categoria,
    values=["Amigos", "Familia", "Trabajo"],
    state="readonly"
).grid(row=2, column=1, padx=4, pady=4)


botones = ttk.Frame(ventana)
botones.pack()

ttk.Button(
    botones,
    text="Agregar",
    command=agregar
).grid(row=0, column=0, padx=4)

ttk.Button(
    botones,
    text="Eliminar",
    command=eliminar
).grid(row=0, column=1, padx=4)


gestor = ttk.Treeview(
    ventana,
    columns=["nombre", "telefono", "categoria"],
    show="headings",
    height=5
)

gestor.pack(pady=24)


gestor.heading("nombre", text="Nombre")
gestor.heading("telefono", text="Teléfono")
gestor.heading("categoria", text="Categoría")


ventana.mainloop()