a_list = [3, 7.5, "hola",7j +5, [1,2]]

#acceso mediante indexación
a_list[0] # 3
a_list[2] # "hola" 
a_list[-1] # [1,2] te imprime el ulitmo elemento

#slicing 
a_list[1:] # [7.5. "hola", 7j + 5, [1,2]] te imprime una lista de una lista del elemento 1 incluido hasta el final
a_list[1:2] # [7.5] te imprime una lista de una lista del elemento 1 incluido hasta el 2 no incluido
a_list[1:3] # [7.5, "hola"] te imprime una lista de una lista del elemento 1 incluido hasta el 3 no incluido
a_list[:2] # [3, 7.5] te imprime una lista de una lista del elemento 0 incluido hasta el 2 no incluido
a_list[:]   #[3, 7.5, "hola", 7j + 5, [1,2]] te imprime una lista de una lista de todo


#Algunas funciones

#Devuelve la cantidad de elementos de la lista
len(a_list) # 5  

#Agrega un elemento al final de la lista
a_list.append(2) 

#Exriende la lista ocn los elementos de otra lista
a_list.extend([3,4]) #añade varios elementos a la vex

#Inserta un elemento en una posicion determinada
a_list.insert(4, "Intercalado") #añade la palabra "Intercalado" en la posicion 4
a_list.insert(12, "Fuera de rango")
a_list.insert(-1, "Hacia altras")

#cuenta cuantos elementos hay  que coincidan con el argumento
a_list.count(3) # hay 2 numeros 3 en la lista

#elimina el primer elemento que encuentra el pasado como parametro
a_list.remove(3)

#hace una copia superficial de la lista
a_list_copy = a_list.copy()

#imprime el utimo elemento de la lista
a_list.pop() #

#imprime el tercer elemento de la lista
a_list.pop(3) 

#borra todos los elementos de la lista
a_list.clear()