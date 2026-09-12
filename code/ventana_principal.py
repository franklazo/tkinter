import tkinter as tk


ventana = tk.Tk()

ventana.title("Ventana principal")  # título de ventana
ventana.iconbitmap("logo.ico")      # ícono de ventana
ventana.geometry("320x480")         # tamaño inicial
ventana.minsize(320, 480)           # tamaño mínimo
ventana.maxsize(960, 640)           # tamaño máximo
ventana.resizable(True, True)       # tamaño redimensionable


ventana.mainloop()
