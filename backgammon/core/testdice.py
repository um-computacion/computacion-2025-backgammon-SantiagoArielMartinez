import unittest
from dice import dados

class TestDados(unittest.TestCase):

    def test_tirar_dado(self):
        dado1 = dados()
        dado1.tirar_dado()
        self.assertIn(dado1.get_valor(), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
