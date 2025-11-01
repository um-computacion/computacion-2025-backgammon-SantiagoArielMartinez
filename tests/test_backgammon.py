import unittest
from core.backgammongame import BackgammonGame
from unittest.mock import patch

class TestBackgammonGame(unittest.TestCase):

    # Tests de inicialización
    def test_constructor_jugador1_nombre(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.get_jugador1().nombre, "Santiago")

    def test_constructor_jugador2_nombre(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.get_jugador2().nombre, "Vanina")

    def test_constructor_jugador1_color(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.get_jugador1().color, "negro")

    def test_constructor_jugador2_color(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.get_jugador2().color, "blanco")

    # Tests de dados
    def test_dados_valor_dado1_en_rango(self):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        self.assertIn(dados.valores_dados()[0], [1, 2, 3, 4, 5, 6])

    def test_dados_valor_dado2_en_rango(self):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        self.assertIn(dados.valores_dados()[1], [1, 2, 3, 4, 5, 6])

    # Tests de obtener_turno
    def test_obtener_turno_inicial_jugador1(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")

    def test_obtener_turno_jugador2(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__turno__ = juego.__jugador2__
        self.assertEqual(juego.obtener_turno(), "Es el turno de Vanina")

    # Tests de cambiar_turno
    def test_cambiar_turno_de_jugador1_a_jugador2(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")
        juego.cambiar_turno()
        self.assertEqual(juego.obtener_turno(), "Es el turno de Vanina")

    def test_cambiar_turno_de_jugador2_a_jugador1(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.cambiar_turno()
        self.assertEqual(juego.obtener_turno(), "Es el turno de Vanina")
        juego.cambiar_turno()
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")

    # Tests de mover_ficha
    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_negro_movimiento_valido_1(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        self.assertTrue(juego.mover_ficha(juego.get_jugador1(), 23, 18, 5))

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_negro_movimiento_valido_2(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        juego.usar_dados(5)
        self.assertTrue(juego.mover_ficha(juego.get_jugador1(), 23, 20, 3))

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_sin_dados_disponibles(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        juego.usar_dados(5)
        juego.usar_dados(3)
        self.assertFalse(juego.mover_ficha(juego.get_jugador1(), 23, 18, 5))

    # Tests de puede_mover
    def test_puede_mover_jugador_con_turno_y_dados(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        self.assertTrue(juego.puede_mover(juego.get_jugador1()))

    def test_puede_mover_jugador_sin_turno(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        juego.cambiar_turno()
        self.assertFalse(juego.puede_mover(juego.get_jugador1()))

    def test_puede_mover_jugador_con_turno_correcto(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        juego.cambiar_turno()
        self.assertTrue(juego.puede_mover(juego.get_jugador2()))

    # Tests de usar_dados
    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_valor_existente_1(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        valor1 = dados.valores_dados()[0]
        self.assertEqual(valor1, 4)
        self.assertTrue(juego.usar_dados(valor1))

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_reduce_cantidad(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        self.assertEqual(len(dados.valores_dados()), 2)
        juego.usar_dados(4)
        self.assertEqual(len(dados.valores_dados()), 1)

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_elimina_valor_usado(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        valor1 = dados.valores_dados()[0]
        juego.usar_dados(valor1)
        self.assertNotIn(valor1, dados.valores_dados())

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_valor_existente_2(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        juego.usar_dados(4)
        self.assertTrue(juego.usar_dados(2))

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_todos_usados(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        juego.usar_dados(4)
        juego.usar_dados(2)
        self.assertEqual(len(dados.valores_dados()), 0)

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_usar_dados_valor_no_existente(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        self.assertFalse(juego.usar_dados(5))

    # Tests de estado_juego
    def test_estado_juego_contiene_tablero(self):
        juego = BackgammonGame("Santiago", "Vanina")
        estado = juego.estado_juego()
        self.assertIn("tablero", estado)

    def test_estado_juego_contiene_turno(self):
        juego = BackgammonGame("Santiago", "Vanina")
        estado = juego.estado_juego()
        self.assertIn("turno", estado)

    def test_estado_juego_turno_correcto(self):
        juego = BackgammonGame("Santiago", "Vanina")
        estado = juego.estado_juego()
        self.assertEqual(estado["turno"], "Santiago")

    def test_estado_juego_tablero_longitud(self):
        juego = BackgammonGame("Santiago", "Vanina")
        estado = juego.estado_juego()
        self.assertEqual(len(estado["tablero"]), 24)

    # Tests de hay_fichas_en_almacen
    def test_hay_almacen_inicial_jugador1(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertFalse(juego.hay_fichas_en_almacen(juego.get_jugador1()))

    def test_hay_almacen_inicial_jugador2(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertFalse(juego.hay_fichas_en_almacen(juego.get_jugador2()))

    def test_hay_almacen_con_fichas_negro(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        self.assertTrue(juego.hay_fichas_en_almacen(juego.get_jugador1()))

    def test_hay_almacen_con_fichas_blanco(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["blanco"] = 2
        self.assertTrue(juego.hay_fichas_en_almacen(juego.get_jugador2()))

    # Tests de reingresar_ficha
    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_sin_turno(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        valor_dado = juego.__dados__.valores_dados()[0]
        self.assertFalse(juego.reingresar_ficha(juego.get_jugador2(), valor_dado))

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_exitoso(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        valor_dado = juego.__dados__.valores_dados()[0]
        self.assertTrue(juego.reingresar_ficha(juego.get_jugador1(), valor_dado))

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_reduce_almacen(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        valor_dado = juego.__dados__.valores_dados()[0]
        juego.reingresar_ficha(juego.get_jugador1(), valor_dado)
        self.assertEqual(juego.__tablero__.__almacen_ficha__["negro"], 0)

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_usa_dado(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        valor_dado = juego.__dados__.valores_dados()[0]
        juego.reingresar_ficha(juego.get_jugador1(), valor_dado)
        self.assertNotIn(valor_dado, juego.__dados__.valores_dados())

    # Tests de verificar_ganador
    def test_verificar_ganador_sin_ganador_inicial(self):
        juego = BackgammonGame("Santiago", "Vanina")
        self.assertIsNone(juego.verificar_ganador())

    def test_verificar_ganador_con_fichas_en_almacen(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        self.assertIsNone(juego.verificar_ganador())

    def test_verificar_ganador_tablero_vacio_jugador1(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__banco__["negro"] = 15
        juego.__tablero__.__contenedor__ = [[] for _ in range(24)]
        self.assertEqual(juego.verificar_ganador(), "Santiago")

    # Tests de finalizar_turno
    def test_finalizar_turno_cambia_jugador(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        self.assertTrue(juego.puede_mover(juego.get_jugador1()))
        juego.finalizar_turno()
        self.assertFalse(juego.puede_mover(juego.get_jugador1()))

    def test_finalizar_turno_permite_siguiente_jugador(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        juego.finalizar_turno()
        juego.tirar_dados()
        self.assertTrue(juego.puede_mover(juego.get_jugador2()))

    # Tests adicionales para cubrir líneas faltantes
    def test_puede_mover_sin_dados_tirados(self):
        """Test puede_mover cuando no se han tirado dados (AttributeError)"""
        juego = BackgammonGame("Santiago", "Vanina")
        resultado = juego.puede_mover(juego.get_jugador1())
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_mover_ficha_jugador_sin_turno(self, mock_randint):
        """Test mover ficha cuando no es el turno del jugador"""
        from core.exceptions import NoEsTuTurno
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        with self.assertRaises(NoEsTuTurno):
            juego.mover_ficha(juego.get_jugador2(), 0, 3, 3)

    @patch("core.dice.random.randint", side_effect=[4, 2])
    def test_mover_ficha_dado_no_disponible(self, mock_randint):
        """Test mover ficha con un valor de dado que no está disponible"""
        from core.exceptions import SinDados
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        with self.assertRaises(SinDados):
            juego.mover_ficha(juego.get_jugador1(), 23, 18, 6)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_movimiento_invalido(self, mock_randint):
        """Test mover ficha con movimiento inválido según reglas del tablero"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        resultado = juego.mover_ficha(juego.get_jugador1(), 23, 0, 5)
        self.assertFalse(resultado)

    def test_estado_juego_sin_dados_tirados(self):
        """Test estado_juego cuando no se han tirado dados (maneja AttributeError)"""
        juego = BackgammonGame("Santiago", "Vanina")
        estado = juego.estado_juego()
        self.assertEqual(estado["dados"], [])

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_sin_fichas_en_almacen(self, mock_randint):
        """Test reingresar ficha cuando no hay fichas en almacén"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 3)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_dado_no_disponible(self, mock_randint):
        """Test reingresar ficha con dado no disponible"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 6)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_posicion_bloqueada(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.__tablero__.__contenedor__[21] = ["blanco", "blanco"]
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 3)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[3, 5])
    def test_reingresar_ficha_blanco_exitoso(self, mock_randint):
        """Test reingresar ficha blanca exitosamente"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.cambiar_turno()
        juego.__tablero__.__almacen_ficha__["blanco"] = 1
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador2(), 3)
        self.assertTrue(resultado)

    def test_verificar_ganador_jugador2_gana(self):
        """Test verificar ganador cuando gana el jugador 2"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__contenedor__ = [[] for _ in range(24)]
        juego.__tablero__.__banco__["blanco"] = 15
        juego.__tablero__.__almacen_ficha__["negro"] = 0
        resultado = juego.verificar_ganador()
        self.assertEqual(resultado, "Vanina")

    @patch("core.dice.random.randint", side_effect=[6, 6])
    def test_tirar_dados_dobles(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        dados = juego.tirar_dados()
        self.assertEqual(len(dados.valores_dados()), 4)

    def test_get_turno_actual_retorna_jugador(self):
        """Test get_turno_actual retorna el jugador correcto"""
        juego = BackgammonGame("Santiago", "Vanina")
        turno = juego.get_turno_actual()
        self.assertEqual(turno, juego.get_jugador1())

    def test_cambiar_turno_multiple_veces(self):
        """Test cambiar turno múltiples veces"""
        juego = BackgammonGame("Santiago", "Vanina")
        turno_inicial = juego.get_turno_actual()
        juego.cambiar_turno()
        juego.cambiar_turno()
        self.assertEqual(juego.get_turno_actual(), turno_inicial)
    @patch("core.dice.random.randint", side_effect=[5, 5])
    def test_bear_off_fallido_con_dado_grande_y_ficha_atras(self, mock_randint):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__contenedor__ = [[] for _ in range(24)]
        juego.__tablero__.__contenedor__[20] = ["blanco"]
        juego.__tablero__.__contenedor__[18] = ["blanco"]
        juego.__turno__ = juego.__jugador2__
        juego.tirar_dados()
        valor_dado = juego.__dados__.valores_dados()[0]
        resultado = juego.realizar_bear_off(juego.__jugador2__, 20, 5)
        self.assertFalse(resultado)
    def test_bear_off_fallido_con_dado_insuficiente(self):
        juego = BackgammonGame("Santiago", "Vanina")
        juego.__tablero__.__contenedor__ = [[] for _ in range(24)]
        juego.__tablero__.__contenedor__[20] = ["blanco"]
        juego.__turno__ = juego.__jugador2__
        juego.__dados__.__valores__ = [3]
        resultado = juego.realizar_bear_off(juego.__jugador2__, 20, 3)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[6, 6])
    def test_mover_ficha_con_dados_dobles(self, mock_randint):
        """Test mover ficha cuando hay dados dobles"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        self.assertEqual(len(juego.__dados__.valores_dados()), 4)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_jugador_incorrecto(self, mock_randint):
        """Test que no permite mover si no es el turno del jugador"""
        from core.exceptions import NoEsTuTurno
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        with self.assertRaises(NoEsTuTurno):
            juego.mover_ficha(juego.get_jugador2(), 0, 5, 5)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_reingresar_ficha_jugador_sin_turno(self, mock_randint):
        """Test reingresar ficha sin turno"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        juego.cambiar_turno()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 3)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_reingresar_ficha_sin_fichas_en_almacen(self, mock_randint):
        """Test reingresar ficha sin fichas en almacén"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 3)
        self.assertFalse(resultado)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_reingresar_ficha_dado_no_disponible(self, mock_randint):
        """Test reingresar ficha con dado no disponible"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().__almacen_ficha__["negro"] = 1
        juego.tirar_dados()
        resultado = juego.reingresar_ficha(juego.get_jugador1(), 6)
        self.assertFalse(resultado)

    def test_verificar_ganador_jugador2_gana(self):
        """Test verificar ganador cuando gana jugador 2"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().__contenedor__ = [[] for _ in range(24)]
        juego.get_tablero().__almacen_ficha__["blanco"] = 0
        juego.get_tablero().__banco__["blanco"] = 15
        ganador = juego.verificar_ganador()
        self.assertEqual(ganador, "Vanina")

    @patch("core.dice.random.randint", side_effect=[3, 3])
    def test_dados_dobles_genera_cuatro_valores(self, mock_randint):
        """Test que dados dobles generan 4 valores"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.tirar_dados()
        self.assertEqual(len(juego.__dados__.valores_dados()), 4)

    def test_cambiar_turno_multiples_veces(self):
        """Test cambiar turno múltiples veces"""
        juego = BackgammonGame("Santiago", "Vanina")
        jugador_inicial = juego.get_turno_actual()
        juego.cambiar_turno()
        juego.cambiar_turno()
        self.assertEqual(juego.get_turno_actual(), jugador_inicial)

    @patch("core.dice.random.randint", side_effect=[5, 3])
    def test_mover_ficha_posicion_invalida(self, mock_randint):
        """Test mover ficha a posición inválida"""
        juego = BackgammonGame("Santiago", "Vanina")
        juego.get_tablero().tablero_inicial()
        juego.tirar_dados()
        resultado = juego.mover_ficha(juego.get_jugador1(), 23, 30, 5)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
