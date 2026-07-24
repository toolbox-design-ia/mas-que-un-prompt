import unittest
from calculos import porcentaje

class TestPorcentaje(unittest.TestCase):
    def test_porcentaje_normal(self):
        self.assertEqual(porcentaje(25, 100), 25.0)

    def test_porcentaje_cero_total(self):
        self.assertEqual(porcentaje(5, 0), 0)

    def test_porcentaje_redondeo(self):
        self.assertEqual(porcentaje(1, 3), 33.33)

if __name__ == "__main__":
    unittest.main()
