import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Interfaz adaptable")
ventana.geometry("320x320")


style = ttk.Style()

style.configure("Azul.TFrame", background="#486be0")
style.configure("Verde.TFrame", background="#48e08c")
style.configure("Rojo.TFrame", background="#e04848")


header = ttk.Frame(ventana, style="Azul.TFrame")
header.pack(fill="x", padx=16, pady=16)

ttk.Label(header, text="Título:").pack(padx=8, pady=8)


contenido = ttk.Frame(ventana, style="Verde.TFrame")
contenido.pack(fill="both", expand=True, padx=16)

contenido.rowconfigure(0, weight=1)
contenido.rowconfigure(1, weight=2)
contenido.columnconfigure(0, weight=1)
contenido.columnconfigure(1, weight=2)

ttk.Label(contenido, text="1", anchor="center").grid(row=0, column=0, padx=16, pady=16, sticky="nsew")
ttk.Label(contenido, text="2", anchor="center").grid(row=0, column=1, padx=16, pady=16, sticky="nsew")
ttk.Label(contenido, text="3", anchor="center").grid(row=1, column=0, padx=16, pady=16, sticky="nsew")
ttk.Label(contenido, text="4", anchor="center").grid(row=1, column=1, padx=16, pady=16, sticky="nsew")


footer = ttk.Frame(ventana, style="Rojo.TFrame")
footer.pack(fill="x", padx=16, pady=16)

botones = ttk.Frame(footer)
botones.pack(padx=8, pady=8, anchor="center")

ttk.Button(botones, text="Aceptar").pack(side="left", padx=8, pady=8)
ttk.Button(botones, text="Cancelar").pack(side="left", padx=8, pady=8)


ventana.mainloop()
