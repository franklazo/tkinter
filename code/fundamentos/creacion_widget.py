import tkinter as tk


ventana = tk.Tk()

ventana.title("Creación de widget")
ventana.geometry("240x120")


widget = tk.Label(         # crear widget
    ventana,               # contenedor o widget padre
    text="Hola, Tkinter",  # contenido textual
)

widget.pack()  # colocar en la interfaz


ventana.mainloop()
