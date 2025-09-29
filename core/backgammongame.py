from core.player import Jugador
from core.board import Tablero
from core.dice import Dados
from core.checkers import Ficha
class BackgammonGame:
    def __init__(self, jugador1,jugador2):
        self.__jugador1__ = Jugador(jugador1, "Negras")
        self.__jugador2__ = Jugador(jugador2, "blancas")
        self.__tablero__ = Tablero()
        self.__dados__ = Dados()
        self.__turno__ = self.__jugador1__
    def get_jugador1(self):
        return self.__jugador1__
    
    def get_jugador2(self):
        return self.__jugador2__
    
    def get_tablero(self):
        return self.__tablero__
    
    def get_dados(self):
        self.__dados__.tirar_dado()
        return self.__dados__
    
    def obtener_turno(self):
        if self.__turno__ == self.__jugador1__:
            return f"Es el turno de {self.__jugador1__.nombre}"
        else:
            return f"Es el turno de {self.__jugador2__.nombre}"
        
    def cambiar_turno(self):
        if self.__turno__ == self.__jugador1__:
            self.__turno__ = self.__jugador2__
        else:
            self.__turno__ = self.__jugador1__
    
    
