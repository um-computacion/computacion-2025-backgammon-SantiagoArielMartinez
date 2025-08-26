class jugador: 

    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__capturado__ = []
    
    @property
    def jugador(self) -> str:
        return self.__nombre__
    
    @jugador.setter
    def jugador(self, nombre: str) -> None:
        self.__nombre__ = nombre

    @property
    def color(self) -> str:
        return self.__color__
    
    @color.setter
    def color(self, color: str) -> None:
        self.__color__ = color

    