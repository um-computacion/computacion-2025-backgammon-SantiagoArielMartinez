"""
Módulo que contiene la clase principal del juego de Backgammon.
Controla el flujo del juego, turnos y movimientos.
"""
from core.player import Jugador
from core.board import Tablero
from core.dice import Dados
from core.exceptions import NoEsTuTurno, SinDados
class BackgammonGame:
    """
    Clase principal que controla el flujo del juego de Backgammon.
    """
    def __init__(self, nombre_jugador1, nombre_jugador2):
        """
        Inicializa un nuevo juego de Backgammon con dos jugadores.
        Arggumentos:
            nombre_jugador1: Nombre del primer jugador (fichas negras)
            nombre_jugador2: Nombre del segundo jugador (fichas blancas)
        """
        self.__jugador1__ = Jugador(nombre_jugador1, "negro")
        self.__jugador2__ = Jugador(nombre_jugador2, "blanco")
        self.__tablero__ = Tablero()
        self.__dados__ = Dados()
        self.__turno__ = self.__jugador1__
        self.__tablero__.tablero_inicial()
    def get_jugador1(self):
        """
        Retorna el primer jugador del juego.
        Returns:
            Objeto Jugador con fichas negras
        """
        return self.__jugador1__
    def get_jugador2(self):
        """
        Retorna el segundo jugador del juego.
        Returns:
            Objeto Jugador con fichas blancas
        """
        return self.__jugador2__
    def get_tablero(self):
        """
        Retorna el tablero actual del juego.
        Returns:
            Objeto Tablero con el estado actual de las fichas
        """
        return self.__tablero__
    def get_turno_actual(self):
        """
        Retorna el jugador que tiene el turno actual.
        Returns:
            Objeto Jugador al que le corresponde jugar
        """
        return self.__turno__
    def tirar_dados(self):
        """
        Tira los dados para iniciar un nuevo turno.
        Genera dos valores aleatorios entre 1 y 6.
        Returns:
            Objeto Dados con los valores generados
        """
        self.__dados__.tirar_dado()
        return self.__dados__
    def finalizar_turno(self):
        """
        Finaliza el turno actual del jugador.
        Resetea los dados disponibles y cambia el turno al otro jugador.
        """
        self.__dados__.resetear_dados()
        self.cambiar_turno()
    def obtener_turno(self):
        """
        Retorna un mensaje de texto indicando de quién es el turno actual.
        Returns:
            String con el mensaje "Es el turno de [nombre_jugador]"
        """
        if self.__turno__ == self.__jugador1__:
            return f"Es el turno de {self.__jugador1__.nombre}"
        return f"Es el turno de {self.__jugador2__.nombre}"
    def cambiar_turno(self):
        """
        Cambia el turno del jugador actual al otro jugador.
        Si es el turno del jugador 1, pasa al jugador 2 y viceversa.
        """
        if self.__turno__ == self.__jugador1__:
            self.__turno__ = self.__jugador2__
        else:
            self.__turno__ = self.__jugador1__
    def puede_mover(self, jugador: Jugador):
        """
        Verifica si un jugador puede realizar movimientos en este momento.
        Valida que sea su turno y que tenga dados disponibles para usar.
        Argumentos:
            jugador: Objeto Jugador a verificar
        Returns:
            True si puede mover, False en caso contrario
        """
        if jugador != self.__turno__:
            return False
        try:
            if len(self.__dados__.valores_dados()) == 0:
                return False
        except AttributeError:
            return False
        return True
    def mover_ficha(self, jugador: Jugador, posicion_inicial, posicion_final, valor_dado):
        """
        Mueve una ficha del jugador de una posición a otra usando un valor de dado específico.
        Valida que el movimiento sea legal y que el dado esté disponible.
        Argumentos:
            jugador: Objeto Jugador que realiza el movimiento
            posicion_inicial: Posición de origen (0-23)
            posicion_final: Posición de destino (0-23)
            valor_dado: Valor del dado a usar para el movimiento
        Returns:
            True si el movimiento fue exitoso, False en caso contrario
        Levanta:
            NoEsTuTurno: Si no es el turno del jugador
            SinDados: Si no hay dados disponibles
        """
        if jugador != self.__turno__:
            raise NoEsTuTurno(f"No es el turno de {jugador.nombre}")
        if not self.puede_mover(jugador):
            return False
        if valor_dado not in self.__dados__.valores_dados():
            raise SinDados(f"El dado {valor_dado} no está disponible")
        if self.__tablero__.movimiento_valido(posicion_inicial, posicion_final, jugador):
            if self.__tablero__.mover_checker(posicion_inicial, posicion_final, jugador.color):
                self.__dados__.usar_valor(valor_dado)
                return True
        return False
    def usar_dados(self, valor):
        """
        Marca un valor de dado como usado, eliminándolo de los dados disponibles.
        Argumentos:
            valor: Valor del dado a marcar como usado (1-6)
        Returns:
            True si el dado fue usado exitosamente, False si el valor no estaba disponible
        """
        if valor in self.__dados__.valores_dados():
            self.__dados__.usar_valor(valor)
            return True
        return False
    def estado_juego(self):
        """
        Retorna el estado completo del juego actual.
        Incluye el tablero, el turno, los dados disponibles y las fichas en el almacén.
        Returns:
            Diccionario con las claves: tablero, turno, dados, almacen_fichas
        """
        try:
            dados_actuales = self.__dados__.valores_dados()
        except AttributeError:
            dados_actuales = []
        return {
            "tablero" : self.__tablero__.estado_tablero(),
            "turno" : self.__turno__.nombre,
            "dados" : dados_actuales,
            "almacen_fichas" : self.__tablero__.__almacen_ficha__
        }
    def hay_fichas_en_almacen(self, jugador: Jugador):
        """
        Verifica si el jugador tiene fichas capturadas en el almacén (barra).
        Argumentos:
            jugador: Objeto Jugador a verificar
        Returns:
            True si tiene fichas en el almacén, False en caso contrario
        """
        return self.__tablero__.__almacen_ficha__[jugador.color] > 0
    def reingresar_ficha(self, jugador: Jugador, valor_dado):
        """
        Reingresa una ficha capturada desde el almacén al tablero usando un valor de dado.
        La ficha entra en la zona de casa del oponente según el valor del dado.
        Blancas entran en posiciones 0-5, negras en posiciones 18-23.
        Argumentos:
            jugador: Objeto Jugador que reingresa la ficha
            valor_dado: Valor del dado para determinar la posición de entrada
        Returns:
            True si el reingreso fue exitoso, False en caso contrario
        """
        if not self.puede_mover(jugador) or not self.hay_fichas_en_almacen(jugador):
            return False
        if valor_dado not in self.__dados__.valores_dados():
            return False

        pos_final = (valor_dado - 1) if jugador.color == "blanco" else (24 - valor_dado)

        if self.__tablero__.sacar_checker_comida(jugador.color, pos_final):
            self.__dados__.usar_valor(valor_dado)
            return True
        return False
    def realizar_bear_off(self, jugador: Jugador, posicion, valor_dado):
        """Intenta sacar una ficha del tablero (bear off)."""
        if not self.puede_mover(jugador) or not self.__tablero__.bear_off_permitido(jugador.color):
            return False
        if valor_dado not in self.__dados__.valores_dados():
            return False
        distancia_para_salir = (24 - posicion) if jugador.color == "blanco" else (posicion + 1)
        if valor_dado == distancia_para_salir:
            if self.__tablero__.bear_off(posicion, jugador.color):
                self.__dados__.usar_valor(valor_dado)
                return True
        elif valor_dado > distancia_para_salir:
            hay_fichas_mas_atras = False
            if jugador.color == "blanco":
                for i in range(18, posicion):
                    tablero_i = self.__tablero__.estado_tablero()[i]
                    if tablero_i and tablero_i[0] == jugador.color:
                        hay_fichas_mas_atras = True
                        break
            else:
                for i in range(posicion + 1, 6):
                    tablero_i = self.__tablero__.estado_tablero()[i]
                    if tablero_i and tablero_i[0] == jugador.color:
                        hay_fichas_mas_atras = True
                        break
            if not hay_fichas_mas_atras:
                if self.__tablero__.bear_off(posicion, jugador.color):
                    self.__dados__.usar_valor(valor_dado)
                    return True
        return False
    def verificar_ganador(self):
        """
        Verifica si algún jugador ha ganado la partida.
        Un jugador gana cuando todas sus fichas están fuera del tablero.
        Returns:
            Nombre del jugador ganador o None si no hay ganador aún
        """
        if self.__tablero__.verificar_ganador(self.__jugador1__.color):
            return self.__jugador1__.nombre
        if self.__tablero__.verificar_ganador(self.__jugador2__.color):
            return self.__jugador2__.nombre
        return None


