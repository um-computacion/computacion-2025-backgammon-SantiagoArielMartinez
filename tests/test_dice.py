import unittest
from core.dice import Dados
from unittest.mock import patch
class TestDados(unittest.TestCase):

    @patch("core.dice.random.randint", side_effect = [5,2])
    def test_dados(self, mock_ranint):
        dado = Dados()
        resultado = dado.tirar_dado()
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0],5)
        self.assertEqual(resultado[1],2)

    @patch("core.dice.random.randint", side_effect = Exception("Error!!")) 
    def test_dados_exception(self, randint_patched):
        dado = Dados()
        prueba = dado.tirar_dado()
        self.assertEqual(len(prueba), 0)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 1)
    
    def valores_disponibles(self):
        dado = Dados()
        dado.__valores__ = [3,4]
        self.assertListEqual(dado.valores_dados(), [3,4])

    def test_usar_valor(self):
        dado = Dados()
        dado.__valores__ = [2,5]
        self.assertTrue(dado.usar_valor(2))
        self.assertListEqual(dado.__valores__, [5])
        self.assertFalse(dado.usar_valor(6))
        self.assertListEqual(dado.__valores__, [5])

    def test_quedan_valores(self):
        dado = Dados()
        dado.__valores__ = [1]
        self.assertTrue(dado.quedan_valores())
        dado.__valores__.clear()
        self.assertFalse(dado.quedan_valores())

    def test_resetear_dados(self):
        dado = Dados()
        dado.__valores__ = [1,2,3]
        dado.resetear_dados()
        self.assertListEqual(dado.__valores__, [])
if __name__ == "__main__":
    unittest.main()