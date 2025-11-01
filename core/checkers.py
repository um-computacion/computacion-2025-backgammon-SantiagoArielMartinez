class Ficha:
    """
    Clase que representa una ficha (checker) en el juego de Backgammon.
    Cada ficha tiene un color que determina a qué jugador pertenece.
    """
    def __init__(self, ficha, posicion):
        """
        Inicializa una nueva ficha con un color específico y una posición.
        Argumentos:
            ficha: Color de la ficha ("blanco" o "negro")
            posicion: Posición de la ficha en el tablero, -1 si está en el almacén
        """
        self.__ficha__ = ficha
        self.__posicion__ = posicion  
    def get_ficha(self):
        """
        Devuelve el color de la ficha.
        """
        return self.__ficha__
    def get_movimiento(self):
        """
        Devuelve la posición de la ficha.
        """
        return self.__posicion__
    def adentro_almacen(self):
        """
        Verifica si la ficha está dentro del almacén.
        Devuelve:
            True si la ficha está en el almacén (posición -1), False en caso contrario.
        """
        if self.__posicion__ == -1:
            return True
        return False
    def __str__(self):
        """
        Devuelve una representación en cadena de la ficha y su posición.
        """
        return f"{self.__ficha__} en {self.__posicion__}"