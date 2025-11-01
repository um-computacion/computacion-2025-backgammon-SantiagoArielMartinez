# 🐳 Guía Docker para Backgammon

Esta guía te ayudará a ejecutar el proyecto de Backgammon usando Docker.

## ⚡ Inicio Rápido

### 1️⃣ Construir la imagen
```bash
docker build -t backgammon-game .
```

### 2️⃣ Modo Testing (Ejecutar Tests)
```bash
docker run --rm backgammon-game
```
Esto ejecuta todos los tests unitarios (197 tests) con cobertura de código.

### 3️⃣ Modo Juego (Jugar Backgammon)
```bash
docker run --rm -it backgammon-game python3 -m cli.cli
```
Esto inicia el juego en modo interactivo CLI donde puedes jugar contra la computadora.

---

## 📋 Requisitos Previos

- Docker instalado en tu sistema
- Docker Compose instalado

### Instalación de Docker en Linux (Debian/Ubuntu)

```bash
# Actualizar el sistema
sudo apt-get update

# Instalar dependencias
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings

# Agregar las claves GPG de Docker
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Añadir el repositorio
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Actualizar e instalar Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Agregar tu usuario al grupo docker
sudo usermod -aG docker $USER

# Iniciar el servicio Docker
sudo systemctl start docker.service
```

**Importante**: Después de agregar tu usuario al grupo docker, cierra sesión y vuelve a iniciar sesión para que los cambios surtan efecto.

### Verificar la instalación

```bash
docker --version
docker-compose --version
```

## 🚀 Uso con Docker

### 1. Construir la imagen

```bash
docker build -t backgammon-game .
```

### 2. Ejecutar los tests con coverage

```bash
docker run backgammon-game
```

O usando docker-compose:

```bash
docker-compose run backgammon-tests
```

### 3. Ejecutar el juego en modo CLI (Línea de Comandos)

```bash
docker run -it backgammon-game python3 -m cli.cli
```

O usando docker-compose:

```bash
docker-compose run backgammon-cli
```

### 4. Ejecutar pylint

```bash
docker run backgammon-game pylint core/ cli/
```

O usando docker-compose:

```bash
docker-compose run backgammon-pylint
```

## 📦 Comandos de Docker Compose

### Construir todos los servicios

```bash
docker-compose build
```

### Ejecutar tests

```bash
docker-compose up backgammon-tests
```

### Ejecutar CLI

```bash
docker-compose up backgammon-cli
```

### Ejecutar pylint

```bash
docker-compose up backgammon-pylint
```

### Limpiar contenedores

```bash
docker-compose down
```

### Limpiar contenedores y volúmenes

```bash
docker-compose down -v
```

## 🔧 Comandos útiles de Docker

| Comando | Descripción |
|---------|-------------|
| `docker images` | Lista todas las imágenes descargadas |
| `docker ps` | Muestra contenedores en ejecución |
| `docker ps -a` | Muestra todos los contenedores |
| `docker rm <container_id>` | Elimina un contenedor |
| `docker rmi <image_id>` | Elimina una imagen |
| `docker system prune` | Limpia recursos no usados |
| `docker logs <container_id>` | Muestra los logs de un contenedor |

## 📁 Estructura del Dockerfile

El Dockerfile está configurado para:

1. Usar Python 3.12-slim como imagen base
2. Instalar dependencias del sistema (SDL2 para pygame)
3. Instalar dependencias de Python desde requirements.txt
4. Copiar todo el código del proyecto
5. Ejecutar tests con coverage por defecto

## 🔄 Flujo de Trabajo Recomendado

1. **Desarrollo local**: Trabaja normalmente en tu máquina
2. **Testing con Docker**: Antes de hacer commit, prueba en Docker:
   ```bash
   docker-compose run backgammon-tests
   ```
3. **Verificación de código**:
   ```bash
   docker-compose run backgammon-pylint
   ```
4. **Commit y push**: Si todo pasa, haz commit de tus cambios

## ⚠️ Notas Importantes

- La interfaz Pygame **NO funcionará** en Docker sin configuración X11 adicional
- El CLI funciona perfectamente con `-it` (modo interactivo)
- Los archivos `__pycache__` y `.coverage` no se copian gracias al `.dockerignore`
- El contenedor monta el volumen actual, por lo que los cambios se reflejan inmediatamente

## 🐛 Solución de Problemas

### Error: "permission denied"

Asegúrate de que tu usuario esté en el grupo docker:

```bash
sudo usermod -aG docker $USER
```

Luego cierra sesión y vuelve a iniciar.

### Error: "Cannot connect to the Docker daemon"

Inicia el servicio Docker:

```bash
sudo systemctl start docker.service
```

### El contenedor no se detiene con Ctrl+C

Usa `Ctrl+C` dos veces o ejecuta en otra terminal:

```bash
docker stop <container_id>
```

## 📚 Recursos Adicionales

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best practices para Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Autor**: Santiago Ariel Martinez  
**Universidad**: Universidad de Mendoza  
**Materia**: Computación 2025
