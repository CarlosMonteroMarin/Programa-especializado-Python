import json

#serielizar un objeto
json.dumps([1,2,3])

#deserializar un objeto
json.loads('[1,2,3]')

#escribir como json directamente a un archivo
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo_json_ejemplo.txt','w') as a_file:
    json.dump([1,2,3,4], a_file)

#leer un json directamente desde un archivo
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/archivo_json_ejemplo.txt','r') as a_file:
    a_list = json.load (a_file)