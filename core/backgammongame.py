from core.player import jugador
from core.board import tablero   
class backgammon_game:
    def __init__(self):
        self.__turno__ = "Blanco"
        self.__contenedor__ = tablero()
    
    def crear_jugador(self, nombre, color):
        return jugador(nombre, color)