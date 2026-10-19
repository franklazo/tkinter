import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def mostrar_informacion():
    messagebox.showinfo(
        "Información",
        "El archivo se guardó correctamente."
    )


def mostrar_advertencia():
    messagebox.showwarning(
        "Advertencia",
        "El campo está vacío."
    )


def mostrar_error():
    messagebox.showerror(
        "Error",
        "No se pudo abrir el archivo."
    )


def eliminar():
    respuesta = messagebox.askyesno(
        "Confirmación",
        "¿Deseas eliminar este elemento?"
    )

    if respuesta:
        realizar_eliminacion()


def realizar_eliminacion():
    print("Eliminando...")
    print("Proceso completado.")


ventana = tk.Tk()

ventana.title("Diálogos")
ventana.geometry("200x200")


botones = ttk.Frame(ventana)
botones.pack(fill="both", expand=True, padx=16, pady=16)

ttk.Button(
    botones,
    text="Información",
    command=mostrar_informacion
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Advertencia",
    command=mostrar_advertencia
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Error",
    command=mostrar_error
).pack(fill="both", expand=True, padx=4, pady=4)

ttk.Button(
    botones,
    text="Preguntar Sí/No",
    command=eliminar
).pack(fill="both", expand=True, padx=4, pady=4)


ventana.mainloop()
