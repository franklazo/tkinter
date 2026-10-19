import tkinter as tk
from tkinter import ttk


class Gastos:
    def __init__(self):
        self.datos = []

    def obtener_gastos(self):
        return self.datos.copy()

    def agregar_gasto(self, descripcion, cantidad, categoria):
        nuevo_dato = (
            descripcion,
            cantidad,
            categoria,
        )

        self.datos.append(nuevo_dato)

    def eliminar_gasto(self, posicion):
        self.datos.pop(posicion)


class Aplicacion():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de gastos")
        self.ventana.geometry("640x320")

        self.gastos = Gastos()

        self.var_descripcion = tk.StringVar(value="")
        self.var_cantidad = tk.StringVar(value="")
        self.var_categoria = tk.StringVar(value="")

        self.crear_interfaz()

    def crear_interfaz(self):

        # --- Formulario --- # ------------------------------------------------

        self.formulario = ttk.Frame(self.ventana)

        self.lbl_descripcion = ttk.Label(
            self.formulario,
            text="Descripción:",
        )

        self.lbl_cantidad = ttk.Label(
            self.formulario,
            text="Cantidad:",
        )

        self.lbl_categoria = ttk.Label(
            self.formulario,
            text="Categoría:",
        )

        self.ent_descripcion = ttk.Entry(
            self.formulario,
            textvariable=self.var_descripcion,
        )

        self.ent_cantidad = ttk.Entry(
            self.formulario,
            textvariable=self.var_cantidad,
        )

        self.ent_categoria = ttk.Entry(
            self.formulario,
            textvariable=self.var_categoria,
        )

        self.lbl_descripcion.grid(
            row=0,
            column=0,
            sticky="w",
            padx=4,
            pady=4,
        )

        self.lbl_cantidad.grid(
            row=1,
            column=0,
            sticky="w",
            padx=4,
            pady=4,
        )

        self.lbl_categoria.grid(
            row=2,
            column=0,
            sticky="w",
            padx=4,
            pady=4,
        )

        self.ent_descripcion.grid(
            row=0,
            column=1,
            padx=4,
            pady=4,
        )

        self.ent_cantidad.grid(
            row=1,
            column=1,
            padx=4,
            pady=4,
        )

        self.ent_categoria.grid(
            row=2,
            column=1,
            padx=4,
            pady=4,
        )

        self.formulario.pack(
            padx=32,
            pady=16,
        )

        # --- Botones --- # ---------------------------------------------------

        self.botones = ttk.Frame(self.ventana)

        self.btn_agregar = ttk.Button(
            self.botones,
            text="Agregar",
            command=self.agregar_gasto,
        )

        self.btn_eliminar = ttk.Button(
            self.botones,
            text="Eliminar",
            command=self.eliminar_gasto,
        )

        self.btn_agregar.pack(
            side="left",
            padx=4,
        )

        self.btn_eliminar.pack(
            side="right",
            padx=4,
        )

        self.botones.pack(
            padx=32,
            pady=8,
        )

        # --- Datos tabulados --- # -------------------------------------------

        self.trv_gastos = ttk.Treeview(
            ventana,
            columns=["descripcion", "cantidad", "categoria"],
            show="headings"
        )

        self.trv_gastos.heading("descripcion", text="Descripción")
        self.trv_gastos.heading("cantidad", text="Cantidad")
        self.trv_gastos.heading("categoria", text="Categoría")

        self.trv_gastos.column("descripcion", width=320)
        self.trv_gastos.column("cantidad", width=128)
        self.trv_gastos.column("categoria", width=128)

        self.trv_gastos.pack(
            padx=32,
            pady=32,
        )

    # --- Métodos --- # -------------------------------------------------------

    def agregar_gasto(self):
        descripcion = self.var_descripcion.get()
        cantidad = self.var_cantidad.get()
        categoria = self.var_categoria.get()

        if descripcion == "":
            return
        elif cantidad == "":
            return
        elif categoria == "":
            return

        self.gastos.agregar_gasto(descripcion, cantidad, categoria)
        self.actualizar_gastos()

        self.limpiar_formulario()

    def eliminar_gasto(self):
        seleccion = self.trv_gastos.selection()

        if seleccion:
            posicion = self.trv_gastos.index(seleccion[0])
            self.gastos.eliminar_gasto(posicion)
            self.actualizar_gastos()

    def actualizar_gastos(self):
        self.limpiar_gastos()

        for gasto in self.gastos.obtener_gastos():
            self.trv_gastos.insert(
                parent="",
                index="end",
                values=gasto
            )

    def limpiar_gastos(self):
        for gasto in self.trv_gastos.get_children():
            self.trv_gastos.delete(gasto)

    def limpiar_formulario(self):
        self.var_descripcion.set("")
        self.var_cantidad.set("")
        self.var_categoria.set("")

        self.ent_descripcion.focus_set()


# -----------------------------------------------------------------------------

ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()
