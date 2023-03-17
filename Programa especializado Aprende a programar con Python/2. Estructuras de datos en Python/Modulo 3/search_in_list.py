a_list = [1, 2, 3, 4, 5]

#devuelve el indice
a_list.index(4) #busca el elemento 4 y nos indica la posicion en la que la a encontrado.

#lanza una excepcion de tipo ValueError
a_list.index(6)

#opciones indicando una sublista
a_list.index(4,1) #busca el elemento 4 desde la posicion 1
a_list.index(4, 0, 2) #busca el elemento 4 desde la posicion 0 hasta la 2
a_list.index(4, 1, 4) #busca el elemento 4 desde la posicion 1 hasta la 4