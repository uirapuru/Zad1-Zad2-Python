import czas

sekundy = 3600
minuty = czas.sekundy_na_minuty(sekundy)
print(f"{sekundy} sekund to {minuty} minut.")

minuty = 150
godziny = czas.minuty_na_godziny(minuty)
print(f"{minuty} minut to {godziny} godzin.")

godziny = 48
dni = czas.godziny_na_dni(godziny)
print(f"{godziny} godzin to {dni} dni.")

dni = 2
godziny = czas.dni_na_godziny(dni)
print(f"{dni} dni to {godziny} godzin.")

godziny = 2
minuty = czas.godziny_na_minuty(godziny)
print(f"{godziny} godzin to {minuty} minut.")

minuty = 2
sekundy = czas.minuty_na_sekundy(minuty)
print(f"{minuty} minut to {sekundy} sekund.")
