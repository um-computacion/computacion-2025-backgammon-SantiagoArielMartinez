import unittest
from core.backgammongame import Backgammon_game

class TestBackgammonGame(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon_game()

    def test_crear_jugador(self):
        jugador = self.game.crear_jugador("chola", "Blanco")
        self.assertEqual(jugador.__nombre__, "chola")
        self.assertEqual(jugador.__color__, "Blanco")

if __name__ == "__main__":
    unittest.main()