#¿Cuál es el resultado de sumar los primeros 50 números pares? (Desde el 2 inclusive hasta el 100 inclusive).

suma =0
for n in range(101):
    if n % 2 == 0:
        print(n)
        suma = suma + n
    n += 1

print ("Total: ",suma)

#EJERCICIO EXAMEN
s = 0
for n in range(10):
    s+=n
print(s)