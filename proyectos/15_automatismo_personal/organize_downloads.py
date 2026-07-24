"""Project from chapter 15: organize PDFs by rules kept as data.

The rule lives in rules.json, not in the code (chapter 15: "la regla como
dato, no como codigo"). Dry-run by default: nothing moves without --apply.
"""
import argparse
import json
import logging
import re
import shutil
from datetime import datetime
from pathlib import Path

logging.basicConfig(filename="organize.log", level=logging.INFO,
                    format="%(asctime)s %(message)s")


def load_rules(path: Path) -> dict:
    # The script reads the rules file at start and operates on what it finds
    return json.loads(path.read_text(encoding="utf-8"))


def target_for(pdf: Path, rules: dict) -> Path | None:
    name = pdf.name.lower()
    for rule in rules["rules"]:
        if re.search(rule["match"], name):
            date = datetime.fromtimestamp(pdf.stat().st_mtime)
            folder = rule["folder"].replace("{year}", str(date.year))
            new_name = rule.get("rename", pdf.name).replace(
                "{date}", date.strftime("%Y-%m-%d")).replace(
                "{original}", pdf.stem)
            return Path(rules["base_dir"]).expanduser() / folder / new_name
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Organiza PDFs segun rules.json (dry-run por defecto)")
    parser.add_argument("--source", default="~/Downloads")
    parser.add_argument("--rules", default="rules.json")
    parser.add_argument("--apply", action="store_true",
                        help="aplica los movimientos (sin esto, solo propone)")
    args = parser.parse_args()

    rules = load_rules(Path(args.rules))
    source = Path(args.source).expanduser()
    moves = []
    for pdf in sorted(source.glob("*.pdf")):
        target = target_for(pdf, rules)
        if target:
            moves.append((pdf, target))
    if not moves:
        print("Nada que organizar segun las reglas actuales.")
        return 0
    mode = "APLICANDO" if args.apply else "PROPUESTA (dry-run)"
    print(f"{mode} — {len(moves)} archivos:\n")
    for src, dst in moves:
        print(f"  {src.name}\n    -> {dst}")
        if args.apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            logging.info("moved %s -> %s", src, dst)
    if not args.apply:
        print("\nNo se ha movido nada. Revisa la propuesta y ejecuta con "
              "--apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
