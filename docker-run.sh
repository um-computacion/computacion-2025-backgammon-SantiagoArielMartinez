#!/bin/bash
# Script helper para ejecutar Docker en el proyecto Backgammon
# Autor: Santiago Martinez

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para mostrar el menú
show_menu() {
    echo "============================================"
    echo "🎲 Backgammon - Docker Helper"
    echo "============================================"
    echo "1) Construir imagen Docker"
    echo "2) Ejecutar tests con coverage"
    echo "3) Ejecutar CLI (modo interactivo)"
    echo "4) Ejecutar pylint"
    echo "5) Ver imágenes Docker"
    echo "6) Ver contenedores activos"
    echo "7) Limpiar contenedores"
    echo "8) Limpiar imagen"
    echo "9) Ayuda / Comandos útiles"
    echo "0) Salir"
    echo "============================================"
}

# Función para construir imagen
build_image() {
    echo -e "${YELLOW}Construyendo imagen Docker...${NC}"
    docker build -t backgammon-game .
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Imagen construida exitosamente${NC}"
    else
        echo -e "${RED}✗ Error al construir la imagen${NC}"
    fi
}

# Función para ejecutar tests
run_tests() {
    echo -e "${YELLOW}Ejecutando tests con coverage...${NC}"
    docker run --rm backgammon-game
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Tests ejecutados exitosamente${NC}"
    else
        echo -e "${RED}✗ Algunos tests fallaron${NC}"
    fi
}

# Función para ejecutar CLI
run_cli() {
    echo -e "${YELLOW}Iniciando CLI interactivo...${NC}"
    docker run --rm -it backgammon-game python3 -m cli.cli
}

# Función para ejecutar pylint
run_pylint() {
    echo -e "${YELLOW}Ejecutando pylint...${NC}"
    docker run --rm backgammon-game pylint core/ cli/
}

# Función para ver imágenes
list_images() {
    echo -e "${YELLOW}Imágenes Docker disponibles:${NC}"
    docker images | grep -E "REPOSITORY|backgammon"
}

# Función para ver contenedores
list_containers() {
    echo -e "${YELLOW}Contenedores Docker:${NC}"
    docker ps -a | grep -E "CONTAINER|backgammon"
}

# Función para limpiar contenedores
clean_containers() {
    echo -e "${YELLOW}Eliminando contenedores detenidos...${NC}"
    docker container prune -f
    echo -e "${GREEN}✓ Contenedores limpiados${NC}"
}

# Función para limpiar imagen
clean_image() {
    echo -e "${YELLOW}Eliminando imagen backgammon-game...${NC}"
    docker rmi backgammon-game
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Imagen eliminada${NC}"
    else
        echo -e "${RED}✗ Error al eliminar imagen${NC}"
    fi
}

# Función de ayuda
show_help() {
    echo "============================================"
    echo "📚 Comandos Útiles de Docker"
    echo "============================================"
    echo "Construcción:"
    echo "  docker build -t backgammon-game ."
    echo ""
    echo "Ejecución:"
    echo "  docker run backgammon-game                    # Tests"
    echo "  docker run -it backgammon-game python3 -m cli.cli  # CLI"
    echo "  docker run backgammon-game pylint core/ cli/  # Pylint"
    echo ""
    echo "Docker Compose:"
    echo "  docker-compose up backgammon-tests"
    echo "  docker-compose run backgammon-cli"
    echo "  docker-compose run backgammon-pylint"
    echo ""
    echo "Limpieza:"
    echo "  docker ps -a                  # Ver contenedores"
    echo "  docker rm <container_id>      # Eliminar contenedor"
    echo "  docker rmi <image_id>         # Eliminar imagen"
    echo "  docker system prune -a        # Limpiar todo"
    echo "============================================"
}

# Loop principal
while true; do
    show_menu
    read -p "Seleccione una opción: " option
    
    case $option in
        1)
            build_image
            ;;
        2)
            run_tests
            ;;
        3)
            run_cli
            ;;
        4)
            run_pylint
            ;;
        5)
            list_images
            ;;
        6)
            list_containers
            ;;
        7)
            clean_containers
            ;;
        8)
            clean_image
            ;;
        9)
            show_help
            ;;
        0)
            echo -e "${GREEN}¡Hasta luego!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Opción inválida${NC}"
            ;;
    esac
    
    echo ""
    read -p "Presione Enter para continuar..."
done
