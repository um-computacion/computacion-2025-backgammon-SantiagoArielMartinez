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
        try:
            if not (0 <= posicion_inicial < len(self.__contenedor__)):
                raise ValueError(f"Posicion inicial {posicion_inicial} fuera de rango (0-23)")
            if not (0 <= posicion_final < len(self.__contenedor__)):
                raise ValueError(f"Posicion final {posicion_final} fuera de rango (0-23)")
            fin = self.__contenedor__[posicion_final]
            inicio = self.__contenedor__[posicion_inicial]
            color_jugador = jugador.color
            if not inicio:
                raise ValueError(f"No hay piezas en la posicion inicial {posicion_inicial}")
            if not fin:
                return True
            if fin[0] == color_jugador:
                return True
            if len(fin) == 1 and fin[0] != color_jugador:
                return True
        except (ValueError, AttributeError) as e:
            print(f"Error en la validacion de movimiento: {e}")
            return False
        return False

    def mover_checker(self,posicion_inicial, posicion_final, color ):
        try:
            if self.__contenedor__[posicion_inicial][-1] != color:
                return None
            if 0 <= posicion_inicial < 24 and 0 <= posicion_final < 24:
                if self.__contenedor__[posicion_inicial]:
                    checker = self.__contenedor__[posicion_inicial].pop()
                    self.__contenedor__[posicion_final].append(checker)
                    return checker

        except (ValueError, IndexError) as e:
            print(f"Error al mover checker: {e}")
            return None

    def sacar_checker(self, posicion):
        if self.__contenedor__[posicion]:
            return self.__contenedor__[posicion].pop()
        return None

    def almacenamiento(self,color):
        self.__almacen_ficha__ = {"blanco": 0, "negras": 0}
        self.__almacen_ficha__[color] += 1
        return self.__almacen_ficha__