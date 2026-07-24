import json, uuid
from pathlib import Path
from datetime import datetime, timezone

NOTAS_PATH = Path("notas.json")

def leer_notas():
    if not NOTAS_PATH.exists():
        return []
    return json.loads(NOTAS_PATH.read_text(encoding="utf-8"))

def guardar_notas(notas):
    NOTAS_PATH.write_text(
        json.dumps(notas, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def nueva_nota(texto):
    notas = leer_notas()
    nota = {
        "id": str(uuid.uuid4())[:8],
        "texto": texto,
        "fecha": datetime.now(timezone.utc).isoformat()
    }
    notas.append(nota)
    guardar_notas(notas)
    return nota
