def es_primo(numero):

    resultado = True
    suma =0
    for divisor in range(2, numero):
        suma+=1
        print(suma)
        if (numero % divisor) == 0:
            resultado = False

            break

    return resultado 


print(es_primo(13))

#------------------------

s = 0

for n in range(1, 10):

     if n % 7 == 0:

         break

     s += n

print(s)


#-----------------------

s = 0

for n in range(1, 10):

     if n % 2 == 0:

         continue

     s += n

print(s)

#-------------------------
s = 0

for n in range(1, 10):

     if n % 11 == 0:

         break

     s += n

else:

     s += 10

print(s)

#--------------------------------

s = 0

for n in range(1, 10):

     if n % 2 == 0:

         pass

     s += n

print (s)


#--------------------------


s = 0

for n in range(1, 10):

     if n % 2 != 0:

       continue

     s += n

else:

      s += 5

print (s)