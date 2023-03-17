s1 = "Prueba"

#Devuelve el numero de ocurrencias de una subcadena de texto en toda la cadena o en un rango
s1.count('a')

#Indica si la cadena de texto empieza con la subcadena pasada como parametro 
s1.startswith('a')

#indica si la cadena de texto termina con la subcadena pasada como parametro
s1.endswith('a')

#busca la subcadena pasada como parametro en la cadena de texto
s1.find('ue')

#similar a find solo que al no encontrar la subcadena levanta una excepcion de tipo valueerror
s1.index('a')

#igual al find solo que no devuelce la primera ocurrencia sino la ultima.
s1.rfind()

#similar a rfind solo que al no econtrar la subcadena levanta una excepcion de tipo valueerror
s1.rindex()

#indica si todos los caracteres de la cadena de texto son decimales.
s1.isdecimal()

#indica si todos los carateres de la cadena de texto son digitos
s1.isdigit()

#indica si todos los caracteres de la cadena de texto son minusculas
s1.islower()

#indica si todos los caracteres de la cadena son mayusculas
s1.isupper()

#indica si la cadena de texto esta con las mayusculas y minusculas al estilo de un titulo "The New York Times"
s1.istitle()

#indica si a cadena de textos son todos espacios
s1.isspace()

#idnica si la cadena de texto esta compuesta por todos caracteres alfabeticos
s1.isalpha()

#indica si la caden ade texto esta compuesta por todos caracteres alfanumericos
s1.isalnum()
