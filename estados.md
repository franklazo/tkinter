# Estados y arquitectura

## Variables

- `StringVar`  → Cadenas de caracteres
- `IntVar`     → Números enteros
- `DoubleVar`  → Números flotantes
- `BooleanVar` → Booleanos

### Métodos

- `.get()`       → Obtener valor
- `.set()`       → Modificar valor
- `.trace_add()` → Asociar función al cambiar

## Estructura

### Código

```text
DATOS → LÓGICA → INTERFAZ
```

```text
mi_app/
│
├── main.py
├── interfaz.py
├── modelos.py
├── logica.py
└── recursos/
```

### Componentes

```python
class Componente(ttk.Frame):
    def __init__(self, parent, texto):
        super().__init__(parent)

        #...
```
