import unittest
from core.backgammongame import BackgammonGame
class TestBackgammonGame(unittest.TestCase):

    def test_constructor(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertEqual(juego.get_jugador1().nombre,"Santiago")
        self.assertEqual(juego.get_jugador2().nombre, "Vanina")
        self.assertEqual(juego.get_jugador1().color, "Negras")
        self.assertEqual(juego.get_jugador2().color, "blancas")
    
    def test_dados(self):
        juego = BackgammonGame("Santiago","Vanina")
        dados = juego.get_dados()
        self.assertIn(dados.tirar_dado()[0], [1,2,3,4,5,6])
        self.assertIn(dados.tirar_dado()[1], [1,2,3,4,5,6])