# Miscelánea

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
