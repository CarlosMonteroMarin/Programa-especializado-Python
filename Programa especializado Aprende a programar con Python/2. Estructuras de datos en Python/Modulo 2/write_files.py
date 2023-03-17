#escribir un string en el archivo (REESCRIBE LINEA)
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'w') as a_file: 
    a_file.write("hola mundo")

#escribir muchas lineas en el archivo.
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'w') as a_file: 
    a_file.writelines(['Linea 3\n, pepe amador\n, algo\n'])

#escribir un string en el archivo, agregandolo al final del mismo (AÑADE INFO)
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'a') as a_file: 
    a_file.write("hola mundo")