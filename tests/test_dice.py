import unittest
from core.dice import Dados
from unittest.mock import patch
class TestDados(unittest.TestCase):

    def test_tirar_dado1(self):
        dado1 = Dados()
        dado1.tirar_dado()
        self.assertIn(dado1.get_valor1(), [1, 2, 3, 4, 5, 6])

    def test_tirar_dado2(self):
        dado2 = Dados()
        dado2.tirar_dado()
        self.assertIn(dado2.get_valor2(), [1, 2, 3, 4, 5, 6])

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
        self.assertEqual(len(prueba), 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 1)

if __name__ == "__main__":
    unittest.main()