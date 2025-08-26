import random as randoms

class dados:
    def __init__(self):
        self.dado1 = 0

    def tirar_dado(self):
        self.dado1 = randoms.randint(1, 6)

    def get_valor(self):
        return self.dado1