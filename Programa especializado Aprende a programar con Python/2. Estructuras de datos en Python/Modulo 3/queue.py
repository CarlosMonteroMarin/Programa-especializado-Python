from collections import deque

#listas como colas NO EFICIENTE
queue =[1,2,3]

queue.append(4)
queue.append(5)

queue.pop(0) #quitamos el primer elemento, se quita pero todos los demas elementos se tienen que mover de posicion y no es eficiente
queue.pop(0)

#colas implementadas EFICIENTEMENTE en la libreria estandar
queue = deque ([1,2,3])

#Agrego los elementos
queue.append(4)
queue.append(5)

#saco los elementos
queue.popleft()
queue.popleft() 