from core.player import Jugador
from core.board import Tablero
from core.dice import Dados
from core.checkers import Ficha
class BackgammonGame:
    def __init__(self, nombre_jugador1,nombre_jugador2):
        self.__jugador1__ = Jugador(nombre_jugador1, "negro")
        self.__jugador2__ = Jugador(nombre_jugador2, "blanco")
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
    
    def get_turno_actual(self):
        return self.__turno__
    
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
    
    def puede_mover(self, jugador: Jugador):
        if jugador != self.__turno__:
            return False
        try:
            if len(self.__dados__.valores_dados()) == 0:
                return False
        except AttributeError:
            return False
        return True
    
    def mover_ficha(self, jugador : Jugador, posicion_inicial, posicion_final, valor_dado):
        if not self.puede_mover(jugador):
           return False
        if valor_dado not in self.__dados__.valores_dados():
           return False
        if self.__tablero__.movimiento_valido(posicion_inicial, posicion_final, jugador):
           self.__tablero__.mover_checker(posicion_inicial, posicion_final, jugador.color)
           self.__dados__.usar_valor(valor_dado)
           return True
        return False

    def usar_dados(self, valor):
        if valor in self.__dados__.valores_dados():
            self.__dados__.usar_valor(valor)
            return True
        else:
            return False
    
    def estado_juego(self):
        try:
            dados_actuales = self.__dados__.valores_dados()
        except AttributeError:
            dados_actuales = []
        return {
            "tablero" : self.__tablero__.estado_tablero(),
            "turno" : self.__turno__.nombre,
            "dados" : dados_actuales,
            "almacen_fichas" : self.__tablero__.__almacen_ficha__
        }    
    
    def hay_fichas_en_almacen(self, jugador : Jugador):
       return self.__tablero__.__almacen_ficha__[jugador.color] > 0

    def reingresar_ficha(self, jugador : Jugador, valor_dado):
       if not self.puede_mover(jugador):
           return False
       if not self.hay_fichas_en_almacen(jugador):
           return False
       if valor_dado not in self.__dados__.valores_dados():
           return False
       if jugador.color == "blanco":
           posicion_final = valor_dado - 1
       else:
           posicion_final = 24 - valor_dado
       if self.__tablero__.sacar_checker_comida(jugador.color, posicion_final):
           self.__dados__.usar_valor(valor_dado)
           return True
       return False

    
