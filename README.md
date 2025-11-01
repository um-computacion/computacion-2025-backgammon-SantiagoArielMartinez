# 🎲 Juego Backgammon

**Alumno:** Martinez Santiago  
**Carrera:** Ingeniería en Informática  
**Universidad:** Universidad de Mendoza

## 📋 Descripción

Implementación del juego clásico de Backgammon en Python con múltiples interfaces:
- 🖥️ **CLI** (Interfaz de línea de comandos)
- 🎮 **Pygame** (Interfaz gráfica)

## 🚀 Instalación

### Opción 1: Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez.git
cd computacion-2025-backgammon-SantiagoArielMartinez

# Instalar dependencias
pip install -r requirements.txt
```

### Opción 2: Docker 🐳

```bash
# Construir la imagen
docker build -t backgammon-game .

# Ejecutar los tests
docker run backgammon-game

# Jugar en modo CLI
docker run -it backgammon-game python -m cli.cli
```

Ver [README-DOCKER.md](README-DOCKER.md) para más detalles sobre Docker.

## 🎮 Cómo Jugar

### Modo CLI (Terminal)
```bash
python -m cli.cli
```

### Modo Pygame (Gráfico)
```bash
python -m pygame_ui.pygame_ui
```

## 🧪 Tests

```bash
# Ejecutar todos los tests
python -m unittest discover -s tests

# Ver coverage
coverage run -m unittest discover -s tests
coverage report -m
```

## 📊 Análisis de Código

```bash
# Pylint
pylint core/ tests/ cli/
```

## 📁 Estructura del Proyecto

```
├── core/              # Lógica del juego
│   ├── backgammongame.py
│   ├── board.py
│   ├── player.py
│   ├── dice.py
│   ├── checkers.py
│   └── exceptions.py
├── cli/               # Interfaz de terminal
│   └── cli.py
├── pygame_ui/         # Interfaz gráfica
│   └── pygame_ui.py
├── tests/             # Tests unitarios
└── Dockerfile         # Configuración Docker
```

## 🛠️ Tecnologías

- Python 3.12
- Pygame
- Coverage
- Pylint
- Docker 