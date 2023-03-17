precios = {"manzana": 3.5, "banana":4.5, "kiwi":6.0,"pera":3.75}

#vistas de diccionarios
claves = precios.keys() #imprime las keys del diccionario (dict_keys(['manzana', 'banana', 'kiwi', 'pera']))

valores = precios.values() #imprime los items del diccionario (dict_values([3.5, 4.5, 6.0, 3.75]))

items = precios.items() #imprime los items del diccionario (dict_items([('manzana', 3.5), ('banana', 4.5), ('kiwi', 6.0), ('pera', 3.75)]))

precios["melon"] = 5.5 #añadir elemento melon al diccionario

#Iteracion de diccionarios
for fruta, precio in precios.items():
    print ("Precio de",fruta,": $",precio)
    #Precio de manzana : $ 3.5
    #Precio de banana : $ 4.5
    #Precio de kiwi : $ 6.0
    #Precio de pera : $ 3.75

