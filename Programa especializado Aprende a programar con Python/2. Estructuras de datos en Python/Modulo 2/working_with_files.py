#abrir arvhivo
a_file = open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r')

#leer todo el contenido del archivo
a_file.read()

#cerrar archivo
a_file.close()

#abrir un archivo como un context manager utilizando la sentencia with.
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo-ejemplo.txt', 'r') as a_file:
    a_file.read()