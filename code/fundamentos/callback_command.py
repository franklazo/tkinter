import tkinter as tk


def saludar():  # callback
    print("Hola, Tkinter")


ventana = tk.Tk()

ventana.title("Callback command")
ventana.geometry("160x80")


tk.Button(
    text="Saludar",
    command=saludar,  # callback
).pack(padx=24, pady=24)


ventana.mainloop()
