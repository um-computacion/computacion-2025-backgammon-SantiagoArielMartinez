# Dockerfile

# 1. Empezamos con una imagen de Python 3.12 (la que usás vos)
FROM python:3.12-slim

# 2. Ponemos las librerías del sistema que PYGAME necesita para funcionar
# (Aunque sea en modo terminal, los tests las necesitan)
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Creamos una carpeta para nuestro proyecto dentro del contenedor
WORKDIR /app

# 4. Copiamos PRIMERO el archivo de requerimientos
COPY requirements.txt .

# 5. Instalamos las librerías (pygame, coverage, pylint)
RUN pip install -r requirements.txt

# 6. Ahora sí, copiamos TODO tu proyecto (core, tests, cli, etc.)
COPY . .

# 7. Este es el comando que se ejecuta cuando corremos la imagen
#    - Primero corre Pylint (para ver el estilo)
#    - Después corre Coverage (para ver los tests)
#    - Si todo eso anda bien (&&), ejecuta tu juego en modo terminal (CLI)
CMD [ "sh", "-c", "pylint core/ tests/ && coverage run -m unittest discover -s tests && coverage report -m && python -m cli.cli" ]