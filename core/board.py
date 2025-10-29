from core.player import Jugador

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
        #Inicializar un tablero con 24 posiciones vacias
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
        #El tablero de 24 posiciones con las fichas en su lugar de origen
        self.__contenedor__[0] = ["blanco"] * 2
        self.__contenedor__[5] = ["negro"] * 5
        self.__contenedor__[7] = ["negro"] * 3
        self.__contenedor__[11] = ["blanco"] * 5
        self.__contenedor__[12] = ["negro"] * 2
        self.__contenedor__[17] = ["blanco"] * 5
        self.__contenedor__[19] = ["blanco"] * 3
        self.__contenedor__[23] = ["negro"] * 5
        return self.__contenedor__

    def estado_tablero(self):
        """
        Retorna el estado actual del tablero con todas las fichas en sus posiciones.
        Returns:
            Lista de 24 posiciones, cada una con una lista de fichas
        """
        #obtenes el estado del tablero actual
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
        elif not (0 <= posicion_inicial < len(self.__contenedor__)):
            return False
        elif not (0 <= posicion_final < len(self.__contenedor__)):
            return False 
        inicio = self.__contenedor__[posicion_inicial]
        fin = self.__contenedor__[posicion_final]
        if not inicio:
            return False
        elif not fin:
            return True
        elif fin[0] == jugador.color:
            return True
        elif len(fin) == 1 and fin[0] != jugador.color:
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
            #Verificar que la ficha pertenezca al jugador
            if self.__contenedor__[posicion_inicial][-1] != color:
                return None
            #Verificar que las posiciones estén en rango valido
            if 0 <= posicion_inicial < 24 and 0 <= posicion_final < 24:
                #verificar que hay fichas en la posicion inicial
                if self.__contenedor__[posicion_inicial]:
                    #mover la ficha
                    checker = self.__contenedor__[posicion_inicial].pop()
                    self.__contenedor__[posicion_final].append(checker)
                    return checker
        except (ValueError, IndexError) as e:
            print(f"Error al mover checker: {e}")
            return None

    def sacar_checker(self, posicion):
        """
        Retira una ficha de una posición específica del tablero.
        Argumentos:
            posicion: Posición del tablero (0-23)
        Returns:
            Color de la ficha retirada o None si la posición está vacía
        """
        #Retira una ficha de una posicion especifica 
        if self.__contenedor__[posicion]:
            return self.__contenedor__[posicion].pop()
        return None

    def estado_almacenamiento(self):
        """
        Retorna el estado del almacén de fichas capturadas.
        Returns:
            Diccionario con las fichas capturadas por color
        """
        return self.__almacen_ficha__
    
    def comer_checker(self, posicion_final, color):
        """
        Captura una ficha enemiga que está sola en una posición (blot).
        La ficha capturada se envía al almacén y debe reingresar antes de mover otras fichas.
        Argumentos:
            posicion_final: Posición donde se realiza la captura
            color: Color del jugador que captura
        Returns:
            True si se capturó una ficha, False en caso contrario
        """
        if not self.__contenedor__[posicion_final]:
            return False
        elif len(self.__contenedor__[posicion_final]) == 1 and self.__contenedor__[posicion_final][0] != color:
            enemigo = self.__contenedor__[posicion_final].pop()
            self.__contenedor__[posicion_final] = [color]
            self.__almacen_ficha__[enemigo] += 1
            return True
        elif len(self.__contenedor__[posicion_final]) >= 2:
            return False
        return False

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
        if self.__almacen_ficha__[color] <= 0:
            return False
        if not (0 <= posicion_final < len(self.__contenedor__)):
            return False
        # Verificar si hay 2 o más fichas enemigas en la posición
        if len(self.__contenedor__[posicion_final]) >= 2:
            if self.__contenedor__[posicion_final][0] != color:
                return False
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
        if color not in self.__almacen_ficha__:
            return False
        elif self.__almacen_ficha__[color] > 0:
            return False
        elif self.__contenedor__ == [[] for _ in range(24)]:
            if self.__banco__[color] == 15:
                return True
        
        return False
    
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
        elif self.__contenedor__[posicion]:
            if self.__contenedor__[posicion][-1] == color:
                self.__contenedor__[posicion].pop()
                self.__banco__[color] += 1
                return True
