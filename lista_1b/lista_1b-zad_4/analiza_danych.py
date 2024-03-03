def sortuj_dane(dane, klucz):
    return sorted(dane, key=lambda x: x[klucz])

def filtruj_dane(dane, klucz, wartosc):
    return [element for element in dane if element[klucz] == wartosc]

def grupuj_dane(dane, klucz):
    grupy = {}
    for element in dane:
        grupy.setdefault(element[klucz], []).append(element)
    return grupy
