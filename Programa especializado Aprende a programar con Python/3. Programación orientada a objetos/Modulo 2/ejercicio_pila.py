
# Pila
# En esta instancia, te propongo realizar una actividad práctica.  

# El objetivo de esta actividad es que puedas enfrentarte a un problema acotado, donde puedas ir incorporando los conceptos vistos, tratando de resolver el problema pensando en objetos.

# Al finalizar el ejercicio, podes ver el siguiente video donde se expone la explicación de una posible solución. Te recomiendo hacer este ejercicio antes de ver el video o al menos pensarlo un tiempo. De esta manera, la solución propuesta te ayudará mucho más a comprender los conceptos vistos en clase.

# ¡Comencemos!

# -        top: devuelve el elemento que está en el tope de la pila.

# -        push: Apila un elemento nuevo.

# -        pop: Desapila un elemento y lo devuelve. Levantar una excepción si se hace pop de una pila vacía.

# -        len: Devuelve la cantidad de elementos de la pila.

# -        is_empty: Indica si la pila está vacía.


#Clase para generar una expeccion personalizada
class EmptyStack(Exception):
    pass



class Stack(object):

    def __init__(self):
        self.head = StackBase()

    def top(self):
        return self.head


    def push(self, value):
        self.head = self.head.push(value)

    def pop(self):
        old_head = self.head
        self.head = self.head.pop()
        return old_head


    def len(self):
        return self.head.len()


    def is_empty(self):
        return self.head.is_empty()
    

class StackBase(object):
        def push(self, value):
            return StackItem(parent=self, value= value)
        
        def pop(self):
            raise EmptyStack("Pila vacia")
        
        def len(self):
            return 0 
        
        def is_empty(self):
            return True
        
        def __repr__(self):
            return 'Base de la pila'
        
class StackItem(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
    
    def push(self, value):
        return StackItem(parent=self, value=value)
    
    def pop(self):
        return self.parent
    
    def len(self):
        return self.parent.len() +1
    
    def ins_empty(self):
        return False
    
    def __repr__(self):
        return str(self.value)
    
stack = Stack() 