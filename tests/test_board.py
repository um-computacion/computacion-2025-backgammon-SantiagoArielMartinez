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
        self.assertEqual(self.tab.mover_checker(0,3,"blanco"), "blanco")
        self.assertEqual(self.tab.mover_checker(5,7,"negro"), "negro")
        self.assertEqual(self.tab.mover_checker(11,12,"blanco"), "blanco")
        self.assertEqual(self.tab.mover_checker(17,19,"blanco"), "blanco")
        self.assertEqual(self.tab.mover_checker(19,23,"blanco"), "blanco")
    
    def test_validar_movimiento(self):
        jugador_blanco = Jugador("Santi","blanco")
        jugador_negro = Jugador("Gonzalo","negro")
        self.assertEqual(self.tab.movimiento_valido(0,5, jugador_negro), True)
        self.assertFalse(self.tab.movimiento_valido(1,5 , jugador_blanco))
        self.assertTrue(self.tab.movimiento_valido(0,1,jugador_blanco))
        self.tab.__contenedor__[5] = ["negro"]
        self.tab.__contenedor__[1] = []
        resultado = self.tab.mover_checker(5,1, "negro")
        self.assertTrue(self.tab.movimiento_valido(0, 1, jugador_blanco))
    def test_movimiento_posicion_fuera_rango(self):
        jugador_blanco = Jugador("Sanchi","blanco")
        resultado = self.tab.movimiento_valido(-1, 5 , "blanco")
        self.assertFalse(resultado)
        resultado = self.tab.movimiento_valido(0,26, "blanco")
        self.assertFalse(resultado)
        resultado = self.tab.movimiento_valido(55, 5 , "blanco")
        self.assertFalse(resultado)

    def test_sacar_checker_posicion_vacia(self):
        resultado = self.tab.sacar_checker(1)
        self.assertIsNone(resultado)
        resultado = self.tab.sacar_checker(3)
        self.assertIsNone(resultado)
    
    def test_mover_checker_especial(self):
        resultado = self.tab.mover_checker(-1,5,"blanco")
        self.assertIsNone(resultado)
        resultado = self.tab.mover_checker(1,2,"negro")
        self.assertIsNone(resultado)
    
    def test_almacenar_ficha(self):
        resultado = self.tab.almacenamiento("blanco")
        self.assertEqual(resultado, {"blanco": 1, "negras": 0})
if __name__ == "__main__":
    unittest.main()