import unittest
from core.backgammongame import BackgammonGame
from unittest.mock import patch
class TestBackgammonGame(unittest.TestCase):

    def test_constructor(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertEqual(juego.get_jugador1().nombre,"Santiago")
        self.assertEqual(juego.get_jugador2().nombre, "Vanina")
        self.assertEqual(juego.get_jugador1().color, "negro")
        self.assertEqual(juego.get_jugador2().color, "blanco")
    
    def test_dados(self):
        juego = BackgammonGame("Santiago","Vanina")
        dados = juego.tirar_dados()
        self.assertIn(dados.valores_dados()[0], [1,2,3,4,5,6])
        self.assertIn(dados.valores_dados()[1], [1,2,3,4,5,6])

    def test_obtener_turno(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")
        juego.__turno__ = juego.__jugador2__
        self.assertEqual(juego.obtener_turno(), "Es el turno de Vanina")

    def test_cambiar_turno(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")
        juego.cambiar_turno()
        self.assertEqual(juego.obtener_turno(), "Es el turno de Vanina")
        juego.cambiar_turno()
        self.assertEqual(juego.obtener_turno(), "Es el turno de Santiago")

    @patch("core.dice.random.randint", side_effect = [5,3])
    def test_mover_ficha(self, mock_randint):
       juego = BackgammonGame("Santiago","Vanina")
       juego.get_tablero().tablero_inicial()
       dados = juego.tirar_dados()
       # Jugador1 (negro) mueve de 23 hacia 0 (restando)
       self.assertTrue(juego.mover_ficha(juego.get_jugador1(), 23, 18, 5))
       self.assertTrue(juego.mover_ficha(juego.get_jugador1(), 23, 20, 3))
       # Sin dados disponibles, no puede mover
       self.assertFalse(juego.mover_ficha(juego.get_jugador1(), 23, 18, 5))
    
    def test_puede_mover(self):
        juego = BackgammonGame("Santiago","Vanina")
        juego.tirar_dados()
        self.assertTrue(juego.puede_mover(juego.get_jugador1()))
        juego.cambiar_turno()
        self.assertFalse(juego.puede_mover(juego.get_jugador1()))
        self.assertTrue(juego.puede_mover(juego.get_jugador2()))

    @patch("core.dice.random.randint", side_effect = [4,2])
    def test_usar_dados(self, mock_randint):
        juego = BackgammonGame("Santiago","Vanina")
        dados = juego.tirar_dados()
        valor1 = dados.valores_dados()[0]
        valor2 = dados.valores_dados()[1]
        self.assertEqual(valor1, 4)
        self.assertEqual(valor2, 2)
        self.assertEqual(len(dados.valores_dados()), 2)
        self.assertTrue(juego.usar_dados(valor1))
        self.assertEqual(len(dados.valores_dados()), 1)
        self.assertNotIn(valor1, dados.valores_dados())
        self.assertTrue(juego.usar_dados(valor2))
        self.assertEqual(len(dados.valores_dados()), 0)
        self.assertFalse(juego.usar_dados(5))
      
    def test_estado_juego(self):
        juego = BackgammonGame("Santiago","Vanina")
        estado = juego.estado_juego()
        self.assertIn("tablero", estado)
        self.assertIn("turno", estado)
        self.assertEqual(estado["turno"], "Santiago")
        self.assertEqual(len(estado["tablero"]), 24)
    
    def test_hay_almacen(self):
        juego = BackgammonGame("Santiago","Vanina")
        self.assertFalse(juego.hay_fichas_en_almacen(juego.get_jugador1()))
        self.assertFalse(juego.hay_fichas_en_almacen(juego.get_jugador2()))
        juego.__tablero__.__almacen_ficha__["negro"] = 1
        juego.__tablero__.__almacen_ficha__["blanco"] = 2
        self.assertTrue(juego.hay_fichas_en_almacen(juego.get_jugador1()))
        self.assertTrue(juego.hay_fichas_en_almacen(juego.get_jugador2()))
        