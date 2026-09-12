import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Comparar pack y grid")
ventana.geometry("240x240")


ttk.Label(ventana, text="Mi aplicación").pack(pady=16)


formulario = ttk.Frame(ventana)
formulario.pack()


etiquetas = ttk.Frame(formulario)
etiquetas.pack(side="left", padx=2)


ttk.Label(etiquetas, text="Nombre:").pack(pady=4)
ttk.Label(etiquetas, text="Edad:").pack(pady=4)
ttk.Label(etiquetas, text="País").pack(pady=4)


entradas = ttk.Frame(formulario)
entradas.pack(side="left", padx=2)


ttk.Entry(entradas).pack(pady=4)
ttk.Entry(entradas).pack(pady=4)
ttk.Entry(entradas).pack(pady=4)


ttk.Button(ventana, text="Aceptar").pack(pady=24)


ventana.mainloop()
