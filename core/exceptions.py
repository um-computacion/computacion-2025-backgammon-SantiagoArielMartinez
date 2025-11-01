"""
Excepciones simples para el juego de Backgammon.
"""

class PosicionInvalida(Exception):
    """Error cuando la posición no existe (debe ser 0-23)."""


class PosicionVacia(Exception):
    """Error cuando no hay fichas en la posición."""


class MovimientoInvalido(Exception):
    """Error cuando el movimiento no está permitido."""


class NoEsTuTurno(Exception):
    """Error cuando intentas jugar y no es tu turno."""


class SinDados(Exception):
    """Error cuando no hay dados disponibles."""


class ColorIncorrecto(Exception):
    """Error cuando el color no es 'blanco' o 'negro'."""
