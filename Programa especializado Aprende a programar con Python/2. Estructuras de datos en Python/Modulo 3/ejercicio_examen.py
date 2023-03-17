[x for x in range(1, 101) if x % 2 == 0]

[x for x in range(101) if x % 2 == 0]    

[x for x in range(1, 101) if x % 2 != 0]    

[x for x in range(1, 100) if x % 2 == 0]

#------------------------

a_list = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)] 

a_list.sort(key=lambda x: x[0]+x[1])    


print(a_list)

#-----------------------------

a = {1, 2, 3, 4, 5} 

b = {3, 7, 8, 9, 1}

print(a^b)