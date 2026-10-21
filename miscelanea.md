# Miscelánea

## Diálogos `messagebox`

```python
from tkinter import messagebox
```

- `.showinfo()`    → Mostrar informacion
- `.showwarning()` → Mostrar advertencia
- `.showerror()`   → Mostrar error
- `.askyesno()`    → Solicitar confirmación (devuelve `bool`)

## Gestión de archivos

```python
from tkinter import filedialog
```

- `.askdirectory()`      → Seleccionar carpeta (devuelve **ruta**)
- `.askopenfilename()`   → Seleccionar archivos
- `.asksaveasfilename()` → Guardar archivo

### Propiedades

- `defaultextension` → Extensión por defecto
- `filetypes`        → Tipos de archivos

## Ventanas secundarias `Toplevel`

```python
root = tk.Tk()
window = tk.Toplevel(root)
```

- `.grab_set()` → Establecer como ventana de trabajo (**modal**)

## Menús

```python
menubar = tk.Menu(window)

cascade = tk.Menu(
    menubar,
    tearoff=False,  # evitar "desprender"
)
```

- `menu`             → Menú contenedor
- `label`            → Etiqueta de opción
- `command`          → Callback al accionar
- `accelerator`      → Etiqueta de atajo de teclado
- `.add_command()`   → Añadir opción ejecutable
- `.add_separator()` → Añadir separador
- `.add_cascade()`   → Añadir menú (desplegable) a barra

```python
window.config(menu=menubar)
```

## Imágenes

### `PhotoImage`

```python
image = tk.PhotoImage(
    file="photo.png"
)

label = tk.Label(
    window,
    image=image
)

label.pack()

label.image = image
```

### Pillow

```powershell
pip install pillow
```

```python
from PIL import Image, ImageTk
```

```python
image = Image.open("photo.jpg")

image = image.resize((300, 200))

tk_image = ImageTk.PhotoImage(image)

label = tk.Label(
    ventana,
    image=tk_image,
)

label.pack()

label.image = tk_image
```

## Validar al escribir

```python
validate = window.register(validate_function)

entry = ttk.Entry(
    window,
    validate="key",
    validatecommand=(validate, "%P")
)
```

## Cerrar ventana

```python
menu.add_command(
    label="Exit",
    command=ventana.destroy,
)
```
