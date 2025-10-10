from core.player import Jugador

class Tablero:
    def __init__(self):
        #Inicializar un tablero con 24 posiciones vacias
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
                              ]
        self.__almacen_ficha__ = {"blanco": 0, "negro": 0}
        self.__banco__ = {"blanco": 0, "negro": 0}
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
        if self.__almacen_ficha__[jugador.color] > 0:
            return False
        elif not (0 <= posicion_inicial < len(self.__contenedor__)):
            return False
        elif not (0 <= posicion_final < len(self.__contenedor__)):
            return False 
        inicio = self.__contenedor__[posicion_inicial]
        fin = self.__contenedor__[posicion_final]
        if not inicio:
            return False
        elif not fin:
            return True
        elif fin[0] == jugador.color:
            return True
        elif len(fin) == 1 and fin[0] != jugador.color:
            return True
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

    def estado_almacenamiento(self):
        return self.__almacen_ficha__
    
    def comer_checker(self, posicion_final, color):
        if not self.__contenedor__[posicion_final]:
            return False
        elif len(self.__contenedor__[posicion_final]) == 1 and self.__contenedor__[posicion_final][0] != color:
            enemigo = self.__contenedor__[posicion_final].pop()
            self.__contenedor__[posicion_final] = [color]
            self.__almacen_ficha__[enemigo] += 1
            return True
        elif len(self.__contenedor__[posicion_final]) >= 2:
            return False
        return False

    def sacar_checker_comida(self, color, posicion_final):
        if self.__almacen_ficha__[color] <= 0:
            return False
        if not (0 <= posicion_final < len(self.__contenedor__)):
            return False
        self.__contenedor__[posicion_final].append(color)
        self.__almacen_ficha__[color] -= 1
        return True
        
    def verificar_ganador(self,color):
        if color not in self.__almacen_ficha__:
            return False
        elif self.__almacen_ficha__[color] > 0:
            return False
        elif self.__contenedor__ == [[] for _ in range(24)]:
            return True
        return False
    
    def bear_off_permitido(self, color):
        if color == "blanco":
            rango = range(18, 24)
        else:
            rango = range(0, 6)
        for i in range(24):
            if i not in rango and self.__contenedor__[i]:
                if self.__contenedor__[i][0] == color:
                    return False
        return True
    
    def bear_off(self, posicion, color):
        if not self.bear_off_permitido(color):
            return False
        elif self.__contenedor__[posicion]:
            if self.__contenedor__[posicion][-1] == color:
                self.__contenedor__[posicion].pop()
                self.__banco__[color] += 1
                return True
        