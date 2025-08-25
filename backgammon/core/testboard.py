import unittest
from board import tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tab = tablero()
        self.tab.tablero_inicial()
    
    def test_cantidad_de_puntos(self):
        self.assertEqual(len(self.tab.tablero_inicial.contenedor), 23)

    def test_tablero_blanco(self):
        self.assertEqual(self.tab.tablero_inicial.contenedor[0], ["blanco", "blanco"])
        self.assertEqual(self.tab.tablero_inicial.contenedor[11], ["blanco"] * 5)
        self.assertEqual(self.tab.tablero_inicial.contenedor[17], ["blanco"] * 5)
        self.assertEqual(self.tab.tablero_inicial.contenedor[19], ["blanco"] * 3) 


    def test_tablero_negros(self):
        self.assertEqual(self.tab.tablero_inicial.contenedor[5], ["negro"] * 5)
        self.assertEqual(self.tab.tablero_inicial.contenedor[7], ["negro"] * 3)
        self.assertEqual(self.tab.tablero_inicial.contenedor[12], ["negro"] * 2)
        self.assertEqual(self.tab.tablero_inicial.contenedor[23], ["negro"] * 5)
        
if __name__ == "__main__":
    unittest.main()