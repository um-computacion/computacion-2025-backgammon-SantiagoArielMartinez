# 🐳 Cómo usar Docker en este proyecto

## ¿Qué es Docker?
Docker es como una "caja" que contiene todo lo necesario para ejecutar tu proyecto (Python, librerías, etc.) sin tener que instalarlo en tu computadora.

## Pasos simples:

### 1. Construir la imagen (hacer la "caja")
```bash
docker build -t backgammon-game .
```
Este comando crea la imagen con todo tu proyecto dentro.

### 2. Ejecutar los tests
```bash
docker run backgammon-game
```
Esto ejecuta los tests automáticamente y muestra el coverage.

### 3. Ejecutar el juego CLI
```bash
docker run -it backgammon-game python -m cli.cli
```
El `-it` permite interactuar con el juego desde la terminal.

### 4. Ver los tests sin ejecutar el juego
```bash
docker run backgammon-game python -m unittest discover -s tests
```

### 5. Ver el pylint
```bash
docker run backgammon-game pylint core/ tests/ cli/
```

### 6. Entrar dentro del contenedor (para explorar)
```bash
docker run -it backgammon-game bash
```
Esto te deja entrar al contenedor como si fuera una computadora virtual.

## Comandos útiles:

- **Ver las imágenes que tienes:**
  ```bash
  docker images
  ```

- **Borrar la imagen:**
  ```bash
  docker rmi backgammon-game
  ```

- **Ver contenedores ejecutándose:**
  ```bash
  docker ps
  ```

- **Borrar contenedores viejos:**
  ```bash
  docker container prune
  ```

## ¿Problemas?

Si algo falla, borra la imagen y vuelve a construirla:
```bash
docker rmi backgammon-game
docker build -t backgammon-game .
```

## Nota sobre Pygame:
El Dockerfile instala las librerías necesarias para pygame, pero la interfaz gráfica **NO** funciona dentro de Docker. Solo puedes usar el CLI (modo texto) dentro del contenedor.
