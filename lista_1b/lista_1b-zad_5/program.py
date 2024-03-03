import math
import trigonometria

# Przykładowe kąty
katy_w_stopniach = [0, 30, 45, 60, 90]
katy_w_radianach = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2]

print("Wartości trygonometryczne dla kątów w stopniach:")
for kat in katy_w_stopniach:
    print(f"Kat {kat} stopni - sin: {trigonometria.sin(kat)}, cos: {trigonometria.cos(kat)}, tan: {trigonometria.tan(kat)}, cot: {trigonometria.cot(kat)}")

print("\nWartości trygonometryczne dla kątów w radianach:")
for kat in katy_w_radianach:
    print(f"Kat {kat} radianów - sin: {trigonometria.sin(kat, False)}, cos: {trigonometria.cos(kat, False)}, tan: {trigonometria.tan(kat, False)}, cot: {trigonometria.cot(kat, False)}")
