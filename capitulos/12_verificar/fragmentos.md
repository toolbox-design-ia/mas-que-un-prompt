# Fragmentos no autocontenidos — 12. Verificar

Estos bloques del libro forman parte de archivos mayores o son extractos; se listan aqui como referencia fiel a lo impreso.

## Pruebas manuales que no dependen de la memoria

```python
Prueba 1 — Archivo vacío
  Entrada: archivo.md con cero contenido
  Acción: ejecutar python convertir.py archivo.md
  Resultado esperado: salida.html existe y contiene solo el esqueleto HTML básico

Prueba 2 — Título y párrafo simple
  Entrada: archivo.md con "# Título\n\nUn párrafo."
  Acción: ejecutar python convertir.py archivo.md
  Resultado esperado: salida.html contiene <h1>Título</h1> y <p>Un párrafo.</p>

Prueba 3 — Caracteres especiales
  Entrada: archivo.md con "Ñoño & <etiqueta>"
  Acción: ejecutar python convertir.py archivo.md
  Resultado esperado: salida.html contiene los caracteres correctamente escapados
```
