from core.backgammongame import BackgammonGame

class CLI:
    def __init__(self):
        print("=== BIENVENIDO AL BACKGAMMON ===")
        jugador1 = input("Nombre del Jugador 1 (Negras): ")
        jugador2 = input("Nombre del Jugador 2 (Blancas): ")
        self.__game__ = BackgammonGame(jugador1, jugador2)
        
    def mostrar_tablero(self):
        """Muestra el tablero de forma simple"""
        print("\n" + "="*50)
        tablero = self.__game__.get_tablero().estado_tablero()
        almacen = self.__game__.get_tablero().estado_almacenamiento()
        
        print(f"Fichas capturadas - Negras: {almacen['negro']}, Blancas: {almacen['blanco']}")
        print("-"*50)
        
        for i, posicion in enumerate(tablero):
            if posicion:
                print(f"Posición {i}: {posicion}")
        print("="*50 + "\n")
    
    def mostrar_turno(self):
       """Muestra de quién es el turno"""
       print(f"\n>>> {self.__game__.obtener_turno()} <<<")
  
    def tirar_dados(self):
       """Tira los dados y muestra los resultados"""
       dados = self.__game__.tirar_dados()
       valores = dados.valores_dados()
       print(f"\n Dados: {valores[0]} y {valores[1]}")
       return valores
