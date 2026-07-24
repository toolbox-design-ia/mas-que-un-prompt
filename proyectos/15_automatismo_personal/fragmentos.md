# Fragmentos no autocontenidos — 15. Un automatismo personal

Estos bloques del libro forman parte de archivos mayores o son extractos; se listan aqui como referencia fiel a lo impreso.

## El ciclo: pseudocódigo antes de código

```python
1. Leer el archivo de configuración
2. Listar todos los archivos en la carpeta fuente que coincidan con las extensiones configuradas
3. Para cada archivo:
   a. Intentar extraer la fecha del nombre del archivo según el formato configurado
   b. Si no hay fecha en el nombre, intentar leerla de los metadatos del archivo
   c. Si no hay fecha en ningún lugar, mover a la carpeta de fallback
   d. Si hay fecha, construir la ruta de destino según el patrón configurado
   e. Construir el nuevo nombre de archivo según el patrón configurado
   f. Si la ruta de destino no existe, crearla
   g. Mover el archivo a la nueva ruta con el nuevo nombre
4. Generar un reporte de lo que se hizo: movidos, saltados y errores
```
