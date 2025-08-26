import unittest
from core.backgammongame import backgammon_game

class TestBackgammonGame(unittest.TestCase):
    def setUp(self):
        self.game = backgammon_game()

    def test_crear_jugador(self):
        jugador = self.game.crear_jugador("chola", "Blanco")
        self.assertEqual(jugador.__nombre__, "chola")
        self.assertEqual(jugador.__color__, "Blanco")
