import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def seleccionar_archivo_general():
    archivo = filedialog.askopenfilename()

    if archivo:
        print(archivo)


def seleccionar_archivo_por_tipo():
    archivo = filedialog.askopenfilename(
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*"),
        ]
    )

    if archivo:
        print(archivo)


def guardar_archivo_general():
    archivo = filedialog.asksaveasfilename()

    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("Hola Tkinter")


def guardar_archivo_por_tipo():
    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Archivos de texto", "*.txt"),
        ]
    )

    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("Hola Tkinter")


def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()

    if carpeta:
        print(carpeta)


ventana = tk.Tk()

ventana.title("Gestión de archivos")
ventana.geometry("240x240")


botones = ttk.Frame(ventana)
botones.pack(fill="both", expand=True, padx=16, pady=16)

ttk.Button(
    botones,
    text="Seleccionar archivo general",
    command=seleccionar_archivo_general
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Seleccionar archivo por tipo",
    command=seleccionar_archivo_por_tipo
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Guardar archivo general",
    command=guardar_archivo_general
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Guardar archivo por tipo",
    command=guardar_archivo_por_tipo
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Seleccionar carpeta",
    command=seleccionar_carpeta
).pack(fill="both", expand=True, padx=4, pady=4)


ventana.mainloop()
