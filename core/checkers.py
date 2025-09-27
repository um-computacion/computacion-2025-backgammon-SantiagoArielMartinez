class Ficha:
    def __init__(self, ficha, posicion):
       self.__ficha__ = ficha
       self.__posicion__ = posicion
  
    def get_ficha(self):
       return self.__ficha__
  
    def get_movimiento(self):
       return self.__posicion__

    def adentro_almacen(self):
       if self.__posicion__ == -1:
           return True
       return False

    def __str__(self):
         return f"{self.__ficha__} en {self.__posicion__}"