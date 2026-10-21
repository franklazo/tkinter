import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def abrir_archivo():
    print("Abrir...")


def guardar_archivo():
    print("Guardar...")


ventana = tk.Tk()

ventana.title("Menús")
ventana.geometry("240x240")

image = Image.open("test.jpeg")

image = image.resize((300, 200))

tk_image = ImageTk.PhotoImage(image)

label = tk.Label(
    ventana,
    image=tk_image
)

label.pack()

label.image = tk_image

ventana.mainloop()
