# 🐳 Uso de Docker para Backgammon

## Resumen Ejecutivo

Este proyecto está completamente dockerizado para facilitar su ejecución y testing en cualquier sistema operativo.

## 🎯 Los Dos Modos de Docker

### 1. Modo Testing 🧪

**Propósito**: Ejecutar la suite completa de tests unitarios con reporte de cobertura.

**Comando**:
```bash
docker run --rm backgammon-game
```

**Qué hace**:
- Ejecuta 197 tests unitarios
- Genera reporte de cobertura de código
- Muestra el porcentaje de código testeado (≈90%)
- Verifica que todo funcione correctamente

**Resultado esperado**:
```
.......................................................................
Ran 197 tests in 0.231s

OK

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
cli/__init__.py              0      0   100%
cli/cli.py                  97     18    81%   77-78, 82-84...
core/backgammongame.py     112     17    85%   102-103...
core/board.py              100      4    96%   91-92...
...
------------------------------------------------------
TOTAL                      383     40    90%
```

### 2. Modo Juego 🎮

**Propósito**: Jugar al Backgammon en modo interactivo CLI.

**Comando**:
```bash
docker run --rm -it backgammon-game python3 -m cli.cli
```

**Qué hace**:
- Inicia el juego de Backgammon
- Permite jugar contra la computadora
- Interfaz de línea de comandos interactiva
- Soporta todos los movimientos del juego

**Resultado esperado**:
```
=== BIENVENIDO AL JUEGO DE BACKGAMMON ===

--- MENU PRINCIPAL ---
1. Iniciar Nuevo Juego
2. Ver Reglas
3. Salir

Ingrese su opción: 
```

## 📦 Usando Docker Compose

Docker Compose simplifica los comandos:

### Modo Testing
```bash
docker-compose up backgammon-tests
```

### Modo Juego
```bash
docker-compose run backgammon-cli
```

### Ejecutar Pylint
```bash
docker-compose run backgammon-pylint
```

## 🔧 Instalación Inicial

**Paso 1**: Construir la imagen
```bash
docker build -t backgammon-game .
```

**Paso 2**: Elegir el modo que necesites (testing o juego)

## ⚠️ Notas Importantes

1. **Modo Testing**: Se ejecuta automáticamente, no requiere interacción
2. **Modo Juego**: Requiere la flag `-it` para modo interactivo
3. **Flag `--rm`**: Elimina el contenedor automáticamente al finalizar
4. **Pygame**: La interfaz gráfica NO funciona en Docker (requiere X11)
5. **CLI**: Funciona perfectamente en Docker

## 🚀 Flujo de Trabajo Recomendado

```bash
# 1. Construir la imagen
docker build -t backgammon-game .

# 2. Verificar que los tests pasan
docker run --rm backgammon-game

# 3. Si los tests pasan, jugar
docker run --rm -it backgammon-game python3 -m cli.cli
```

## 📊 Comandos Útiles

| Comando | Descripción |
|---------|-------------|
| `docker images` | Ver imágenes descargadas |
| `docker ps` | Ver contenedores en ejecución |
| `docker rm $(docker ps -aq)` | Eliminar todos los contenedores |
| `docker rmi backgammon-game` | Eliminar la imagen |

## 🐛 Solución de Problemas

### Error: "permission denied"
```bash
sudo usermod -aG docker $USER
# Luego cierra sesión y vuelve a iniciar
```

### Error: "Cannot connect to Docker daemon"
```bash
sudo systemctl start docker.service
```

### Reconstruir imagen después de cambios
```bash
docker build --no-cache -t backgammon-game .
```

---

**Autor**: Santiago Ariel Martinez  
**Universidad**: Universidad de Mendoza  
**Fecha**: Octubre 2025
