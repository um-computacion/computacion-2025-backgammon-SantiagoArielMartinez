#!/bin/bash
# Script para facilitar el uso de Docker en el proyecto

echo "🎲 Backgammon - Docker Helper"
echo "=============================="
echo ""
echo "¿Qué quieres hacer?"
echo ""
echo "1) Construir la imagen Docker"
echo "2) Ejecutar tests (con coverage)"
echo "3) Jugar en modo CLI"
echo "4) Ver pylint"
echo "5) Entrar al contenedor (bash)"
echo "6) Limpiar (borrar imagen)"
echo ""
read -p "Selecciona una opción (1-6): " opcion

case $opcion in
  1)
    echo "🏗️  Construyendo imagen..."
    docker build -t backgammon-game .
    ;;
  2)
    echo "🧪 Ejecutando tests..."
    docker run backgammon-game
    ;;
  3)
    echo "🎮 Iniciando juego CLI..."
    docker run -it backgammon-game python -m cli.cli
    ;;
  4)
    echo "📊 Ejecutando pylint..."
    docker run backgammon-game pylint core/ tests/ cli/
    ;;
  5)
    echo "💻 Entrando al contenedor..."
    docker run -it backgammon-game bash
    ;;
  6)
    echo "🗑️  Borrando imagen..."
    docker rmi backgammon-game
    docker container prune -f
    ;;
  *)
    echo "❌ Opción inválida"
    ;;
esac
