import unittest
from core.board import tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tab = tablero()
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

if __name__ == "__main__":
    unittest.main()