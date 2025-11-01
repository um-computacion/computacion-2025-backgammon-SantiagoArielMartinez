#!/bin/bash
Docker entrypoint script for Backgammon
case "$1" in
  test)
    echo "Running tests with coverage..."
    python -m coverage run -m unittest discover -s tests -p "test*.py" -v
    python -m coverage report
    python -m coverage xml
    ;;
  cli)
    echo "Starting CLI game..."
    python -m cli.cli
    ;;
esac

    