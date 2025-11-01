"""
Módulo que define la clase Dados para el juego de Backgammon.
"""
import random


class Dados:
    """
    Clase que representa los dados del juego de Backgammon.
    Maneja el lanzamiento de dos dados y el control de valores disponibles para usar.
    """
    def __init__(self):
        """
        Inicializa el objeto Dados sin valores iniciales.
        Los dados deben ser lanzados antes de poder usarse.
        """
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__valores__ = []

    def tirar_dado(self):
        """
        Lanza dos dados generando valores aleatorios entre 1 y 6.
        Si se obtienen valores iguales (dobles), se generan 4 valores en lugar de 2.
        Returns:
            Lista con los valores de los dados lanzados
        """
        try:
            self.__dado1__ = random.randint(1, 6)
            self.__dado2__ = random.randint(1, 6)
            if self.__dado1__ == self.__dado2__:
                self.__valores__ = [self.__dado1__]*4
            else:
                self.__valores__ = [self.__dado1__, self.__dado2__]
            return tuple(self.__valores__)
        except Exception: 
            return ()

    def valores_dados(self):
        """
        Retorna los valores de dados actualmente disponibles para usar.
        Returns:
            Lista con los valores de dados disponibles
        """
        return list(self.__valores__)

    def usar_valor(self, valor):
        """
        Marca un valor de dado como usado, eliminándolo de la lista de disponibles.
        Argumentos:
            valor: Valor del dado a eliminar (1-6)
        """
        if valor in self.__valores__:
            self.__valores__.remove(valor)
            return True
        return False

    def quedan_valores(self):
        """
        Verifica si quedan valores disponibles por usar.
        Returns:
            True si hay valores disponibles, False en caso contrario
        """
        return len(self.__valores__) > 0

    def resetear_dados(self):
        """
        Resetea los dados eliminando todos los valores disponibles.
        Se usa al finalizar un turno para preparar el siguiente lanzamiento.
        """
        self.__valores__.clear()
