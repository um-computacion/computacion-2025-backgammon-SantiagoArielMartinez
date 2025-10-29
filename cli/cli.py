from core.backgammongame import BackgammonGame

class CLI:
    def __init__(self):
        print("=== BIENVENIDO AL BACKGAMMON ===")
        jugador1 = input("Nombre del Jugador 1 (Negras): ")
        jugador2 = input("Nombre del Jugador 2 (Blancas): ")
        self.__game__ = BackgammonGame(jugador1, jugador2)
        
    def mostrar_tablero(self):
        """Muestra el tablero de forma simple"""
        print("\n" + "="*80)
        tablero = self.__game__.get_tablero().estado_tablero()
        almacen = self.__game__.get_tablero().estado_almacenamiento()
        print(f"Fichas capturadas - Negras: {almacen['negro']}, Blancas: {almacen['blanco']}")
        print("-"*80)
        print("\nParte Superior (Puntos 12-23):")
        for i in range(23, 11, -1):
            fichas = tablero[i] if tablero[i] else []
            if fichas:
                color = fichas[0]
                cantidad = len(fichas)
                print(f"Punto {i}: {color} x{cantidad}")
            else:
                print(f"Punto {i:}: (vacío)")
                
        print("Parte Inferior (Puntos 0-11):")
      
        for i in range(12):
            fichas = tablero[i] if tablero[i] else []
            if fichas:
                color = fichas[0]
                cantidad = len(fichas)
                print(f"Punto {i}: {color} x{cantidad}")
            else:
                print(f"Punto {i}: (vacío)")
        
        print("="*80 + "\n")
    
    def mostrar_turno(self):
       """Muestra de quién es el turno"""
       print(f"\n>>> {self.__game__.obtener_turno()} <<<")
  
    def tirar_dados(self):
       """Tira los dados y muestra los resultados"""
       dados = self.__game__.tirar_dados()
       valores = dados.valores_dados()
       print(f"\n Dados: {valores[0]} y {valores[1]}")
       return valores

    def realizar_movimiento(self, jugador):
       """Permite al jugador mover una ficha"""
       try:
           print("\nIngrese el movimiento:")
           origen = int(input("  Posición origen (0-23): "))
           destino = int(input("  Posición destino (0-23): "))
           dado = int(input("  Valor del dado a usar: "))
          
           if self.__game__.mover_ficha(jugador, origen, destino, dado):
               print("Movimiento realizado con éxito")
               return True
           else:
               print("Movimiento inválido")
               return False
       except ValueError:
           print("Error: Ingrese solo números")
           return False
    

    def menu_turno(self, jugador):
       """Menú de opciones del turno"""
       while self.__game__.puede_mover(jugador):
           print("\n¿Qué desea hacer?")
           print("1. Mover ficha")
           print("2. Reingresar ficha (si tiene en el almacén)")
           print("3. Ver tablero")
           print("4. Finalizar turno")
          
           opcion = input("Opción: ")
          
           if opcion == "1":
               self.realizar_movimiento(jugador)
           elif opcion == "2":
               if self.__game__.hay_fichas_en_almacen(jugador):
                   dado = int(input("Valor del dado: "))
                   if self.__game__.reingresar_ficha(jugador, dado):
                       print("Ficha reingresada")
                   else:
                       print("No se pudo reingresar")
               else:
                   print("No tienes fichas en el almacén")
           elif opcion == "3":
               self.mostrar_tablero()
           elif opcion == "4":
               break
           else:
               print("Opción inválida")
  
    def main(self):
       """Bucle principal del juego"""
       print("\n¡Comienza el juego!")
       self.mostrar_tablero()
      
       while not self.__game__.verificar_ganador():
           self.mostrar_turno()
           jugador_actual = self.__game__.get_turno_actual()
          
           self.tirar_dados()
           self.menu_turno(jugador_actual)
          
           self.__game__.finalizar_turno()
      
       ganador = self.__game__.verificar_ganador()
       print(f"\n¡FELICIDADES {ganador}! HAS GANADO")


if __name__ == "__main__":
   juego = CLI()
   juego.main()