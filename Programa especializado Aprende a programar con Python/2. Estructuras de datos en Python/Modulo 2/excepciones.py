t =1/0

try:
    t= 1/0
except ZeroDivisionError:
    print("Divisioón por cero")


def find (elemento, lista):
    #Devuelve el indice donde se ecuentra el elemento de la lista. Si no lo encuentra devuelve-1

    index = 0
    while True:
        try: 
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index +=1

#ejemplos de find
find (4, [2,3,4,5])
find (1, [2,3,4,5])

#----------------------------------------------------------------

def divide (x, y): 
    #Divide dos números
    try:
        result = x/y
    except ZeroDivisionError:
        print("Divisón por cero!")
    else:
        print("El resultado es ",result)
    finally:
        print("Ejecutando la clausula finally. siempre aparece")


#Ejemplos de divide
divide (2,1)
divide (2,0)