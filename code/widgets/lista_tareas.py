import tkinter as tk
from tkinter import ttk


def agregar_tarea():
    nueva_tarea = var_tarea.get().strip()

    if nueva_tarea:
        tareas.insert(tk.END, nueva_tarea)
        var_tarea.set("")

    entrada.focus()


def eliminar_tarea():
    seleccion = tareas.curselection()  # devuelve tupla → (0,)

    if seleccion:
        tareas.delete(seleccion[0])


ventana = tk.Tk()

ventana.title("Lista de tareas")
ventana.geometry("280x350")


var_tarea = tk.StringVar(value="")


ttk.Label(
    ventana,
    text="Nueva tarea:"
).pack(pady=16)


formulario = ttk.Frame(ventana)

formulario.pack()


entrada = ttk.Entry(
    formulario,
    textvariable=var_tarea
)

entrada.grid(row=0, column=0, padx=4)


ttk.Button(
    formulario,
    text="Agregar",
    command=agregar_tarea
).grid(row=0, column=1, padx=4)


tareas = tk.Listbox(
    ventana,
    width=32
)

tareas.pack(pady=16)


ttk.Button(
    ventana,
    text="Eliminar seleccionada",
    command=eliminar_tarea
).pack(pady=16)


ventana.mainloop()
