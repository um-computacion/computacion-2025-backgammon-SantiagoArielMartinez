from core.player import Jugador
class BackgammonGame:
    def __init__(self, jugador1,jugador2):
        self.__jugador1__ = Jugador(jugador1, "Negras")
        self.__jugador2__ = Jugador(jugador2, "blancas")

    def get_jugador1(self):
        return self.__jugador1__
    
    def get_jugador2(self):
        return self.__jugador2__
    
