import math

def raiz_cuadrada (number):
    if number < 0:
        raise ValueError("Número negativo.")
    return math.sqrt(number)