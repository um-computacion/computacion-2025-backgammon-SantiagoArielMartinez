from core.checkers import Ficha
import unittest

class TestFicha(unittest.TestCase):
  
   def test_obtener_ficha(self):
       ficha = Ficha("blanca", 6)
       self.assertEqual(ficha.get_ficha(),"blanca")
  
   def test_obtener_movimiento(self):
       ficha = Ficha("Negra", 3)
       self.assertEqual(ficha.get_movimiento(),3)
