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
