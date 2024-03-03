import analiza_danych

dane = [
    {"imie": "Jan", "wiek": 25, "miasto": "Warszawa"},
    {"imie": "Anna", "wiek": 30, "miasto": "Kraków"},
    {"imie": "Piotr", "wiek": 20, "miasto": "Warszawa"},
    {"imie": "Katarzyna", "wiek": 22, "miasto": "Gdańsk"}
]

posortowane_po_wieku = analiza_danych.sortuj_dane(dane, "wiek")
print("Posortowane po wieku:")
for osoba in posortowane_po_wieku:
    print(osoba)

filtr_warszawa = analiza_danych.filtruj_dane(dane, "miasto", "Warszawa")
print("\nOsoby z Warszawy:")
for osoba in filtr_warszawa:
    print(osoba)

grupy_miasto = analiza_danych.grupuj_dane(dane, "miasto")
print("\nGrupowanie po mieście:")
for miasto, osoby in grupy_miasto.items():
    print(f"{miasto}: {osoby}")
