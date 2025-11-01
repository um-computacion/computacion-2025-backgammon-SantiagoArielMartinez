import unittest
from core.player import Jugador

class TestJugador(unittest.TestCase):

    def test_constructor_nombre(self):
        jugador = Jugador("Santiago", "blanco")
        self.assertEqual(jugador.nombre, "Santiago")

    def test_constructor_color(self):
        jugador = Jugador("Santiago", "blanco")
        self.assertEqual(jugador.color, "blanco")

    def test_jugador_nombre_diferente(self):
        jugador = Jugador("Vanina", "negro")
        self.assertEqual(jugador.nombre, "Vanina")

    def test_jugador_color_negro(self):
        jugador = Jugador("Vanina", "negro")
        self.assertEqual(jugador.color, "negro")

    def test_dos_jugadores_diferentes(self):
        jugador1 = Jugador("Santiago", "blanco")
        jugador2 = Jugador("Vanina", "negro")
        self.assertNotEqual(jugador1.nombre, jugador2.nombre)
        self.assertNotEqual(jugador1.color, jugador2.color)

    def test_jugador_blanco_nombre_correcto(self):
        jugador = Jugador("Carlos", "blanco")
        self.assertEqual(jugador.nombre, "Carlos")

    def test_jugador_negro_color_correcto(self):
        jugador = Jugador("Maria", "negro")
        self.assertEqual(jugador.color, "negro")

    def test_jugador_get_nombre(self):
        jugador = Jugador("Pedro", "blanco")
        self.assertEqual(jugador.nombre, "Pedro")

    def test_jugador_get_color(self):
        jugador = Jugador("Ana", "negro")
        self.assertEqual(jugador.color, "negro")

    def test_jugador_eq_mismo(self):
        jugador1 = Jugador("Test", "blanco")
        jugador2 = Jugador("Test", "blanco")
        self.assertTrue(jugador1.nombre == jugador2.nombre)

    def test_jugador_setter_nombre_invalido_no_string(self):
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = 123

    def test_jugador_setter_nombre_vacio(self):
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = ""

    def test_jugador_setter_nombre_solo_espacios(self):
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = "   "

    def test_jugador_setter_color_valido(self):
        jugador = Jugador("Test", "blanco")
        jugador.color = "negro"
        self.assertEqual(jugador.color, "negro")

    def test_jugador_setter_color_cambio(self):
        jugador = Jugador("Test", "negro")
        jugador.color = "blanco"
        self.assertEqual(jugador.color, "blanco")

if __name__ == '__main__':
    unittest.main()
