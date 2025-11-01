import unittest
from core.dice import Dados
from unittest.mock import patch

class TestDados(unittest.TestCase):

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_tirar_dado_valores_mockados(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [4, 2])
    @patch("core.dice.random.randint", side_effect=[3, 1])
    def test_tirar_dado_genera_dos_valores(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 2)

    def test_tirar_dado_valor1_en_rango(self):
        dado = Dados()
        dado.tirar_dado()
        self.assertIn(dado.valores_dados()[0], [1, 2, 3, 4, 5, 6])

    def test_tirar_dado_valor2_en_rango(self):
        dado = Dados()
        dado.tirar_dado()
        self.assertIn(dado.valores_dados()[1], [1, 2, 3, 4, 5, 6])

    @patch("core.dice.random.randint", side_effect=[3, 3])
    def test_tirar_dado_dobles_genera_cuatro_valores(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 4)

    @patch("core.dice.random.randint", side_effect=[3, 3])
    def test_tirar_dado_dobles_todos_iguales(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [3, 3, 3, 3])

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_valor_elimina_dado(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(4)
        self.assertNotIn(4, dado.valores_dados())

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_valor_reduce_cantidad(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(4)
        self.assertEqual(len(dado.valores_dados()), 1)

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_valor_mantiene_otros_dados(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(4)
        self.assertIn(2, dado.valores_dados())

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_resetear_dados_vacia_lista(self, mock_randint):
        dado = Dados()
        dado.tirar_dado()
        dado.resetear_dados()
        self.assertEqual(len(dado.valores_dados()), 0)
    @patch("core.dice.random.randint", side_effect=[4, 2, 5, 6])
    def test_resetear_dados_permite_nuevo_tiro(self,mock_randint):
        dado = Dados()
        dado.tirar_dado()
        dado.resetear_dados()
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 2)

    @patch("core.dice.random.randint", side_effect=[6, 6])
    def test_usar_valor_en_dobles(self, mock_randint):
        """Test usar valor cuando hay dados dobles"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(len(dado.valores_dados()), 4)
        dado.usar_valor(6)
        self.assertEqual(len(dado.valores_dados()), 3)

    def test_usar_valor_no_existente_no_modifica_lista(self):
        """Test que usar un valor inexistente no modifica la lista"""
        dado = Dados()
        dado.tirar_dado()
        valores_antes = dado.valores_dados().copy()
        dado.usar_valor(7)
        self.assertEqual(len(dado.valores_dados()), len(valores_antes))

    @patch("core.dice.random.randint", side_effect=[1, 1])
    def test_tirar_dado_dobles_uno(self, mock_randint):
        """Test dados dobles con valor 1"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [1, 1, 1, 1])

    @patch("core.dice.random.randint", side_effect=[6, 6])
    def test_tirar_dado_dobles_seis(self, mock_randint):
        """Test dados dobles con valor 6"""
        dado = Dados()
        dado.tirar_dado()
        self.assertEqual(dado.valores_dados(), [6, 6, 6, 6])

    def test_valores_dados_antes_de_tirar(self):
        """Test valores_dados cuando no se han tirado dados"""
        dado = Dados()
        try:
            valores = dado.valores_dados()
            self.assertIsInstance(valores, list)
        except AttributeError:
            pass

    @patch("core.dice.random.randint", side_effect=[2, 5])
    def test_usar_todos_los_valores(self, mock_randint):
        """Test usar todos los valores de los dados"""
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(2)
        dado.usar_valor(5)
        self.assertEqual(len(dado.valores_dados()), 0)

    @patch("core.dice.random.randint", side_effect=[4, 4])
    def test_usar_valor_multiple_veces_en_dobles(self, mock_randint):
        """Test usar el mismo valor múltiples veces en dados dobles"""
        dado = Dados()
        dado.tirar_dado()
        dado.usar_valor(4)
        dado.usar_valor(4)
        dado.usar_valor(4)
        self.assertEqual(len(dado.valores_dados()), 1)
        self.assertEqual(dado.valores_dados()[0], 4)

    @patch("core.dice.random.randint", side_effect=Exception("Error simulado"))
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