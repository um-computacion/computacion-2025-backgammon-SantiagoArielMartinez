# 🐳 Guía Rápida de Docker - Backgammon

## Comandos Básicos

### 1️⃣ Construir la imagen
```bash
docker build -t backgammon-game .
```

### 2️⃣ Ejecutar tests automáticamente
```bash
docker run backgammon-game
```

### 3️⃣ Jugar (modo interactivo)
```bash
docker run -it backgammon-game python -m cli.cli
```

## Usando el script helper (más fácil)

```bash
./docker-run.sh
```

Luego selecciona la opción que quieras del menú.

## Comandos avanzados

### Ver solo los tests unitarios
```bash
docker run backgammon-game python -m unittest discover -s tests -v
```

### Ejecutar pylint
```bash
docker run backgammon-game pylint core/
```

### Ver coverage completo
```bash
docker run backgammon-game sh -c "coverage run -m unittest discover && coverage report -m"
```

### Entrar al contenedor para explorar
```bash
docker run -it backgammon-game bash
```

## Con Docker Compose

```bash
# Construir y ejecutar
docker-compose up

# Solo construir
docker-compose build

# Ejecutar en segundo plano
docker-compose up -d

# Parar y limpiar
docker-compose down
```

## Limpieza

```bash
# Borrar imagen
docker rmi backgammon-game

# Limpiar todo Docker
docker system prune -a
```

## Troubleshooting

### Error: "Cannot connect to Docker daemon"
- Asegúrate de que Docker Desktop esté corriendo

### Error: "port already in use"
- Para este proyecto no necesitas puertos, así que no debería pasar

### La imagen es muy grande
- Usa `docker images` para ver el tamaño
- El Dockerfile usa `python:3.12-slim` que es ligero

### Los tests fallan en Docker pero andan local
- Verifica que el `.dockerignore` no esté excluyendo archivos importantes
- Revisa que `requirements.txt` tenga todas las dependencias
