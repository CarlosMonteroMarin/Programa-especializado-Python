nombre = "Agustin"

lista = list(nombre) #genera una lista con todas las letras de agustin

#El indexado funciona de igual manera
nombre[0]
lista[0]

#El slicing funciona de igual manera
nombre[:4]
lista[:4]

#La funcion len funciona de igual manera
len(nombre)
len(lista)

#el in funciona en ambas
"A" in nombre
"A" in lista

#el not in funciona en ambas
"z" not in nombre #si la z no esta en el nombre devuelve True
"z" not in lista

#Los string tambien se pueden recorrer con un for
for letra in nombre:
    print(letra) #imprime todo el nombre letra por letra

#los strings son inmutales
lista[2] = "o"
nombre[2] = "o" #TYpeError

"Hola" + nombre
nombre + "!!"
nombre[:2] + "o" + nombre [3:]