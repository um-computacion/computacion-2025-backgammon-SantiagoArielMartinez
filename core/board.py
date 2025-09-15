from core.player import Jugador

class Tablero:
    def __init__(self):
        #Inicializar un tablero con 24 posiciones vacias
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
                              ]

    def tablero_inicial(self):
        #El tablero de 24 posiciones con las fichas en su lugar de origen
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
        #obtenes el estado del tablero actual
        return self.__contenedor__
       
    def movimiento_valido(self, posicion_inicial, posicion_final, jugador : Jugador):
        #verifica si el movimiento que realizo el jugador es correcto, a partir de las reglas del backgammon
        try:
            #Verifica que las posiciones esten en un rango valido
            if not (0 <= posicion_inicial < len(self.__contenedor__)):
                raise ValueError(f"Posicion inicial {posicion_inicial} fuera de rango (0-23)")
            if not (0 <= posicion_final < len(self.__contenedor__)):
                raise ValueError(f"Posicion final {posicion_final} fuera de rango (0-23)")
            #Obtener las fichas en las posiciones 
            fin = self.__contenedor__[posicion_final]
            inicio = self.__contenedor__[posicion_inicial]
            color_jugador = jugador.color
            #Verifica que hay fichas en la posicion inicial
            if not inicio:
                raise ValueError(f"No hay piezas en la posicion inicial {posicion_inicial}")
            #Movimiento valido a posicion vacia
            if not fin:
                return True
            #Movimiento valido a posicion con fichas del mismo color
            if fin[0] == color_jugador:
                return True
            #Movimiento valido para capturar un blot (una ficha enemiga)
            if len(fin) == 1 and fin[0] != color_jugador:
                return True
        except (ValueError, AttributeError) as e:
            print(f"Error en la validacion de movimiento: {e}")
            return False
        #Movimiento no valido (posicion bloqueada)
        return False

    def mover_checker(self,posicion_inicial, posicion_final, color ):
        try:
            #Verificar que la ficha pertenezca al jugador
            if self.__contenedor__[posicion_inicial][-1] != color:
                return None
            #Verificar que las posiciones estén en rango valido
            if 0 <= posicion_inicial < 24 and 0 <= posicion_final < 24:
                #verificar que hay fichas en la posicion inicial
                if self.__contenedor__[posicion_inicial]:
                    #mover la ficha
                    checker = self.__contenedor__[posicion_inicial].pop()
                    self.__contenedor__[posicion_final].append(checker)
                    return checker

        except (ValueError, IndexError) as e:
            print(f"Error al mover checker: {e}")
            return None

    def sacar_checker(self, posicion):
        #Retira una ficha de una posicion especifica 
        if self.__contenedor__[posicion]:
            return self.__contenedor__[posicion].pop()
        return None

    def almacenamiento(self,color):
        #Almacena una ficha capturada en el almacen
        self.__almacen_ficha__ = {"blanco": 0, "negras": 0}
        self.__almacen_ficha__[color] += 1
        return self.__almacen_ficha__
    
    def mover_con_dado(self,posicion_inicial, jugador :Jugador, tiro : tuple):
        movimientos_realizados = []
        for valor in tiro:
            if len(self.__contenedor__[posicion_inicial]) == 0:
                break
            if jugador.color == "blanco":
                posicion_final = posicion_inicial + valor
            else:
                posicion_final = posicion_inicial - valor
                
            if self.movimiento_valido(posicion_inicial,posicion_final,jugador):
                ficha = self.sacar_checker(posicion_inicial)
                if ficha:
                    self.__contenedor__[posicion_final].append(ficha)
                    movimientos_realizados.append((posicion_inicial, posicion_final, valor))
        return movimientos_realizados
