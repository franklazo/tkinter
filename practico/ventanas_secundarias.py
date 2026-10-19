import tkinter as tk
from tkinter import ttk


def abrir_ventana():
    ventana_secundaria = tk.Toplevel(ventana)

    ventana_secundaria.title("Configuración")
    ventana_secundaria.geometry("240x80")

    ventana_secundaria.grab_set()  # establecer como ventana de trabajo

    ttk.Label(
        ventana_secundaria,
        text="Configuración",
    ).pack(padx=24, pady=24)


ventana = tk.Tk()

ventana.title("Ventanas secundarias")
ventana.geometry("240x240")


botones = ttk.Frame(ventana)
botones.pack(fill="both", expand=True, padx=16, pady=16)

ttk.Button(
    botones,
    text="Configuración",
    command=abrir_ventana
).pack(fill="both", expand=True, padx=16, pady=16)


ventana.mainloop()
