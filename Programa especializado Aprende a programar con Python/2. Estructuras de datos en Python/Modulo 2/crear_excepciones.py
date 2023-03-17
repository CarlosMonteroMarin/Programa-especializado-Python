import math

class NegativeNumer (Exception):
    #Excewpcion de tipo numero negativo
    pass

def raiz_cuadrada (number):
    if number < 0:
        raise NegativeNumer ("Número negativo.")
    return math.sqrt(number)
