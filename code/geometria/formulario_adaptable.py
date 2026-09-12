import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Formulario adaptable")
ventana.geometry("320x320")


# style = ttk.Style()

# style.configure("Azul.TFrame", background="#486be0")
# style.configure("Verde.TFrame", background="#48e08c")
# style.configure("Rojo.TFrame", background="#e04848")


header = ttk.Frame(ventana, style="Azul.TFrame")
header.pack(fill="x", padx=16, pady=16)

ttk.Label(header, text="Registro").pack()


contenido = ttk.Frame(ventana, style="Verde.TFrame")
contenido.pack(fill="both", expand=True, padx=16)


ttk.Label(
    contenido, text="Nombre:", anchor="center"
).grid(row=0, column=0, padx=8, pady=4, sticky="nsew")
ttk.Label(
    contenido, text="Apellido:", anchor="center"
).grid(row=1, column=0, padx=8, pady=4, sticky="nsew")
ttk.Label(
    contenido, text="Correo:", anchor="center"
).grid(row=2, column=0, padx=8, pady=4, sticky="nsew")
ttk.Label(
    contenido, text="País:", anchor="center"
).grid(row=3, column=0, padx=8, pady=4, sticky="nsew")


ttk.Entry(contenido).grid(row=0, column=1, padx=8, pady=4, sticky="nsew")
ttk.Entry(contenido).grid(row=1, column=1, padx=8, pady=4, sticky="nsew")
ttk.Entry(contenido).grid(row=2, column=1, padx=8, pady=4, sticky="nsew")
ttk.Entry(contenido).grid(row=3, column=1, padx=8, pady=4, sticky="nsew")


terminos = tk.BooleanVar(value=False)

ttk.Checkbutton(
    contenido, text="Acepto los términos", variable=terminos
).grid(row=4, column=0, columnspan=2, padx=8, pady=8, sticky="nsew")


contenido.rowconfigure(0, weight=1)
contenido.rowconfigure(1, weight=1)
contenido.rowconfigure(2, weight=1)
contenido.rowconfigure(3, weight=1)
contenido.rowconfigure(4, weight=1)

contenido.columnconfigure(0, weight=1)
contenido.columnconfigure(1, weight=4)


footer = ttk.Frame(ventana, style="Rojo.TFrame")
footer.pack(fill="x", padx=16, pady=16)

ttk.Button(footer, text="Registrar").pack(side="right", padx=8, pady=8)


ventana.mainloop()
