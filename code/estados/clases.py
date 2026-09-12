import tkinter as tk
from tkinter import ttk


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana

        self.entrada = ttk.Entry(self.ventana)
        self.entrada.pack(pady=20)

        self.boton = ttk.Button(
            self.ventana,
            text="Mostrar",
            command=self.mostrar,
        )

        self.boton.pack()

    def mostrar(self):
        print(self.entrada.get())


ventana = tk.Tk()

ventana.title("Clases")
ventana.geometry("240x120")


app = Aplicacion(ventana)


ventana.mainloop()
