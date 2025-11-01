# Usa Python 3.12
FROM python:3.12-slim

# Instala dependencias del sistema para pygame
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Carpeta de trabajo en el contenedor
WORKDIR /app

# Copia requirements y instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Comando por defecto: ejecuta tests con coverage
CMD ["sh", "-c", "coverage run -m unittest discover -s tests && coverage report -m"]