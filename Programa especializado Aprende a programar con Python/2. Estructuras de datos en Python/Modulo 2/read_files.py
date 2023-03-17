#La funcion read lee todo el contenido del arhivo
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    print(a_file.read())

#la funcion readline lee la linea acutal del archivo
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    print(a_file.readline())

#la funcion readlines lee las lineas del archivo y las guarda en una lista
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    print(a_file.readlines())

#la funcion list genera una lista con loas lineas del arvhivo ( lo mismo que la funcion readlines)
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    print(list(a_file))

#el for recorre linea a linea.
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    for line in a_file:
        print(line)