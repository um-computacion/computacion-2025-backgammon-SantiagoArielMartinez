class Jugador:
    """
    Clase que representa a un jugador en el juego de Backgammon.
    Cada jugador tiene un nombre único y un color de fichas (blanco o negro).
    """
    
    def __init__(self, nombre, color):
        """
        Inicializa un nuevo jugador con un nombre y color específico.
        Argumentos:
            nombre: Nombre del jugador (string)
            color: Color de las fichas del jugador ("blanco" o "negro")
        """
        self.__nombre__ = nombre
        self.__color__ = color
        self.__capturado__ = []
    
    @property
    def nombre(self) -> str:
        """Devuelve el nombre del jugador."""
        return self.__nombre__
    
    @nombre.setter
    def jugador(self, nombre: str) -> None:
        """
        Establece el nombre del jugador.
        Argumentos:
            nombre: Nuevo nombre para el jugador (string)
        Levanta:
            ValueError: Si el nombre no es un string o está vacío.
        """
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser un string no vacio")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre__ = nombre

    @property
    def color(self) -> str:
        """Devuelve el color de las fichas del jugador."""
        return self.__color__
    
    @color.setter
    def color(self, color: str) -> None:
        """
        Establece el color de las fichas del jugador.
        Argumentos:
            color: Nuevo color para las fichas del jugador (string)
        """
        self.__color__ = color