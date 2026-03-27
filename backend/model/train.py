# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# =========================
# 1. Crear dataset (simulado)
# =========================

data = {
    "edad": [25, 45, 35, 50, 23, 40, 60, 48, 33, 28],
    "ingresos": [300000, 800000, 500000, 900000, 200000, 700000, 1000000, 850000, 400000, 350000],
    "score": [600, 750, 680, 800, 550, 720, 820, 790, 650, 620],
    "aprobado": [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

# =========================
# 2. Separar variables
# =========================

X = df[["edad", "ingresos", "score"]]
y = df["aprobado"]

# =========================
# 3. Dividir dataset
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 4. Entrenar modelo
# =========================

model = LogisticRegression()
model.fit(X_train, y_train)

# =========================
# 5. Evaluación simple
# =========================

accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# =========================
# 6. Guardar modelo
# =========================

import os

# Obtener ruta absoluta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta donde se guardará el modelo
model_path = os.path.join(BASE_DIR, "model.pkl")

joblib.dump(model, model_path)

print("Modelo guardado correctamente ✅")