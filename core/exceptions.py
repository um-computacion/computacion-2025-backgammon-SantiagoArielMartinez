"""
Excepciones simples para el juego de Backgammon.
"""

class PosicionInvalida(Exception):
    """Error cuando la posición no existe (debe ser 0-23)."""
    pass

class PosicionVacia(Exception):
    """Error cuando no hay fichas en la posición."""
    pass

class MovimientoInvalido(Exception):
    """Error cuando el movimiento no está permitido."""
    pass

class NoEsTuTurno(Exception):
    """Error cuando intentas jugar y no es tu turno."""
    pass

class SinDados(Exception):
    """Error cuando no hay dados disponibles."""
    pass

class ColorIncorrecto(Exception):
    """Error cuando el color no es 'blanco' o 'negro'."""
    pass
