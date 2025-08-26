import random as randoms

class dados:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0

    def tirar_dado(self):
        self.__dado1__ = randoms.randint(1, 6)
        self.__dado2__ = randoms.randint(1, 6)

    def get_valor1(self):
        return self.__dado1__
    def get_valor2(self):
        return self.__dado2__