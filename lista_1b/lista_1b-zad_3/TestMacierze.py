import unittest
import numpy as np
import macierze


class TestMacierze(unittest.TestCase):

    def test_dodaj_macierze_wymiary(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6]])
        with self.assertRaises(ValueError):
            macierze.dodaj_macierze(A, B)

    def test_odejmij_macierze_wymiary(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6]])
        with self.assertRaises(ValueError):
            macierze.odejmij_macierze(A, B)

    def test_pomnoz_macierze_wymiary(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8], [9, 10]])
        with self.assertRaises(ValueError):
            macierze.pomnoz_macierze(A, B)


if __name__ == '__main__':
    unittest.main()
