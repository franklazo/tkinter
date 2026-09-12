import tkinter as tk
from tkinter import ttk


def actualizar_contador(*args):
    caracteres = len(var_entrada.get())
    var_resultado.set(f"Caracteres: {caracteres}")


# Ventana principal -----------------------------------------------------------

ventana = tk.Tk()

ventana.title("Interfaz reactiva")
ventana.geometry("240x160")


# Variables -------------------------------------------------------------------

var_entrada = tk.StringVar(value="")
var_resultado = tk.StringVar(value="Caracteres: 0")

var_entrada.trace_add("write", actualizar_contador)


# Widgets ---------------------------------------------------------------------

ent_nombre = ttk.Entry(ventana, textvariable=var_entrada)
lbl_resultado = ttk.Label(ventana, textvariable=var_resultado)


# Interfaz --------------------------------------------------------------------

ent_nombre.pack(fill="x", padx=32, pady=32)
lbl_resultado.pack(padx=32)


# Inicio de la aplicación -----------------------------------------------------

ventana.mainloop()
