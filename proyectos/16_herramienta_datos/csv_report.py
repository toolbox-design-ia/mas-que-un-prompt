"""Project from chapter 16: a data tool with validation and a reproducible report.

CLI interface (the user as operator), validation BEFORE processing, and a
markdown report as reproducible artifact.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


def validate(rows: list[dict], required: list[str]) -> list[str]:
    # Validation before processing: from file to value (chapter 16)
    errors = []
    if not rows:
        errors.append("El CSV no tiene filas de datos.")
        return errors
    missing = [c for c in required if c not in rows[0]]
    if missing:
        errors.append(f"Faltan columnas requeridas: {', '.join(missing)}")
    for i, row in enumerate(rows, start=2):  # 1 = cabecera
        for col in required:
            if col in row and not str(row.get(col, "")).strip():
                errors.append(f"Fila {i}: la columna '{col}' esta vacia.")
    return errors[:20]


def summarize(rows: list[dict], amount_col: str, group_col: str) -> dict:
    totals: Counter = Counter()
    invalid = 0
    for row in rows:
        try:
            totals[row[group_col]] += float(
                str(row[amount_col]).replace(",", "."))
        except (KeyError, ValueError):
            invalid += 1
    return {"totals": totals, "invalid_rows": invalid,
            "row_count": len(rows)}


def write_report(source: Path, summary: dict, out: Path) -> None:
    lines = [f"# Informe de {source.name}", "",
             f"Filas procesadas: {summary['row_count']} "
             f"(no numericas: {summary['invalid_rows']})", "",
             "| Grupo | Total |", "| --- | --- |"]
    for group, total in summary["totals"].most_common():
        lines.append(f"| {group} | {total:.2f} |")
    grand = sum(summary["totals"].values())
    lines += ["", f"**Total general: {grand:.2f}**"]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resumen agrupado de un CSV con informe en markdown")
    parser.add_argument("csv_file")
    parser.add_argument("--group", default="categoria",
                        help="columna por la que agrupar")
    parser.add_argument("--amount", default="importe",
                        help="columna numerica a sumar")
    parser.add_argument("--out", default="informe.md")
    args = parser.parse_args()

    source = Path(args.csv_file)
    if not source.is_file():
        print(f"No existe el archivo {source}")
        return 1
    with open(source, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    errors = validate(rows, [args.group, args.amount])
    if errors:
        print("El archivo no supera la validacion:")
        for error in errors:
            print(" -", error)
        return 1
    summary = summarize(rows, args.amount, args.group)
    out = Path(args.out)
    write_report(source, summary, out)
    print(f"Informe escrito en {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
