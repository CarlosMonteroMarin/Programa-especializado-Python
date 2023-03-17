import math
 

factorial_10 = str(math.factorial(10))
 
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo_examen.txt', 'w') as a_file: 
    a_file.write(factorial_10)