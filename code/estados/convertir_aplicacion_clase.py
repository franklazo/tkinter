import tkinter as tk
from tkinter import ttk


class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self, cantidad):
        self.valor += cantidad

    def disminuir(self, cantidad):
        self.valor -= cantidad

    def reiniciar(self):
        self.valor = 0


class Aplicacion():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Convertir aplicación a clase")
        self.ventana.geometry("240x192")

        self.contador = Contador()

        self.var_contador = tk.StringVar(value=self.contador.valor)
        self.var_incremento = tk.StringVar(value="0")

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):
        style = ttk.Style()

        style.configure(
            "Min.TButton",
            width=1
        )

    def crear_interfaz(self):
        self.frm_contador = ttk.Frame(self.ventana)

        self.btn_disminuir = ttk.Button(
            self.frm_contador,
            text="-",
            command=lambda: self.actualizar_contador("-"),
            style="Min.TButton",
        )

        self.lbl_contador = ttk.Label(
            self.frm_contador,
            textvariable=self.var_contador,
            anchor="center",
        )

        self.btn_incrementar = ttk.Button(
            self.frm_contador,
            text="+",
            command=lambda: self.actualizar_contador("+"),
            style="Min.TButton",
        )

        self.btn_disminuir.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4,
            pady=4
        )

        self.lbl_contador.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4,
            pady=4
        )

        self.btn_incrementar.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4,
            pady=4
        )

        self.frm_contador.pack(
            fill="x",
            padx=16,
            pady=16
        )

        self.btn_reiniciar = ttk.Button(
            self.ventana,
            text="Reiniciar",
            command=self.reiniciar,
        )

        self.btn_reiniciar.pack(
            fill="x",
            padx=20
        )

        self.frm_incremento = ttk.Frame(self.ventana)

        self.lbl_incremento = ttk.Label(
            self.frm_incremento,
            text="Incremento:"
        )

        self.ent_incremento = ttk.Spinbox(
            self.frm_incremento,
            textvariable=self.var_incremento,
            from_=0,
            to=1000,
            justify="center",
        )

        self.lbl_incremento.pack(
            side="left",
            padx=4,
            pady=4
        )

        self.ent_incremento.pack(
            side="left",
            padx=4,
            pady=4
        )

        self.frm_incremento.pack(
            padx=16,
            pady=32
        )

    def actualizar_contador(self, operacion):
        try:
            incremento = int(self.var_incremento.get())
        except ValueError:
            return

        if operacion == "+":
            self.contador.incrementar(incremento)

        elif operacion == "-":
            self.contador.disminuir(incremento)

        self.var_contador.set(self.contador.valor)

    def reiniciar(self):
        self.contador.reiniciar()
        self.var_contador.set(self.contador.valor)


ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()
