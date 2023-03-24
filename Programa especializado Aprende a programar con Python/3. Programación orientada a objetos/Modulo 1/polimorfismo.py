import math
#Los enteros y los decimales son polimorficos con respecto a la suma
4 + 6
4.5 +5.7

#Los enteros y los decimales son polimorfismos con respecto a la resta 
4 - 3
3.5 - 4.0

#Los enteros y los decimales son polimorficos con respecto a la multiplicacion
4 * 5
2.5 * 5.0

#Los enteros  y los decimales son polmorficos con respecto a la division
4 / 5
5.6 / 3.2

#Pero por ejemplo los enteros no son polimorificos con respecto a la funcion factorial
math.factorial(4)  #24
math.factorial(4.5) #ValueError

class ClassA (object):
    def m1(self,a,b):
        return a + b