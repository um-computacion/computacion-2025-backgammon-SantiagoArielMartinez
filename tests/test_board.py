import unittest
from core.board import Tablero
from core.player import Jugador
class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tab = Tablero()

        self.tablero = self.tab.tablero_inicial()

    def test_cantidad_casilleros(self):
        self.assertEqual(len(self.tablero), 24)

    def test_tablero_blanco(self):
        self.assertListEqual(self.tablero[0], ["blanco", "blanco"])
        self.assertListEqual(self.tablero[11], ["blanco", "blanco", "blanco", "blanco", "blanco"])
        self.assertListEqual(self.tablero[17], ["blanco", "blanco", "blanco", "blanco", "blanco"])
        self.assertListEqual(self.tablero[19], ["blanco", "blanco", "blanco"])


    def test_tablero_negros(self):
        self.assertListEqual(self.tablero[23], ["negro", "negro", "negro", "negro", "negro"])
        self.assertListEqual(self.tablero[7], ["negro", "negro", "negro"])
        self.assertListEqual(self.tablero[12], ["negro", "negro"])
        self.assertListEqual(self.tablero[5], ["negro", "negro", "negro", "negro", "negro"])

    def test_mostrar_tablero(self):
        self.assertEqual(self.tab.estado_tablero(), self.tab.__contenedor__)

    def test_sacar_checker(self):
        self.assertEqual(self.tab.sacar_checker(0), "blanco")
        self.assertEqual(self.tab.sacar_checker(5), "negro")
        self.assertEqual(self.tab.sacar_checker(11), "blanco")
        self.assertEqual(self.tab.sacar_checker(17), "blanco")
        self.assertEqual(self.tab.sacar_checker(19), "blanco")
        self.assertEqual(self.tab.sacar_checker(23), "negro")

    def test_mover_checker(self):
        self.assertEqual(self.tab.mover_checker(0,3), "blanco")
        self.assertEqual(self.tab.mover_checker(5,7), "negro")
        self.assertEqual(self.tab.mover_checker(11,12), "blanco")
        self.assertEqual(self.tab.mover_checker(17,19), "blanco")
        self.assertEqual(self.tab.mover_checker(19,23), "blanco")
    
    def test_validar_movimiento(self):
        jugador_blanco = Jugador("Santi","blanco")
        jugador_negro = Jugador("Gonzalo","negro")
        self.assertEqual(self.tab.movimiento_valido(0,1, jugador_blanco),True)
        self.assertEqual(self.tab.movimiento_valido(0,2, jugador_blanco), True)
        self.assertEqual(self.tab.movimiento_valido(0,5, jugador_negro), True)

    def test_movimiento_posicion_fuera_rango(self):
        jugador = Jugador("Sanchi", "blanco")

        resultado = self.tab.movimiento_valido(-1, 5 , jugador)
        self.assertFalse(resultado)

        resultado = self.tab.movimiento_valido(0,26, jugador)
        self.assertFalse(resultado)

        resultado = self.tab.movimiento_valido(55, 5 , jugador)
        self.assertFalse(resultado)

    def test_sacar_checker_posicion_vacia(self):
        resultado = self.tab.sacar_checker(1)
        self.assertIsNone(resultado)

        resultado = self.tab.sacar_checker(3)
        self.assertIsNone(resultado)
    
    def test_mover_checker_especial(self):
        resultado = self.tab.mover_checker(-1,5)
        self.assertIsNone(resultado)

        resultado = self.tab.mover_checker(1,2)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()