import numpy as np
import macierze

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

wynik_dodawania = macierze.dodaj_macierze(A, B)
print("Wynik dodawania macierzy A i B:")
print(wynik_dodawania)

wynik_odejmowania = macierze.odejmij_macierze(A, B)
print("\nWynik odejmowania macierzy B od A:")
print(wynik_odejmowania)

wynik_mnozenia = macierze.pomnoz_macierze(A, B)
print("\nWynik mnożenia macierzy A przez B:")
print(wynik_mnozenia)

wynik_transpozycji = macierze.transponuj_macierz(A)
print("\nMacierz A po transpozycji:")
print(wynik_transpozycji)
