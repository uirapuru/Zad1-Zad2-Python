import numpy as np

def dodaj_macierze(A, B):
    if A.shape != B.shape:
        raise ValueError("Macierze muszą mieć takie same wymiary do dodawania.")
    return np.add(A, B)

def odejmij_macierze(A, B):
    if A.shape != B.shape:
        raise ValueError("Macierze muszą mieć takie same wymiary do odejmowania.")
    return np.subtract(A, B)

def pomnoz_macierze(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy do mnożenia.")
    return np.dot(A, B)

def transponuj_macierz(A):
    return np.transpose(A)