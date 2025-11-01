from core.checkers import Ficha
import unittest

class TestFicha(unittest.TestCase):

    def test_ficha_blanca_color(self):
        ficha = Ficha("blanco",0)
        self.assertEqual(str(ficha), "blanco en 0")

    def test_ficha_negra_color(self):
        ficha = Ficha("negro",5)
        self.assertEqual(str(ficha), "negro en 5")

    def test_ficha_blanca_str(self):
        ficha = Ficha("blanco",7)
        self.assertEqual(str(ficha), "blanco en 7")

    def test_ficha_negra_str(self):
        ficha = Ficha("negro",9)
        self.assertEqual(str(ficha), "negro en 9")

    def test_dos_fichas_blancas_mismo_color(self):
        ficha1 = Ficha("blanco",11)
        ficha2 = Ficha("blanco",11)
        self.assertEqual(str(ficha1), str(ficha2))

    def test_dos_fichas_diferentes_colores(self):
        ficha_blanca = Ficha("blanco",23)
        ficha_negra = Ficha("negro",22)
        self.assertNotEqual(ficha_blanca, ficha_negra)

    def test_str_method_blanca(self):
        ficha = Ficha("blanco",4)
        self.assertEqual(ficha.__str__(), "blanco en 4")

    def test_str_method_negra(self):
        ficha = Ficha("negro" , 6)
        self.assertEqual(ficha.__str__(), "negro en 6")

    def test_get_ficha_blanca(self):
        ficha = Ficha("blanco", 5)
        self.assertEqual(ficha.get_ficha(), "blanco")

    def test_get_ficha_negra(self):
        ficha = Ficha("negro", 10)
        self.assertEqual(ficha.get_ficha(), "negro")

    def test_get_movimiento_posicion_inicial(self):
        ficha = Ficha("blanco", 0)
        self.assertEqual(ficha.get_movimiento(), 0)

    def test_get_movimiento_posicion_media(self):
        ficha = Ficha("negro", 12)
        self.assertEqual(ficha.get_movimiento(), 12)

    def test_get_movimiento_posicion_final(self):
        ficha = Ficha("blanco", 23)
        self.assertEqual(ficha.get_movimiento(), 23)

    def test_adentro_almacen_true(self):
        ficha = Ficha("blanco", -1)
        self.assertTrue(ficha.adentro_almacen())

    def test_adentro_almacen_false_posicion_cero(self):
        ficha = Ficha("negro", 0)
        self.assertFalse(ficha.adentro_almacen())

    def test_adentro_almacen_false_posicion_normal(self):
        ficha = Ficha("blanco", 10)
        self.assertFalse(ficha.adentro_almacen())

if __name__ == '__main__':
    unittest.main()