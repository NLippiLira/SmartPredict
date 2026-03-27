# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import numpy as np

# =========================
# Inicializar app
# =========================

app = Flask(__name__)
CORS(app)  # Permitir conexiones desde frontend

# =========================
# Cargar modelo
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")

model = joblib.load(model_path)

print("Modelo cargado correctamente ✅")

# =========================
# Ruta de prueba
# =========================

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API funcionando correctamente 🚀"})

# =========================
# Endpoint de predicción
# =========================

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validación de datos
        edad = data.get("edad")
        ingresos = data.get("ingresos")
        score = data.get("score")

        if edad is None or ingresos is None or score is None:
            return jsonify({"error": "Faltan datos"}), 400

        # Convertir a formato esperado por el modelo
        features = np.array([[edad, ingresos, score]])

        # Predicción
        prediction = model.predict(features)[0]

        return jsonify({
            "prediccion": int(prediction)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# =========================
# Ejecutar servidor (PRO)
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)