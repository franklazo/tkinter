# Elementos básicos

```python
import tkinter as tk  # importar tkinter
window = tk.Tk()      # crear ventana principal
window.mainloop()     # ciclo de eventos
```

## Ventana principal

- `.title()`      → Título de ventana
- `.iconbitmap()` → Ícono de ventana
- `.geometry()`   → Tamaño inicial
- `.minsize()`    → Tamaño mínimo
- `.maxsize()`    → Tamaño máximo
- `.resizable()`  → Tamaño redimensionable

## Widgets

```python
import tkinter as tk     # widgets clásicos
from tkinter import ttk  # widgets modernos
```

### Creación de widget

```python
tk.Label(contenedor).pack()    # no reutilizable

widget = tk.Label(contenedor)  # reutilizable
widget.pack()                  # colocar en la interfaz
```

### Widgets fundamentales

- `Frame`       → Contenedor
- `Label`       → Etiqueta
- `Button`      → Botón
- `Entry`       → Entrada de texto
- `Combobox`    → Cuadro combinado
- `Checkbutton` → Casilla de verificación
- `Radiobutton` → Botón de opción
- `Text`        → Área de texto
- `Listbox`     → Cuadro de lista
- `Spinbox`     → Caja de texto numérica
- `Progressbar` → Barra de progreso
- `LabelFrame`  → Contenedor
- `Treeview`    → Tabla o vista de árbol
- `Scale`       → Control deslizante

### Propiedades

- `foreground`          → Color de texto
- `background`          → Color de fondo
- `highlightthickness`  → Grosor de contorno
- `highlightbackground` → Color de contorno sin foco
- `text`                → Contenido textual
- `font`                → Tipo, tamaño y estilo
- `justify`             → Justificación de texto
- `anchor`              → Alineación de texto
- `value`               → Valor actual
- `values`              → Lista de valores
- `variable`            → Vincular variable tkinter
- `from_`               → Valor mínimo
- `to`                  → Valor máximo
- `command`             → Callback al accionar
- `state`               → Estado del widget
- `width`               → Anchura (caracteres)
- `height`              → Altura (líneas o filas)
- `length`              → Longitud (píxeles)
- `mode`                → Animación del widget
- `columns`             → Columnas de la tabla
- `show`                → Mostrar encabezados

### Métodos

- `.config()`       → Configurar propiedades
- `.get()`          → Obtener contenido
- `.set()`          → Establecer contenido
- `.insert()`       → Insertar contenido
- `.delete()`       → Borrar contenido
- `.focus_set()`    → Enfocar entrada
- `.curselection()` → Obtener selección (tupla de posiciones)
- `.selection()`    → Obtener selección (tupla de posiciones)
- `.heading()`      → Configurar encabezado
- `.start()`        → Iniciar animación
- `.stop()`         → Detener animación
