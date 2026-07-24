@app.route("/api/notas", methods=["POST"])
def crear_nota():
    try:
        datos = request.get_json()
        if not datos or not datos.get("texto"):
            return {"error": "El campo texto es obligatorio"}, 400

        texto = datos["texto"].strip()
        if not texto:
            return {"error": "El texto no puede estar vacío"}, 400

        nota = nueva_nota(texto)
        return {"ok": True, "nota": nota}, 200

    except Exception as e:
        app.logger.error(f"Error al crear nota: {e}")
        return {"error": "No se pudo guardar la nota. Inténtalo de nuevo."}, 500
