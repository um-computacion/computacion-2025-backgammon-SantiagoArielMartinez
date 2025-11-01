import unittest
from core.dice import Dados
from unittest.mock import patch

class TestDados(unittest.TestCase):

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_tirar_dado_valores_mockados(self, mock_randint):
        """Test que tirar_dado retorna los valores correctos"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [4, 2])

    def test_tirar_dado_valores_en_rango(self):
        """Test que los valores de los dados están en rango 1-6"""
        dado = Dados()
        dado.tirar_dado()
        for valor in dado.valores_dados():
            self.assertIn(valor, [1, 2, 3, 4, 5, 6])

    @patch("core.dice.random.randint", side_effect=[3, 3])
    def test_tirar_dado_dobles_genera_cuatro_valores(self, mock_randint):
        """Test que dados dobles generan 4 valores iguales"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [3, 3, 3, 3])

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_valor_elimina_y_reduce(self, mock_randint):
        """Test que usar_valor elimina el valor y mantiene otros"""
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(4)
        self.assertNotIn(4, dado.valores_dados())
        self.assertIn(2, dado.valores_dados())
        self.assertEqual(len(dado.valores_dados()), 1)

    @patch("core.dice.random.randint", side_effect=[4, 2, 5, 6])
    def test_resetear_dados_permite_nuevo_tiro(self, mock_randint):
        """Test que resetear permite tirar dados nuevamente"""
        dado = Dados()
        dado.tirar_dado()
        dado.resetear_dados()
        self.assertEqual(len(dado.valores_dados()), 0)
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 2)

    @patch("core.dice.random.randint", side_effect=[4, 4])
    def test_usar_valor_multiple_veces_en_dobles(self, mock_randint):
        """Test usar el mismo valor múltiples veces en dados dobles"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 4)
        dado.usar_valor(4)
        dado.usar_valor(4)
        dado.usar_valor(4)
        self.assertEqual(len(dado.valores_dados()), 1)

    def test_usar_valor_no_existente_retorna_false(self):
        """Test que usar un valor inexistente no modifica la lista"""
        dado = Dados()
        dado.tirar_dado()
        valores_antes = len(dado.valores_dados())
        resultado = dado.usar_valor(7)
        self.assertFalse(resultado)
        self.assertEqual(len(dado.valores_dados()), valores_antes)

    @patch("core.dice.random.randint", side_effect=ValueError("Error simulado"))
    def test_tirar_dado_con_excepcion(self, mock_randint):
        """Test que tirar_dado maneja excepciones correctamente"""
        dado = Dados()
        resultado = dado.tirar_dado()
        self.assertEqual(resultado, ())

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_quedan_valores_true(self, mock_randint):
        """Test quedan_valores retorna True cuando hay valores"""
        dado = Dados()
        dado.tirar_dado()
        self.assertTrue(dado.quedan_valores())

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_quedan_valores_false_despues_de_usar_todos(self, mock_randint):
        """Test quedan_valores retorna False cuando no hay valores"""
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(5)
        dado.usar_valor(3)
        self.assertFalse(dado.quedan_valores())

if __name__ == '__main__':
    unittest.main()