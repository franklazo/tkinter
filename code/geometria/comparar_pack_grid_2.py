import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Comparar pack y grid")
ventana.geometry("240x240")


ttk.Label(ventana, text="Mi aplicación").pack(pady=16)


formulario = ttk.Frame(ventana)
formulario.pack()


ttk.Label(formulario, text="Nombre:").grid(row=0, column=0, padx=2, pady=4)
ttk.Label(formulario, text="Edad:").grid(row=1, column=0, padx=2, pady=4)
ttk.Label(formulario, text="País").grid(row=2, column=0, padx=2, pady=4)


ttk.Entry(formulario).grid(row=0, column=1, padx=2, pady=4)
ttk.Entry(formulario).grid(row=1, column=1, padx=2, pady=4)
ttk.Entry(formulario).grid(row=2, column=1, padx=2, pady=4)


ttk.Button(ventana, text="Aceptar").pack(pady=24)


ventana.mainloop()
