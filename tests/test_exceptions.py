"""
Tests para las excepciones personalizadas del juego.
"""
import unittest
from core.exceptions import (
    PosicionInvalida,
    PosicionVacia,
    MovimientoInvalido,
    NoEsTuTurno,
    SinDados,
    ColorIncorrecto
)
from core.board import Tablero
from core.player import Jugador
from core.backgammongame import BackgammonGame


class TestExcepciones(unittest.TestCase):
    """Tests para las excepciones simples"""

    def test_posicion_invalida_en_sacar_checker(self):
        """Test que sacar_checker lanza excepción con posición inválida"""
        tablero = Tablero()
        with self.assertRaises(PosicionInvalida):
            tablero.sacar_checker(25)

    def test_posicion_invalida_negativa(self):
        """Test posición negativa lanza excepción"""
        tablero = Tablero()
        with self.assertRaises(PosicionInvalida):
            tablero.sacar_checker(-5)

    def test_posicion_vacia_en_sacar_checker(self):
        """Test que sacar_checker lanza excepción con posición vacía"""
        tablero = Tablero()
        tablero.__contenedor__[5] = []
        with self.assertRaises(PosicionVacia):
            tablero.sacar_checker(5)

    def test_no_es_tu_turno_al_mover(self):
        """Test que mover_ficha lanza excepción si no es tu turno"""
        juego = BackgammonGame("Jugador1", "Jugador2")
        juego.tirar_dados()
        jugador2 = juego.get_jugador2()
        with self.assertRaises(NoEsTuTurno):
            juego.mover_ficha(jugador2, 0, 5, 5)

    def test_sin_dados_al_usar_dado_inexistente(self):
        """Test que usar dado inexistente lanza excepción"""
        juego = BackgammonGame("Jugador1", "Jugador2")
        juego.tirar_dados()
        jugador1 = juego.get_jugador1()
        with self.assertRaises(SinDados):
            juego.mover_ficha(jugador1, 23, 18, 7)

    def test_excepcion_posicion_invalida_mensaje(self):
        """Test que la excepción PosicionInvalida tiene mensaje correcto"""
        try:
            raise PosicionInvalida("La posición 30 no existe")
        except PosicionInvalida as e:
            self.assertIn("30", str(e))

    def test_excepcion_posicion_vacia_mensaje(self):
        """Test que la excepción PosicionVacia tiene mensaje"""
        try:
            raise PosicionVacia("No hay fichas en posición 10")
        except PosicionVacia as e:
            self.assertIn("10", str(e))

    def test_excepcion_no_es_tu_turno_mensaje(self):
        """Test que la excepción NoEsTuTurno tiene mensaje"""
        try:
            raise NoEsTuTurno("No es turno de Juan")
        except NoEsTuTurno as e:
            self.assertIn("Juan", str(e))

    def test_excepcion_sin_dados_mensaje(self):
        """Test que la excepción SinDados tiene mensaje"""
        try:
            raise SinDados("No hay dados disponibles")
        except SinDados as e:
            self.assertIn("dados", str(e))

    def test_movimiento_invalido_excepcion(self):
        """Test que MovimientoInvalido se puede lanzar"""
        with self.assertRaises(MovimientoInvalido):
            raise MovimientoInvalido("Movimiento no permitido")

    def test_color_incorrecto_excepcion(self):
        """Test que ColorIncorrecto se puede lanzar"""
        with self.assertRaises(ColorIncorrecto):
            raise ColorIncorrecto("Color debe ser blanco o negro")


if __name__ == '__main__':
    unittest.main()
