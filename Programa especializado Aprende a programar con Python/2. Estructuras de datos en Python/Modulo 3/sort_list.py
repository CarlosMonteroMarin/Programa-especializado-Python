a_list = [3, 1, 2 ,9, 5, 4, 7, 8, 6] #creamos lista

#ordena los elementos de la lista in situ
a_list.sort() #ordenamos la lista en ascendente
a_list.sort(recerse=True) #ordenamos la lista descendente

a_list = [(1, 9),(1,3),(1,4),(1,2)]
a_list.sort(key=lambda x: x[1])

#revierte los elementos de la lista in situ
a_list = [3,1,2,9,5,4,7,8,6] #creamos lista
a_list.reverse() #ordena la lista del reves a como estaba escrita


#ordena los elementos y crea una lista nueva
a_list = [3,1,2,9,5,4,7,8,6] #creamos una lista
sorted(a_list) #CREA UNA LISTA NUEVA y la ordena de manera ascendente
sorted(a_list, reverse=True) #CREA UNA LISTA NUEVA y la ordena de manera descendente

a_list = [(1, 9),(1,3),(1,4),(1,2)]
sorted(a_list, key=lambda x: x[1])