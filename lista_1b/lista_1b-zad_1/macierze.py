import numpy as np


def dodaj_macierze(A, B):
    return np.add(A, B)


def odejmij_macierze(A, B):
    return np.subtract(A, B)


def pomnoz_macierze(A, B):
    return np.dot(A, B)


def transponuj_macierz(A):
    return np.transpose(A)
