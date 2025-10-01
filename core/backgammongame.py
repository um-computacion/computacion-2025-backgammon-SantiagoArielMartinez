from core.player import Jugador
from core.board import Tablero
from core.dice import Dados
from core.checkers import Ficha
class BackgammonGame:
    def __init__(self, jugador1,jugador2):
        self.__jugador1__ = Jugador(jugador1, "negro")
        self.__jugador2__ = Jugador(jugador2, "blanco")
        self.__tablero__ = Tablero()
        self.__dados__ = Dados()
        self.__turno__ = self.__jugador1__
        self.__tablero__.tablero_inicial()
        
    def get_jugador1(self):
        return self.__jugador1__
    
    def get_jugador2(self):
        return self.__jugador2__
    
    def get_tablero(self):
        return self.__tablero__
    
    def tirar_dados(self):
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
    
    def mover_ficha(self, jugador : Jugador, posicion_inicial, posicion_final, valor_dado):
        if jugador.color != self.__turno__.color:
           return False
        if jugador != self.__turno__:
           return False
        if valor_dado not in self.__dados__.valores_dados():
           return False
        if self.__tablero__.movimiento_valido(posicion_inicial, posicion_final, jugador):
           self.__tablero__.mover_checker(posicion_inicial, posicion_final, jugador.color)
           self.__dados__.usar_valor(valor_dado)
           return True
        return False
