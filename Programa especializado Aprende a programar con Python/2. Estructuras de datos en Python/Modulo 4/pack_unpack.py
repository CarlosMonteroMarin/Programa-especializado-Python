#Empaquetado de tuplas
a = 30 #asignamos las variables
b = "T"
C = "A"

tupla = a,b,C #agrupamos o empaquetamos varias variables en una tupla

#desempaquetado
x,y,z = tupla #se puede desempaquetar por orden 

#errores por distintos tamaños a desempaquetar
x,y = tupla
w,x,y,z = tupla