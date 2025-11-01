from core.checkers import Ficha
import unittest

class TestFicha(unittest.TestCase):

    def test_ficha_str_blanca(self):
        """Test representación string de ficha blanca"""
        ficha = Ficha("blanco", 0)
        self.assertEqual(str(ficha), "blanco en 0")

    def test_ficha_str_negra(self):
        """Test representación string de ficha negra"""
        ficha = Ficha("negro", 5)
        self.assertEqual(str(ficha), "negro en 5")

    def test_dos_fichas_diferentes(self):
        """Test que fichas con diferentes atributos no son iguales"""
        ficha_blanca = Ficha("blanco", 23)
        ficha_negra = Ficha("negro", 22)
        self.assertNotEqual(ficha_blanca, ficha_negra)

    def test_get_ficha_color(self):
        """Test que get_ficha retorna el color correcto"""
        ficha_blanca = Ficha("blanco", 5)
        ficha_negra = Ficha("negro", 10)
        self.assertEqual(ficha_blanca.get_ficha(), "blanco")
        self.assertEqual(ficha_negra.get_ficha(), "negro")

    def test_get_movimiento_posicion(self):
        """Test que get_movimiento retorna la posición correcta"""
        ficha_inicio = Ficha("blanco", 0)
        ficha_medio = Ficha("negro", 12)
        ficha_final = Ficha("blanco", 23)
        self.assertEqual(ficha_inicio.get_movimiento(), 0)
        self.assertEqual(ficha_medio.get_movimiento(), 12)
        self.assertEqual(ficha_final.get_movimiento(), 23)

    def test_adentro_almacen_true(self):
        """Test que adentro_almacen retorna True para posición -1"""
        ficha = Ficha("blanco", -1)
        self.assertTrue(ficha.adentro_almacen())

    def test_adentro_almacen_false(self):
        """Test que adentro_almacen retorna False para posiciones normales"""
        ficha_cero = Ficha("negro", 0)
        ficha_normal = Ficha("blanco", 10)
        self.assertFalse(ficha_cero.adentro_almacen())
        self.assertFalse(ficha_normal.adentro_almacen())

if __name__ == '__main__':
    unittest.main()