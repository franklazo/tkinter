import tkinter as tk


ventana = tk.Tk()

ventana.title("Configuración de widget")


label = tk.Label(
    ventana,
    text="",
)

label.pack(padx=48, pady=24)

label.config(                    # configurar widget
    text="Hola, Tkinter",
    foreground="royalblue",      # color de texto
    font=("comic sans ms", 24),  # Tipo y tamaño de texto
)


ventana.mainloop()
