import unittest
from core.board import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tab = Tablero()
    def test_cantidad_casilleros(self):
        self.assertEqual(len(self.tab.__contenedor__), 24)

    def test_tablero_blanco(self):
        self.assertListEqual(self.tab.__contenedor__[0], ["blanco", "blanco"])
        self.assertListEqual(self.tab.__contenedor__[11], ["blanco", "blanco", "blanco", "blanco", "blanco"])
        self.assertListEqual(self.tab.__contenedor__[17], ["blanco", "blanco", "blanco", "blanco", "blanco"])
        self.assertListEqual(self.tab.__contenedor__[19], ["blanco", "blanco", "blanco"])


    def test_tablero_negros(self):
        self.assertListEqual(self.tab.__contenedor__[5], ["negro", "negro", "negro", "negro", "negro"])
        self.assertListEqual(self.tab.__contenedor__[7], ["negro", "negro", "negro"])
        self.assertListEqual(self.tab.__contenedor__[12], ["negro", "negro"])
        self.assertListEqual(self.tab.__contenedor__[23], ["negro", "negro", "negro", "negro", "negro"])

    def test_mostrar_tablero(self):
        self.assertEqual(self.tab.mostrar_contenedor(), self.tab.__contenedor__)

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
    
    def test_almacenar_fichas(self):
        self.assertEqual(self.tab.almacenamiento(1,0), "blanco: 1, negro: 0" )
        self.assertEqual(self.tab.almacenamiento(0,0), "blanco: 0, negro: 0" )
        self.assertEqual(self.tab.almacenamiento(0,2), "blanco: 0, negro: 2" )
        self.assertEqual(self.tab.almacenamiento(4,4), "blanco: 4, negro: 4" )

if __name__ == "__main__":
    unittest.main()