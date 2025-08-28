import unittest
from core.player import Jugador

class Testjugador(unittest.TestCase):
    
    def test_creacion_jugador(self):
        
        jugador1 = Jugador("Jugador1", "Blanco")
        self.assertEqual(jugador1.jugador, "Jugador1")
        self.assertEqual(jugador1.color, "Blanco")

    def test_setters(self):
        s = Jugador("jugador1", "Blanco")
        s.jugador = "Santiago"
        s.color = "Blanco"
        self.assertEqual(s.jugador, "Santiago")
        self.assertEqual(s.color, "Blanco")
        
if __name__ == "__main__":
    unittest.main()
    