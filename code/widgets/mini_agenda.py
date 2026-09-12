import tkinter as tk
from tkinter import ttk


def agregar():
    nombre = var_nombre.get().strip()
    categoria = var_categoria.get()
    prioridad = var_prioridad.get()

    if nombre and categoria:
        agenda.insert(
            "",
            tk.END,
            values=(nombre, categoria, prioridad)
        )

        var_nombre.set("")
        entrada.focus()


ventana = tk.Tk()

ventana.title("Mini agenda")
ventana.geometry("900x300")


var_nombre = tk.StringVar()
var_categoria = tk.StringVar()
var_prioridad = tk.StringVar(value="media")
var_completada = tk.BooleanVar()


contenedor = ttk.Frame(ventana)

contenedor.pack(padx=16, pady=16)


formulario = ttk.Frame(contenedor)

formulario.grid(row=0, column=0, padx=8)


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
    text="Categoría:"
).grid(row=1, column=0, padx=4, pady=4)


ttk.Combobox(
    formulario,
    textvariable=var_categoria,
    values=["Estudio", "Personal", "Trabajo"],
    state="readonly"
).grid(row=1, column=1, padx=4, pady=4, sticky="w")


ttk.Label(
    formulario,
    text="Prioridad:"
).grid(row=2, column=0, padx=4, pady=4)


opciones_prioridad = ttk.Frame(formulario)

opciones_prioridad.grid(row=2, column=1, padx=4, pady=4, sticky="w")


ttk.Radiobutton(
    opciones_prioridad,
    text="Baja",
    value="baja",
    variable=var_prioridad
).pack(anchor="w")


ttk.Radiobutton(
    opciones_prioridad,
    text="Media",
    value="media",
    variable=var_prioridad
).pack(anchor="w")


ttk.Radiobutton(
    opciones_prioridad,
    text="Alta",
    value="alta",
    variable=var_prioridad
).pack(anchor="w")


ttk.Checkbutton(
    formulario,
    text="Completada",
    variable=var_completada
).grid(row=3, column=0, columnspan=2, padx=4, pady=4, sticky="w")


ttk.Button(
    formulario,
    text="Agregar",
    command=agregar
).grid(row=4, column=0, columnspan=2, padx=4, pady=8)


agenda = ttk.Treeview(
    contenedor,
    columns=["nombre", "categoria", "prioridad"],
    show="headings"
)

agenda.grid(row=0, column=1, padx=8)


agenda.heading("nombre", text="Nombre")
agenda.heading("categoria", text="Categoría")
agenda.heading("prioridad", text="Prioridad")


ventana.mainloop()
