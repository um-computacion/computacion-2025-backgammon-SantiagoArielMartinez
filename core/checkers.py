class Ficha:
   def __init__(self, ficha, posicion):
       self.__ficha__ = ficha
       self.__posicion__ = posicion
  
   def get_ficha(self):
       return self.__ficha__
  
   def get_movimiento(self):
       return self.__posicion__
