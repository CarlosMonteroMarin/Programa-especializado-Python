#Lista de cuadrados
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

#lista por comprension
cuadrados_2 = [x**2 for x in range(10)]

#cuadrados utilizando la funcion map
cuadrados_3 = list (map(lambda x: x**2, range(10)))

a_list = [-4, -2, 0 , 2, 4]

#lista por comprension con los numeros positivos de a_list
positivos = [x for x in a_list if x >= 0]

#lista con los numeros positivos de a_list utilizando la funcion filter
positivos_2 = list(filter(lambda x: x > 0, a_list))

#pares numero y su cadrado
[(x,x ** 2) for x in range(6)] 

#lista de pares combinados
pares = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]