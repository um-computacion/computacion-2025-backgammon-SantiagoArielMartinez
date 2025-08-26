import unittest
from core.dice import dados

class TestDados(unittest.TestCase):

    def test_tirar_dado(self):
        dado1 = dados()
        dado1.tirar_dado()
        self.assertIn(dado1.get_valor1(), [1, 2, 3, 4, 5, 6])
