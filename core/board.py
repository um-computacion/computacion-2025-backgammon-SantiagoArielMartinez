"""
Módulo que define la clase Tablero para el juego de Backgammon.
"""
from core.player import Jugador
from core.exceptions import PosicionInvalida, PosicionVacia


class Tablero:
    """
    Clase que representa el tablero de Backgammon.
    Maneja las 24 posiciones del juego, el almacén de fichas capturadas,
    y todas las operaciones relacionadas con el movimiento de fichas.
    """
    def __init__(self):
        """
        Inicializa un tablero vacío con 24 posiciones y el almacén de fichas.
        El tablero comienza sin fichas, deben colocarse con tablero_inicial().
        """
        self.__contenedor__ = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[],
                              ]
        self.__almacen_ficha__ = {"blanco": 0, "negro": 0}
        self.__banco__ = {"blanco": 0, "negro": 0}
    def tablero_inicial(self):
        """
        Configura el tablero con la disposición inicial del juego de Backgammon.
        Coloca las fichas en sus posiciones de inicio según las reglas estándar.
        Returns:
            Lista con el estado inicial del tablero (24 posiciones)
        """
        self.__contenedor__[0] = ["blanco"] * 2
        self.__contenedor__[11] = ["blanco"] * 5
        self.__contenedor__[17] = ["blanco"] * 5
        self.__contenedor__[19] = ["blanco"] * 3
        self.__contenedor__[23] = ["negro"] * 5
        self.__contenedor__[12] = ["negro"] * 2
        self.__contenedor__[7] = ["negro"] * 3
        self.__contenedor__[5] = ["negro"] * 5
        return self.__contenedor__
    def estado_tablero(self):
        """Retorna el estado actual del tablero."""
        return self.__contenedor__
    def movimiento_valido(self, posicion_inicial, posicion_final, jugador : Jugador):
        """
        Verifica si un movimiento de ficha es válido según las reglas del Backgammon.
        Valida que las posiciones estén en rango, que haya fichas del jugador,
        y que el destino esté disponible o permita captura.
        Argumentos:
            posicion_inicial: Posición de origen (0-23)
            posicion_final: Posición de destino (0-23)
            jugador: Objeto Jugador que intenta mover
        Returns:
            True si el movimiento es válido, False en caso contrario
        """
        if self.__almacen_ficha__[jugador.color] > 0:
            return False
        if not 0 <= posicion_inicial < len(self.__contenedor__):
            return False
        if not 0 <= posicion_final < len(self.__contenedor__):
            return False
        inicio = self.__contenedor__[posicion_inicial]
        fin = self.__contenedor__[posicion_final]
        if not inicio:
            return False
        if not fin:
            return True
        if fin[0] == jugador.color:
            return True
        if len(fin) == 1 and fin[0] != jugador.color:
            return True
        return False
    def mover_checker(self,posicion_inicial, posicion_final, color ):
        """
        Mueve una ficha de una posición a otra en el tablero.
        Verifica que la ficha pertenezca al jugador correcto antes de moverla.
        Argumentos:
            posicion_inicial: Posición de origen (0-23)
            posicion_final: Posición de destino (0-23)
            color: Color de la ficha a mover ("blanco" o "negro")
        Returns:
            Color de la ficha movida o None si el movimiento falló
        """
        try:
            posicion_inicial_vacia = not self.__contenedor__[posicion_inicial]
            color_diferente = self.__contenedor__[posicion_inicial][-1] != color
            if posicion_inicial_vacia or color_diferente:
                return None
            destino = self.__contenedor__[posicion_final]
            if destino and len(destino) == 1 and destino[0] != color:
                enemigo_capturado = destino.pop()
                self.agregar_a_almacen(enemigo_capturado, 1)
            checker_a_mover = self.__contenedor__[posicion_inicial].pop()
            self.__contenedor__[posicion_final].append(checker_a_mover)
            return checker_a_mover
        except (ValueError, IndexError) as e:
            print(f"Error al mover checker: {e}")
            return None
    def agregar_a_almacen(self, color, cantidad):
        """Agrega una o más fichas a la barra (almacén)."""
        if color in self.__almacen_ficha__:
            self.__almacen_ficha__[color] += cantidad
    def sacar_checker(self, posicion):
        """
        Retira una ficha de una posición específica del tablero.
        Argumentos:
            posicion: Posición del tablero (0-23)
        Returns:
            Color de la ficha retirada o None si la posición está vacía
        """
        if not 0 <= posicion < 24:
            raise PosicionInvalida(f"La posición {posicion} no existe. Debe ser entre 0 y 23")
        if not self.__contenedor__[posicion]:
            raise PosicionVacia(f"No hay fichas en la posición {posicion}")
        return self.__contenedor__[posicion].pop()
    def estado_almacenamiento(self):
        """Retorna el estado de la barra de fichas capturadas."""
        return self.__almacen_ficha__
    def sacar_checker_comida(self, color, posicion_final):
        """
        Reingresa una ficha capturada desde el almacén a una posición del tablero.
        Solo funciona si el jugador tiene fichas en el almacén.
        Argumentos:
            color: Color de la ficha a reingresar
            posicion_final: Posición de destino en el tablero
        Returns:
            True si el reingreso fue exitoso, False en caso contrario
        """
        if not 0 <= posicion_final < 24:
            return False
        if self.__almacen_ficha__.get(color, 0) == 0:
            return False
        destino = self.__contenedor__[posicion_final]
        if destino and destino[0] != color and len(destino) >= 2:
            return False
        if destino and destino[0] != color and len(destino) == 1:
            enemigo_capturado = destino.pop()
            self.agregar_a_almacen(enemigo_capturado, 1)
        self.__contenedor__[posicion_final].append(color)
        self.__almacen_ficha__[color] -= 1
        return True
    def verificar_ganador(self,color):
        """
        Verifica si un jugador ha ganado sacando todas sus fichas del tablero.
        Argumentos:
            color: Color del jugador a verificar
        Returns:
            True si el jugador ha ganado, False en caso contrario
        """
        fichas_en_banco = self.__banco__.get(color, 0)
        return fichas_en_banco == 15
    def bear_off_permitido(self, color):
        """
        Verifica si un jugador puede comenzar a sacar fichas del tablero (bear off).
        Solo se permite cuando todas las fichas están en la zona de casa.
        Argumentos:
            color: Color del jugador a verificar
        Returns:
            True si puede hacer bear off, False en caso contrario
        """
        if color == "blanco":
            rango = range(18, 24)
        else:
            rango = range(0, 6)
        for i in range(24):
            if i not in rango and self.__contenedor__[i]:
                if self.__contenedor__[i][0] == color:
                    return False
        return True
    def bear_off(self, posicion, color):
        """
        Saca una ficha del tablero definitivamente (bear off).
        Solo se permite si el jugador tiene todas sus fichas en la zona de casa.
        Argumentos:
            posicion: Posición desde donde sacar la ficha
            color: Color del jugador que saca la ficha
        Returns:
            True si se sacó la ficha exitosamente, False en caso contrario
        """
        if not self.bear_off_permitido(color):
            return False
        if self.__contenedor__[posicion]:
            if self.__contenedor__[posicion][-1] == color:
                self.__contenedor__[posicion].pop()
                self.__banco__[color] += 1
                return True
            return False
        return False
