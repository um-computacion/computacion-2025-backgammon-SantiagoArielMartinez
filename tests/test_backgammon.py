import unittest
from core.backgammongame import BackgammonGame
class TestBackgammonGame(unittest.TestCase):

    def test_constructor(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertEqual(juego.get_jugador1().nombre,"Santiago")
        self.assertEqual(juego.get_jugador2().nombre, "Vanina")
        