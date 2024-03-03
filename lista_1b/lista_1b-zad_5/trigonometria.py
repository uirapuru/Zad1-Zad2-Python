import math

def sin(kat, w_stopniach=True):
    if w_stopniach:
        kat = math.radians(kat)
    return math.sin(kat)

def cos(kat, w_stopniach=True):
    if w_stopniach:
        kat = math.radians(kat)
    return math.cos(kat)

def tan(kat, w_stopniach=True):
    if w_stopniach:
        kat = math.radians(kat)
    return math.tan(kat)

def cot(kat, w_stopniach=True):
    if w_stopniach:
        kat = math.radians(kat)
    if math.tan(kat) == 0:
        return None
    return 1 / math.tan(kat)
