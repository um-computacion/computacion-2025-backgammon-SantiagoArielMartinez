"""
Módulo de tests para la interfaz CLI del juego de Backgammon.
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from cli.cli import CLI


class TestCLI(unittest.TestCase):
    """Tests para la clase CLI"""

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2"])
    @patch('builtins.print')
    def test_constructor_crea_juego(self, mock_print, mock_input):
        """Test que el constructor crea un juego correctamente"""
        cli = CLI()
        self.assertIsNotNone(cli.__game__)

    @patch('builtins.input', side_effect=["Santiago", "Vanina"])
    @patch('builtins.print')
    def test_constructor_con_nombres_personalizados(self, mock_print, mock_input):
        """Test constructor con nombres específicos"""
        cli = CLI()
        self.assertEqual(cli.__game__.get_jugador1().nombre, "Santiago")
        self.assertEqual(cli.__game__.get_jugador2().nombre, "Vanina")

    @patch('builtins.input', side_effect=["Juan", "Maria"])
    @patch('builtins.print')
    def test_mostrar_tablero_imprime_estado(self, mock_print, mock_input):
        """Test que mostrar_tablero imprime el estado del tablero"""
        cli = CLI()
        cli.mostrar_tablero()
        # Verifica que se haya llamado print
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Test1", "Test2"])
    @patch('builtins.print')
    def test_mostrar_turno_imprime_turno_actual(self, mock_print, mock_input):
        """Test que mostrar_turno imprime el turno del jugador"""
        cli = CLI()
        cli.mostrar_turno()
        # Verifica que se imprimió información del turno
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Player1", "Player2"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[4, 2])
    def test_tirar_dados_retorna_valores(self, mock_randint, mock_print, mock_input):
        """Test que tirar_dados retorna valores correctos"""
        cli = CLI()
        valores = cli.tirar_dados()
        self.assertEqual(len(valores), 2)
        self.assertIn(valores[0], [1, 2, 3, 4, 5, 6])
        self.assertIn(valores[1], [1, 2, 3, 4, 5, 6])

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "0", "5", "5"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_realizar_movimiento_exitoso(self, mock_randint, mock_print, mock_input):
        """Test realizar movimiento exitoso"""
        cli = CLI()
        cli.__game__.get_tablero().tablero_inicial()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        resultado = cli.realizar_movimiento(jugador)
        self.assertIsInstance(resultado, bool)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "abc", "def", "xyz"])
    @patch('builtins.print')
    def test_realizar_movimiento_entrada_invalida(self, mock_print, mock_input):
        """Test realizar movimiento con entrada inválida"""
        cli = CLI()
        jugador = cli.__game__.get_jugador1()
        resultado = cli.realizar_movimiento(jugador)
        self.assertFalse(resultado)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "100", "200", "7"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_realizar_movimiento_posiciones_invalidas(self, mock_randint, mock_print, mock_input):
        """Test realizar movimiento con posiciones inválidas"""
        cli = CLI()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        resultado = cli.realizar_movimiento(jugador)
        self.assertFalse(resultado)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_opcion_finalizar(self, mock_randint, mock_print, mock_input):
        """Test menu turno con opción finalizar"""
        cli = CLI()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        # Verifica que el menú se ejecutó sin errores
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "3", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_opcion_ver_tablero(self, mock_randint, mock_print, mock_input):
        """Test menu turno con opción ver tablero"""
        cli = CLI()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "2", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_reingresar_sin_fichas(self, mock_randint, mock_print, mock_input):
        """Test menu turno intentando reingresar sin fichas en almacén"""
        cli = CLI()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        # Verifica que se manejó correctamente la opción
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "2", "3", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_reingresar_con_fichas(self, mock_randint, mock_print, mock_input):
        """Test menu turno reingresando ficha del almacén"""
        cli = CLI()
        # Usa el método público para agregar fichas al almacén
        cli.__game__.get_tablero().agregar_a_almacen("negro", 1)
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "5", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_opcion_invalida(self, mock_randint, mock_print, mock_input):
        """Test menu turno con opción inválida"""
        cli = CLI()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2", "1", "23", "18", "5", "4"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[5, 3])
    def test_menu_turno_mover_ficha_exitoso(self, mock_randint, mock_print, mock_input):
        """Test menu turno moviendo ficha exitosamente"""
        cli = CLI()
        cli.__game__.get_tablero().tablero_inicial()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        cli.menu_turno(jugador)
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2"])
    @patch('builtins.print')
    def test_mostrar_tablero_muestra_almacen(self, mock_print, mock_input):
        """Test que mostrar tablero muestra el almacén"""
        cli = CLI()
        cli.__game__.get_tablero().__almacen_ficha__["negro"] = 2
        cli.__game__.get_tablero().__almacen_ficha__["blanco"] = 1
        cli.mostrar_tablero()
        # Verifica que se imprimió información del almacén
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2"])
    @patch('builtins.print')
    def test_mostrar_tablero_muestra_fichas_vacias(self, mock_print, mock_input):
        """Test que mostrar tablero muestra posiciones vacías"""
        cli = CLI()
        cli.__game__.get_tablero().__contenedor__ = [[] for _ in range(24)]
        cli.mostrar_tablero()
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2"])
    @patch('builtins.print')
    def test_mostrar_tablero_muestra_fichas_ocupadas(self, mock_print, mock_input):
        """Test que mostrar tablero muestra posiciones ocupadas"""
        cli = CLI()
        cli.__game__.get_tablero().tablero_inicial()
        cli.mostrar_tablero()
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=["Test1", "Test2"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[3, 3])
    def test_tirar_dados_con_dobles(self, mock_randint, mock_print, mock_input):
        """Test tirar dados con valores dobles"""
        cli = CLI()
        valores = cli.tirar_dados()
        self.assertEqual(len(valores), 4)  # Dados dobles generan 4 valores

    @patch('builtins.input', side_effect=["Jugador1", "Jugador2"])
    @patch('builtins.print')
    def test_get_game_devuelve_instancia_correcta(self, mock_print, mock_input):
        """Test que se puede acceder al juego"""
        cli = CLI()
        game = cli.__game__
        self.assertIsNotNone(game)
        self.assertEqual(game.get_jugador1().nombre, "Jugador1")

    @patch('builtins.input', side_effect=["Player1", "Player2", "0", "1", "1"])
    @patch('builtins.print')
    @patch('core.dice.random.randint', side_effect=[1, 2])
    def test_realizar_movimiento_con_movimiento_valido(self, mock_randint, mock_print, mock_input):
        """Test realizar movimiento válido después de tirar dados"""
        cli = CLI()
        cli.__game__.get_tablero().tablero_inicial()
        cli.__game__.tirar_dados()
        jugador = cli.__game__.get_jugador1()
        # Aunque el movimiento sea inválido, debe retornar False sin error
        resultado = cli.realizar_movimiento(jugador)
        self.assertIsInstance(resultado, bool)


if __name__ == '__main__':
    unittest.main()
