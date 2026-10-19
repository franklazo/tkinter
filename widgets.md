# Widgets

```python
import tkinter as tk
from tkinter import ttk
```

## Creación de widget

```python
tk.Label(contenedor).pack()  # no reutilizable
```

```python
widget = tk.Label(contenedor)  # reutilizable
widget.pack()  # colocar en la interfaz
```

## Propiedades y métodos

- `.config()` → Configurar propiedades

### Contenedor `Frame`

- `background`          → Color de fondo
- `highlightthickness`  → Grosor de contorno
- `highlightbackground` → Color de contorno sin foco

### Etiqueta `Label`

- `text`       → Contenido textual
- `font`       → Tipo, tamaño y estilo
- `background` → Color de fondo
- `foreground` → Color de texto
- `justify`    → Justificación
- `anchor`     → Alineación

### Botón `Button`

- `text`    → Contenido textual
- `state`   → Estado del botón
- `command` → Callback

### Entrada de texto `Entry`

- `.get()`       → Obtener texto
- `.delete()`    → Borrar texto
- `.insert()`    → Insertar texto
- `.focus_set()` → Enfocar entrada

### Cuadro combinado `Combobox`

- `values` → Lista de opciones
- `state`  → Estado de la entrada
- `.set()` → Establecer valor
- `.get()` → Obtener valor

### Casilla de verificación `Checkbutton`

- `text`     → Contenido textual
- `variable` → Vincular variable tkinter
- `command`  → Callback al cambiar de estado

### Botón de opción `Radiobutton`

- `text`     → Contenido textual
- `value`    → Valor de la opción
- `variable` → Vincular variable tkinter
- `command`  → Callback al cambiar de estado

### Área de texto `Text`

- `width`     → Anchura en caracteres
- `height`    → Altura en líneas
- `.get()`    → Obtener contenido
- `.insert()` → Insertar contenido
- `.delete()` → Borrar contenido

### Cuadro de lista `Listbox`

- `.insert()`       → Agregar elemento
- `.curselection()` → Obtener selección (tupla de posiciones)

### Caja de texto numérica `Spinbox`

- `from_`  → Valor mínimo
- `to`     → Valor máximo
- `.get()` → Obtener valor

### Barra de progreso `Progressbar`

- `length`   → Longitud en píxeles
- `mode`     → Comportamiento de la barra
- `value`    → Valor actual
- `.start()` → Iniciar animación
- `.stop()`  → Detener animación

### Contenedor `LabelFrame`

- `text` → Título del contenedor

### Tabla o vista de árbol `Treeview`

- `columns`      → Columnas de la tabla
- `show`         → Mostrar encabezados
- `height`       → Número de filas
- `.heading()`   → Definir encabezado
- `.insert()`    → Agregar dato
- `.selection()` → Obtener selección (tupla de posiciones)
- `.delete()`    → Borrar dato

### Control deslizante `Scale`

- `from_`    → Valor mínimo
- `to`       → Valor máximo
- `variable` → Vincular variable tkinter
- `.get()`   → Obtener valor

## Otros widgets

- `Canvas`      → Lienzo
- `Scrollbar`   → Barra de desplazamiento
- `PanedWindow` → Ventana con paneles
