import random


respuesta = "s"
tiradas = 0
while respuesta == "s":
    tiradas += 1
    print("-------------------------------------------------------------")
    print("---------------Simulador de tiradas de dados-----------------")
    print("--------------------------------------------------Tiradas: ", tiradas)

    dado1= random.randrange(1, 7, 1)
    dado2= random.randrange(1, 7, 1)
    total = dado1 + dado2

    print("El primer dado a sacado el número: ",dado1)
    print("El segundo dado a sacado el número: ",dado2)
    print("La suma de los dos dados a sido de: ",total)

    respuesta = input("¿Quieres volver a tirar? (S/N) ")
    print (respuesta)
   
    if respuesta in ("s, S, SI, si, Si, SÍ, Sí"):
        respuesta = "s"


