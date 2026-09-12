import tkinter as tk


ventana = tk.Tk()

ventana.title("Contenedor Frame")


frame = tk.Frame(
    ventana,
    background="gold",             # color de fondo
    highlightthickness=8,          # grosor de contorno
    highlightbackground="tomato",  # color de contorno sin foco
)

frame.pack(
    padx=32,  # margen externo horizontal
    pady=16,  # margen externo vertical
)


label = tk.Label(
    frame,
    text="Hola, Tkinter",
)

label.pack(
    padx=32,   # margen externo horizontal
    pady=16,   # margen externo vertical
    ipadx=32,  # margen interno horizontal
    ipady=16,  # margen interno vertical
)


ventana.mainloop()
