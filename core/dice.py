import random 

class Dados:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0

    def get_valor1(self):
            return self.__dado1__
    def get_valor2(self):
            return self.__dado2__
 
    def tirar_dado(self):
        try:
            self.__dado1__ = random.randint(1, 6)
            self.__dado2__ = random.randint(1, 6) 
            if self.__dado1__ == self.__dado2__:
                return (self.__dado1__, self.__dado2__,self.__dado1__,self.__dado2__)
            else: 
                return (self.__dado1__,self.__dado2__)
        except Exception as e:
            return  ()