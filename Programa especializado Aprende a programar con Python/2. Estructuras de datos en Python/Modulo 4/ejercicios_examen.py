v = 1, 2, 3

x,y = v[1:]

v

z = v[-3]

w = y, x, z

w

#--------------

t1 = (1,2,3)
t2 = (4,5,6)

t1+t2


t3 = (1,2,3)

t3*3

#--------------------
d = {"a": 1, "b":2, "c":3}

d.update({"a":5, "d":4})

del d["b"]

#---------------

precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, "ciruela": 2.45, "durazno": 4.55, "melon": 7.35, "sandia": 9.70, "anana": 11.25}
 

total= (precios["manzana"]*2)+(precios["banana"]*2.5)+(precios["kiwi"]*1)+(precios["pera"]*3)+(precios["ciruela"]*1)+(precios["durazno"]*2)+(precios["melon"]*5)+(precios["sandia"]*10)+(precios["anana"]*3)


#------------

def numeros_pares(n):
   return (x for x in range(n) if x % 2 == 0)


gen = numeros_pares(15)
gen.__next__()
gen.__next__()