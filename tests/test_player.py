import unittest
from core.player import Jugador

class TestJugador(unittest.TestCase):

    def test_constructor_nombre(self):
        """Test que el constructor inicializa correctamente el nombre"""
        jugador = Jugador("Santiago", "blanco")
        self.assertEqual(jugador.nombre, "Santiago")

    def test_constructor_color(self):
        """Test que el constructor inicializa correctamente el color"""
        jugador = Jugador("Santiago", "blanco")
        self.assertEqual(jugador.color, "blanco")

    def test_constructor_color_negro(self):
        """Test que el constructor acepta color negro"""
        jugador = Jugador("Vanina", "negro")
        self.assertEqual(jugador.color, "negro")

    def test_dos_jugadores_diferentes(self):
        """Test que dos jugadores con diferentes atributos no son iguales"""
        jugador1 = Jugador("Santiago", "blanco")
        jugador2 = Jugador("Vanina", "negro")
        self.assertNotEqual(jugador1.nombre, jugador2.nombre)
        self.assertNotEqual(jugador1.color, jugador2.color)

    def test_jugador_setter_nombre_invalido_no_string(self):
        """Test que el setter de nombre rechaza valores no string"""
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = 123

    def test_jugador_setter_nombre_vacio(self):
        """Test que el setter de nombre rechaza strings vacíos"""
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = ""

    def test_jugador_setter_nombre_solo_espacios(self):
        """Test que el setter de nombre rechaza strings solo con espacios"""
        jugador = Jugador("Test", "blanco")
        with self.assertRaises(ValueError):
            jugador.jugador = "   "

    def test_jugador_setter_color_cambio(self):
        """Test que el setter de color permite cambiar el color"""
        jugador = Jugador("Test", "negro")
        jugador.color = "blanco"
        self.assertEqual(jugador.color, "blanco")

if __name__ == '__main__':
    unittest.main()
