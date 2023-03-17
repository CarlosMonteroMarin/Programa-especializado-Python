frutas = {"manzana","naranja", "manzana", "pera","naranja","banana", "kiwi"}  #crea un conjunto sin elementos repetidos

"pera" in frutas #comprueba si la palabra "pera" esta en la lista y te devuelve True si lo está
"herba" in frutas

#conjunto vacio
set()

#otra forma de crear conjuntos
a= set ("abracadabra") #crea un conjunto del string, la separa por letras y no pone las repetidas
b= set ("alacazam")

#operaciones de conjuntos
a - b #letras en a pero no en b
a | b #letras en a o en b o en ambas
a & b #letras en a y en b
a ^ b #letras en a o b pero no en ambos

#comprension de conjuntos 
a = {x for x in "abracadabra" if x not in "abc"}  #imprime todas las letras de "abracadabra que no sean "abc" y las que estan repetidas