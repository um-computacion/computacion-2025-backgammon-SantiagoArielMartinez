from core.player import Jugador

class Tablero:
    def __init__(self):
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
                              ]
    
    def tablero_inicial(self):
        self.__contenedor__[0] = ["blanco"] * 2
        self.__contenedor__[5] = ["negro"] * 5
        self.__contenedor__[7] = ["negro"] * 3
        self.__contenedor__[11] = ["blanco"] * 5
        self.__contenedor__[12] = ["negro"] * 2
        self.__contenedor__[17] = ["blanco"] * 5
        self.__contenedor__[19] = ["blanco"] * 3
        self.__contenedor__[23] = ["negro"] * 5
        return self.__contenedor__
    
    def estado_tablero(self):
        return self.__contenedor__
    
    
    def movimiento_valido(self, posicion_inicial, posicion_final, jugador : Jugador):
        if not (0 <= posicion_inicial < len(self.__contenedor__)) or not (0 <= posicion_final < len(self.__contenedor__)):
            return False 
        fin = self.__contenedor__[posicion_final]
        inicio = self.__contenedor__[posicion_inicial]
        color_jugador = jugador.color
        if not inicio:
            return False
        if not fin:
            return True
        if fin[0] == color_jugador:
            return True
        if len(fin) == 1 and fin[0] != color_jugador:
            return True
        return False

    def mover_checker(self,posicion_inicial, posicion_final):
        if 0 <= posicion_inicial < 24 and 0 < posicion_final < 24:
            if self.__contenedor__[posicion_inicial]:
                checker = self.__contenedor__[posicion_inicial].pop()
                self.__contenedor__[posicion_final].append(checker)
            return checker
        
    def sacar_checker(self, posicion):
        if self.__contenedor__[posicion]:
            return self.__contenedor__[posicion].pop()
        return None
    
    
    
    