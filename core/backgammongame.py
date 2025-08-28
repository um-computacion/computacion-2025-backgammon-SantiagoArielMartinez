from core.player import Jugador
from core.board import Tablero   
class Backgammon_game:
    def __init__(self):
        self.__turno__ = "Blanco"
        self.__contenedor__ = Tablero()
    
    def crear_jugador(self, nombre, color):
        return Jugador(nombre, color)
