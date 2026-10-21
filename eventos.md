# Eventos y `after`

## Asociar funciones

- `command`      → Acción del widget
- `.bind()`      → Evento del widget
- `.bind_all()`  → Evento de la aplicación
- `.trace_add()` → Evento de variable
- `.unbind()`    → Quitar binding

## Eventos del mouse

- `<Button-1>`        → Clic izquierdo
- `<Button-2>`        → Clic central
- `<Button-3>`        → Clic derecho
- `<Double-Button-1>` → Doble clic izquierdo
- `<Motion>`          → Movimiento
- `<Enter>`           → Entrada al widget
- `<Leave>`           → Salida del widget
- `<ButtonPress>`     → Botón presionado
- `<ButtonRelease>`   → Botón liberado

## Eventos del teclado

- `<Key>`       → Tecla cualquiera
- `<Return>`    → Tecla `Enter`
- `<Escape>`    → Tecla `Esc`
- `<F1>`        → Tecla `F1`
- `<Control-s>` → Combinación `Ctrl + S`

## Objeto `event`

```python
def function(event):
    # ...

    # Detener propagación
    return "break"
```

```python
# Usar como función y como callback
def function(event=None):
    # ...
```

- `.keysym` → Nombre simbólico de la tecla presionada
- `.char`   → Carácter ASCII de la tecla presionada
- `.x`      → Posición horizontal del puntero
- `.y`      → Posición vertical del puntero
- `.widget` → Instancia exacta del objeto widget

## Método `after`

```python
window.after(1000, function)
```

```python
# Identificador
id_after = window.after(1000, function)

# Cancelar ejecución
window.after_cancel(id_after)
```

```python
# Cuando termine el proceso actual
window.after_idle(function)
```
