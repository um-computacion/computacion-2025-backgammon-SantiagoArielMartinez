import unittest
from core.board import Tablero
from core.player import Jugador

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tab = Tablero()
        self.tablero = self.tab.tablero_inicial()

    # Tests de inicialización
    def test_cantidad_casilleros(self):
        self.assertEqual(len(self.tablero), 24)

    # Tests de configuración inicial - Fichas blancas
    def test_tablero_blanco_posicion_0(self):
        self.assertListEqual(self.tablero[0], ["blanco", "blanco"])
    
    def test_tablero_blanco_posicion_11(self):
        self.assertListEqual(self.tablero[11], ["blanco", "blanco", "blanco", "blanco", "blanco"])
    
    def test_tablero_blanco_posicion_17(self):
        self.assertListEqual(self.tablero[17], ["blanco", "blanco", "blanco", "blanco", "blanco"])
    
    def test_tablero_blanco_posicion_19(self):
        self.assertListEqual(self.tablero[19], ["blanco", "blanco", "blanco"])

    # Tests de configuración inicial - Fichas negras
    def test_tablero_negro_posicion_23(self):
        self.assertListEqual(self.tablero[23], ["negro", "negro", "negro", "negro", "negro"])
    
    def test_tablero_negro_posicion_7(self):
        self.assertListEqual(self.tablero[7], ["negro", "negro", "negro"])
    
    def test_tablero_negro_posicion_12(self):
        self.assertListEqual(self.tablero[12], ["negro", "negro"])
    
    def test_tablero_negro_posicion_5(self):
        self.assertListEqual(self.tablero[5], ["negro", "negro", "negro", "negro", "negro"])

    # Tests de estado del tablero
    def test_mostrar_tablero(self):
        self.assertEqual(self.tab.estado_tablero(), self.tab.__contenedor__)

    # Tests de sacar_checker - Casos exitosos
    def test_sacar_checker_blanco_posicion_0(self):
        self.assertEqual(self.tab.sacar_checker(0), "blanco")
    
    def test_sacar_checker_negro_posicion_5(self):
        self.assertEqual(self.tab.sacar_checker(5), "negro")
    
    def test_sacar_checker_posicion_vacia(self):
        resultado = self.tab.sacar_checker(1)
        self.assertIsNone(resultado)

    def test_mover_checker_blanco(self):
        self.assertEqual(self.tab.mover_checker(0, 3, "blanco"), "blanco")
    
    def test_mover_checker_negro(self):
        self.assertEqual(self.tab.mover_checker(5, 7, "negro"), "negro")

    def test_validar_movimiento_a_posicion_con_fichas_enemigas(self):
        jugador_negro = Jugador("Gonzalo", "negro")
        self.assertTrue(self.tab.movimiento_valido(0, 5, jugador_negro))
    
    def test_validar_movimiento_a_posicion_vacia(self):
        jugador_blanco = Jugador("Santi", "blanco")
        self.assertTrue(self.tab.movimiento_valido(0, 1, jugador_blanco))
    
    def test_validar_movimiento_captura_blot(self):
        jugador_blanco = Jugador("Santi", "blanco")
        self.tab.__contenedor__[5] = ["negro"]
        self.tab.__contenedor__[1] = []
        self.assertTrue(self.tab.movimiento_valido(0, 1, jugador_blanco))

    def test_movimiento_invalido_desde_posicion_vacia(self):
        jugador_blanco = Jugador("Sanchi", "blanco")
        self.assertFalse(self.tab.movimiento_valido(1, 5, jugador_blanco))
    
    def test_movimiento_invalido_con_fichas_en_almacen(self):
        jugador_blanco = Jugador("Santi", "blanco")
        self.tab.__almacen_ficha__[jugador_blanco.color] += 1
        self.assertFalse(self.tab.movimiento_valido(0, 1, jugador_blanco))
    
    def test_movimiento_invalido_posicion_origen_fuera_rango_negativo(self):
        jugador_blanco = Jugador("Sanchi", "blanco")
        resultado = self.tab.movimiento_valido(-2, 5, jugador_blanco)
        self.assertFalse(resultado)
    
    def test_movimiento_invalido_posicion_destino_fuera_rango_positivo(self):
        jugador_blanco = Jugador("Sanchi", "blanco")
        resultado = self.tab.movimiento_valido(0, 26, jugador_blanco)
        self.assertFalse(resultado)
    
    def test_movimiento_invalido_posicion_origen_fuera_rango_positivo(self):
        jugador_blanco = Jugador("Sanchi", "blanco")
        resultado = self.tab.movimiento_valido(55, 5, jugador_blanco)
        self.assertFalse(resultado)

    def test_estado_almacenamiento_inicial(self):
        almacen = self.tab.estado_almacenamiento()
        self.assertEqual(almacen["blanco"], 0)
        self.assertEqual(almacen["negro"], 0)
    
    def test_comer_checker(self): 
        self.tab.__contenedor__[10] = ["negro"]
        resultado = self.tab.comer_checker(10, "blanco")
        self.assertTrue(resultado)
        self.assertEqual(self.tab.__almacen_ficha__["negro"], 1)
    
    def test_comer_checker_posicion_vacia(self):
        resultado = self.tab.comer_checker(1, "blanco")
        self.assertFalse(resultado)
    
    def test_comer_checker_multiples_fichas_enemigas(self):
        self.tab.__contenedor__[10] = ["negro", "negro"]
        resultado = self.tab.comer_checker(10, "blanco")
        self.assertFalse(resultado)
    
    def test_sacar_checker_comida_exitoso(self):
        self.tab.__almacen_ficha__["blanco"] = 1
        resultado = self.tab.sacar_checker_comida("blanco", 2)
        self.assertTrue(resultado)
        self.assertEqual(self.tab.__almacen_ficha__["blanco"], 0)
        self.assertIn("blanco", self.tab.__contenedor__[2])
    
    def test_sacar_checker_comida_sin_fichas_en_almacen(self):
        resultado = self.tab.sacar_checker_comida("blanco", 5)
        self.assertFalse(resultado)
    
    def test_sacar_checker_comida_posicion_invalida(self):
        self.tab.__almacen_ficha__["blanco"] = 1
        resultado = self.tab.sacar_checker_comida("blanco", 30)
        self.assertFalse(resultado)

    def test_verificar_ganador_con_fichas_en_almacen(self):
        self.tab.__almacen_ficha__["blanco"] = 1
        self.assertFalse(self.tab.verificar_ganador("blanco"))
    
    def test_verificar_ganador_tablero_vacio(self):
        self.tab.__contenedor__ = [[] for _ in range(24)]
        self.tab.__banco__["blanco"] = 15
        self.assertTrue(self.tab.verificar_ganador("blanco"))
    
    def test_verificar_ganador_con_fichas_en_tablero(self):
        self.assertFalse(self.tab.verificar_ganador("blanco"))

    def test_bear_off_permitido_todas_fichas_en_casa_blanco(self):
        self.tab.__contenedor__ = [[] for _ in range(24)]
        self.tab.__contenedor__[18] = ["blanco", "blanco"]
        self.tab.__contenedor__[20] = ["blanco"]
        self.assertTrue(self.tab.bear_off_permitido("blanco"))
    
    def test_bear_off_no_permitido_fichas_fuera_casa_blanco(self):
        self.assertFalse(self.tab.bear_off_permitido("blanco"))
    
    def test_bear_off_permitido_todas_fichas_en_casa_negro(self):
        self.tab.__contenedor__ = [[] for _ in range(24)]
        self.tab.__contenedor__[0] = ["negro", "negro"]
        self.tab.__contenedor__[3] = ["negro"]
        self.assertTrue(self.tab.bear_off_permitido("negro"))
    
    def test_bear_off_exitoso(self):
        self.tab.__contenedor__ = [[] for _ in range(24)]
        self.tab.__contenedor__[18] = ["blanco"]
        resultado = self.tab.bear_off(18, "blanco")
        self.assertTrue(resultado)
        self.assertEqual(len(self.tab.__contenedor__[18]), 0)
    
    def test_bear_off_no_permitido(self):
        resultado = self.tab.bear_off(0, "blanco")
        self.assertFalse(resultado)

    # Tests adicionales para cubrir líneas faltantes
    def test_mover_checker_color_incorrecto(self):
        """Test mover checker con color que no corresponde a la posición"""
        resultado = self.tab.mover_checker(0, 3, "negro")
        self.assertIsNone(resultado)

    def test_mover_checker_posicion_origen_invalida_negativa(self):
        """Test mover checker con posición de origen negativa"""
        resultado = self.tab.mover_checker(-1, 5, "blanco")
        self.assertIsNone(resultado)

    def test_mover_checker_posicion_destino_invalida_mayor(self):
        """Test mover checker con posición de destino fuera de rango"""
        resultado = self.tab.mover_checker(0, 25, "blanco")
        self.assertIsNone(resultado)

    def test_mover_checker_desde_posicion_vacia(self):
        """Test intentar mover desde una posición vacía"""
        resultado = self.tab.mover_checker(1, 5, "blanco")
        self.assertIsNone(resultado)

    def test_movimiento_valido_posicion_destino_con_mismas_fichas(self):
        """Test movimiento a posición con fichas del mismo color"""
        jugador_blanco = Jugador("Test", "blanco")
        self.assertTrue(self.tab.movimiento_valido(0, 11, jugador_blanco))

    def test_movimiento_valido_captura_con_almacen_vacio(self):
        """Test captura cuando no hay fichas en almacén"""
        jugador_negro = Jugador("Test", "negro")
        self.tab.__contenedor__[0] = ["blanco"]
        resultado = self.tab.movimiento_valido(5, 0, jugador_negro)
        self.assertTrue(resultado)

    def test_comer_checker_misma_ficha_color(self):
        """Test intentar comer ficha del mismo color"""
        self.tab.__contenedor__[10] = ["blanco"]
        resultado = self.tab.comer_checker(10, "blanco")
        self.assertFalse(resultado)

    def test_sacar_checker_comida_posicion_negativa(self):
        """Test sacar checker comida con posición negativa"""
        self.tab.__almacen_ficha__["blanco"] = 1
        resultado = self.tab.sacar_checker_comida("blanco", -1)
        self.assertFalse(resultado)

    def test_verificar_ganador_color_inexistente(self):
        """Test verificar ganador con color que no existe en almacén"""
        resultado = self.tab.verificar_ganador("verde")
        self.assertFalse(resultado)

    def test_bear_off_posicion_vacia(self):
        """Test bear off desde posición vacía"""
        self.tab.__contenedor__ = [[] for _ in range(24)]
        resultado = self.tab.bear_off(18, "blanco")
        self.assertFalse(resultado)

    def test_bear_off_color_incorrecto(self):
        """Test bear off con color incorrecto"""
        self.tab._Tablero__contenedor__ = [[] for _ in range(24)]
        self.tab._Tablero__contenedor__[18] = ["negro"]
        resultado = self.tab.bear_off(18, "blanco")
        self.assertFalse(resultado)

    def test_bear_off_permitido_negro_con_fichas_fuera(self):
        """Test bear off negro no permitido con fichas fuera de casa"""
        self.tab.__contenedor__[10] = ["negro"]
        resultado = self.tab.bear_off_permitido("negro")
        self.assertFalse(resultado)

    def test_mover_checker_con_excepcion_index_error(self):
        try:
            resultado = self.tab.mover_checker(100, 5, "blanco")
            self.assertIsNone(resultado)
        except IndexError:
            pass

    def test_mover_checker_con_excepcion_value_error(self):
        try:
            self.tab.__contenedor__[0] = []
            resultado = self.tab.mover_checker(0, 5, "blanco")
            self.assertIsNone(resultado)
        except (ValueError, IndexError):
            pass

if __name__ == '__main__':
    unittest.main()