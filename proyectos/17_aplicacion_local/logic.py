"""Logic layer of the local app (chapter 17): no web code in here."""
import sqlite3

DB = "hours.db"


def init_db() -> None:
    with sqlite3.connect(DB) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS entries ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                     "project TEXT NOT NULL, hours REAL NOT NULL, "
                     "created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)")


def add_entry(project: str, hours: str) -> None:
    project = project.strip()
    if not project:
        raise ValueError("El nombre del proyecto no puede estar vacio.")
    try:
        value = float(hours)
    except ValueError:
        raise ValueError(f"'{hours}' no es un numero de horas valido.")
    if not 0 < value <= 24:
        raise ValueError("Las horas deben estar entre 0.25 y 24.")
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO entries (project, hours) VALUES (?, ?)",
                     (project, value))


def totals() -> list[tuple[str, float]]:
    with sqlite3.connect(DB) as conn:
        return conn.execute(
            "SELECT project, ROUND(SUM(hours), 2) FROM entries "
            "GROUP BY project ORDER BY 2 DESC").fetchall()
