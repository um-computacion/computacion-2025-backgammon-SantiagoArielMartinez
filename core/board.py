from core.player import Jugador

class Tablero:
    def __init__(self):
        #Inicializar un tablero con 24 posiciones vacias
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
                              ]
        self.__almacen_ficha__ = {"blanco": 0, "negro": 0}
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

        if posicion_inicial == -1:
            if 0<= posicion_final < len(self.__contenedor__):
                return True
            return False 
        
        if not (0 <= posicion_inicial < len(self.__contenedor__)):
            return False
        
        if not (0 <= posicion_final < len(self.__contenedor__)):
            return False 
        
        inicio = self.__contenedor__[posicion_inicial]
        fin = self.__contenedor__[posicion_final]

        if not inicio:
            return False
        
        if not fin:
            return True
        
        if fin[0] == jugador.color:
            return True
        
        if len(fin) == 1 and fin[0] != jugador.color:
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

    def almacenamiento(self,color):
        #Almacena una ficha capturada en el almacen
        self.__almacen_ficha__[color] += 1
        return self.__almacen_ficha__
    
    def comer_checker(self, posicion_final, color):

        if not self.__contenedor__[posicion_final]:
            return False
        
        if len(self.__contenedor__[posicion_final]) == 1 and self.__contenedor__[posicion_final][0] != color:
            enemigo = self.__contenedor__[posicion_final].pop()
            self.__contenedor__[posicion_final] = [color]
            self.__almacen_ficha__[enemigo] += 1
            return True
        
        if len(self.__contenedor__[posicion_final]) >= 2:
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
        