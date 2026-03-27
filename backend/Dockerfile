# Usar imagen base estable
FROM python:3.10-slim

# Evitar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Output directo en consola
ENV PYTHONUNBUFFERED=1

# Crear carpeta app
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para correr la app
CMD ["python", "app.py"]