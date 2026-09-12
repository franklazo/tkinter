import tkinter as tk
from tkinter import ttk


def contar_caracteres(event=None):
    caracteres = len(txt_editor.get("1.0", "end-1c"))
    resultado.set(f"Caracteres: {caracteres}")


def actualizar_conteo(event=None):
    ventana.after_idle(contar_caracteres)


def guardar(event=None):
    resultado.set("Guardando...")
    ventana.after(500, actualizar_conteo)


def seleccionar_todo(event=None):
    txt_editor.tag_add("sel", "1.0", "end")
    txt_editor.focus_set()

    if event is not None:
        return "break"


def limpiar(event=None):
    txt_editor.delete("1.0", "end")
    actualizar_conteo()

    if event is not None:
        return "break"


ventana = tk.Tk()

ventana.title("Mini editor de texto")
ventana.geometry("480x480")
ventana.minsize(360, 360)

ventana.bind("<Control-s>", guardar)


menus = ttk.Frame(ventana)
menus.pack(fill="x", padx=16, pady=8)


ttk.Button(
    menus,
    text="Guardar",
    command=guardar,
).pack(side="left", padx=8, pady=4)


ttk.Button(
    menus,
    text="Seleccionar todo",
    command=seleccionar_todo,
).pack(side="left", padx=8, pady=4)


ttk.Button(
    menus,
    text="Limpiar",
    command=limpiar,
).pack(side="right", padx=8, pady=4)


editor = ttk.Frame(ventana)
editor.pack(fill="both", expand=True, padx=16, pady=4)


txt_editor = tk.Text(
    editor,
    height=15,
)

txt_editor.pack(fill="both", expand=True, padx=8)

txt_editor.bind("<Key>", actualizar_conteo)
txt_editor.bind("<Control-a>", seleccionar_todo)
txt_editor.bind("<Control-e>", limpiar)


estado = ttk.Frame(ventana)
estado.pack(fill="x", padx=16, pady=16)


resultado = tk.StringVar(value="Caracteres: 0")

ttk.Label(
    estado,
    textvariable=resultado,
).pack()


ventana.mainloop()
