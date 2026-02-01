# Imagen con Chrome + Selenium ya listo
FROM selenium/standalone-chrome:115.0

USER root

# Instalar Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar TODO el contenido del frontend
COPY . /app

# Instalar dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Ejecutar pruebas
CMD ["pytest", "-v", "-s", "--maxfail=1"]
