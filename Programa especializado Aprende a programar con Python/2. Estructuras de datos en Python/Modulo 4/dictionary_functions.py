precios = {"manzana":3.5,"banana":4.5, "kiwi":6.0, "pera":3.75}

#Cantidad de elementos clave-valor
len(precios)

#Obtiene el valor de la clave indicada, se puede inidcar un default si no existe.
precios.get("manzana")  
precios.get("melon")
precios.get("melon",0.00)

#Si existe devuelve elvalor, sino lo crea con el valor default o si no se indica el default con None.
precios.setdefault("banana")
precios.setdefault("sandia",6.7)  #si no esta el registro lo crea

#Actualizacion de un diccionario
precios.update({"banana":4.0,"durazno":5.5})
precios.update([{"durazno", 5,5}])

#Me devuelve una vista con las claves del diccionario
precios.keys()

#Me devuelve una vista con los valores del diccionario.
precios.vaules()

#Me devuelve una vista con los items del diccionario
precios.items()

#Quita el elemento de la clave indicada, se puede poner un default si no existe
precios.pop("manzana")
precios.pop("melon",0.00)
precios.pop("melon")

#Saca un elemento siguiendo el orden: LIFO
precios.popitem() #quita elementos last in first out (el ultimo que entra primero que sale)

#Copia superficial de los diccionarios
copia_precios = precios.copy()

#Borrar todos los elementos
precios.clear() 