class Tablero:
    def __init__(self):
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
                              ]
        self.__contenedor__[0] = ["blanco"] * 2
        self.__contenedor__[5] = ["negro"] * 5
        self.__contenedor__[7] = ["negro"] * 3
        self.__contenedor__[11] = ["blanco"] * 5
        self.__contenedor__[12] = ["negro"] * 2
        self.__contenedor__[17] = ["blanco"] * 5
        self.__contenedor__[19] = ["blanco"] * 3
        self.__contenedor__[23] = ["negro"] * 5

    def mostrar_contenedor(self):
        return self.__contenedor__
    
    def almacenamiento(self,ficha_blanca,ficha_negra):
        self.__almacen_ficha__ = {"blanco": ficha_blanca, "negras": ficha_negra}
        return f"blanco: {ficha_blanca}, negro: {ficha_negra}"
    
    def sacar_checker(self, posicion):
        if self.__contenedor__[posicion]:
            return self.__contenedor__[posicion].pop()
        return None
    
    def mover_checker(self,posicion_inicial, posicion_final):
        if 0 <= posicion_inicial < 24 and 0 < posicion_final < 24:
            if self.__contenedor__[posicion_inicial]:
                checker = self.__contenedor__[posicion_inicial].pop()
                self.__contenedor__[posicion_final].append(checker)
            return checker

    