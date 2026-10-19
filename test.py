import tkinter as tk
from tkinter import ttk


def abrir_archivo():
    print("Abrir...")


def guardar_archivo():
    print("Guardar...")


ventana = tk.Tk()

ventana.title("Menús")
ventana.geometry("240x240")


barra_menu = tk.Menu(ventana)

menu_archivo = tk.Menu(
    barra_menu,
    tearoff=False,
)

menu_archivo.add_command(
    label="Abrir",
    command=abrir_archivo,
)

menu_archivo.add_command(
    label="Guardar",
    command=guardar_archivo,
)

menu_archivo.add_separator()

menu_archivo.add_command(
    label="Salir",
    command=ventana.destroy
)

barra_menu.add_cascade(
    label="Archivo",
    menu=menu_archivo,
)

ventana.config(menu=barra_menu)


ventana.mainloop()
