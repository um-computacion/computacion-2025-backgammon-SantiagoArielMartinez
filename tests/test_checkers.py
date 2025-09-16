from core.checkers import Ficha
import unittest

class TestFicha(unittest.TestCase):
  
    def test_obtener_ficha(self):
       ficha = Ficha("blanca", 6)
       self.assertEqual(ficha.get_ficha(),"blanca")
  
    def test_obtener_movimiento(self):
       ficha = Ficha("Negra", 3)
       self.assertEqual(ficha.get_movimiento(),3)

    def test_adentro_almacen(self):
         ficha = Ficha("Negra", -1)
         self.assertTrue(ficha.adentro_almacen())
         ficha2 = Ficha("Blanca", 5)
         self.assertFalse(ficha2.adentro_almacen())

    def test_str(self):
        ficha = Ficha("Negra", 3)
        self.assertEqual(ficha.__str__(), "Negra en 3")