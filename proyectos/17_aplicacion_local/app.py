"""Project from chapter 17: a local web application in two layers.

Layer 1 (logic.py): what the app does. Layer 2 (this file): the web
interface. Persistence in SQLite: what the server remembers between
requests. Errors that inform instead of a bare 500.
"""
from flask import Flask, jsonify, render_template_string, request

import logic

app = Flask(__name__)
logic.init_db()

PAGE = """<!doctype html><meta charset="utf-8">
<title>Registro de horas</title>
<style>body{font-family:sans-serif;max-width:640px;margin:2rem auto}
input,button{padding:.4rem}table{border-collapse:collapse;margin-top:1rem}
td,th{border:1px solid #ccc;padding:.3rem .6rem}</style>
<h1>Registro de horas</h1>
<form method="post" action="/add">
  <input name="project" placeholder="proyecto" required>
  <input name="hours" type="number" step="0.25" min="0.25"
         placeholder="horas" required>
  <button>Registrar</button>
</form>
{% if error %}<p style="color:#a00">{{ error }}</p>{% endif %}
<table><tr><th>Proyecto</th><th>Horas</th></tr>
{% for project, total in rows %}
<tr><td>{{ project }}</td><td>{{ total }}</td></tr>
{% endfor %}</table>"""


@app.get("/")
def index():
    return render_template_string(PAGE, rows=logic.totals(), error=None)


@app.post("/add")
def add():
    try:
        logic.add_entry(request.form["project"], request.form["hours"])
    except ValueError as exc:
        # Errors that inform: the message says what to fix (chapter 17)
        return render_template_string(PAGE, rows=logic.totals(),
                                      error=str(exc)), 400
    return index()


@app.get("/api/totals")
def api_totals():
    return jsonify(dict(logic.totals()))


if __name__ == "__main__":
    # Local server: only reachable from this machine
    app.run(host="127.0.0.1", port=5000, debug=False)
