class Jugador: 

    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__capturado__ = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre__
    
    @nombre.setter
    def jugador(self, nombre: str) -> None:
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser un string no vacio")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre__ = nombre

    @property
    def color(self) -> str:
        return self.__color__
    
    @color.setter
    def color(self, color: str) -> None:
        self.__color__ = color