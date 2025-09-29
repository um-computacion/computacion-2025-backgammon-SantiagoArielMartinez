import random 

class Dados:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__valores = []
 
    def tirar_dado(self):
        try:
            self.__dado1__ = random.randint(1, 6)
            self.__dado2__ = random.randint(1, 6) 
            if self.__dado1__ == self.__dado2__:
                self.__valores__ = [self.__dado1__]*4
            else: 
                self.__valores__ = [self.__dado1__, self.__dado2__]
            return tuple(self.__valores__)
        except Exception as e:
            return  ()
    
    def valores_dados(self):
        return list(self.__valores__)
    