# Fragmentos no autocontenidos — 7. Git desde la instalación

Estos bloques del libro forman parte de archivos mayores o son extractos; se listan aqui como referencia fiel a lo impreso.

## .gitignore: qué no debe recordar el proyecto

```python
# Entorno virtual
venv/
.venv/
env/

# Secretos y configuración local
.env
.env.local
secrets.py
config_local.py

# Archivos de Python compilados
__pycache__/
*.pyc
*.pyo

# Datos grandes o modelos descargados
*.pkl
*.h5
data/raw/

# Sistema operativo
.DS_Store
Thumbs.db
```
