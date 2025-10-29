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

if __name__ == '__main__':
    unittest.main()