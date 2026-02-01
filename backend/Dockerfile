# Python slim para no cargar cosas innecesarias
FROM python:3.9-slim
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app
WORKDIR /app
COPY requirements.txt .

# Instalacion dependencias
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "pytest", "tests", "-v", "-s", "--maxfail=1"]
