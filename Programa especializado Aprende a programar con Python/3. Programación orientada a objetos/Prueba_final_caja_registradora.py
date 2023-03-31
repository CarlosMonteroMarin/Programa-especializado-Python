#REQUISITOS
# - El sistema debe poder escanea un producto
# - Agregar el producto al listado de productos comprados para el cliente.
# - Debe mostrar el subtotal.
# - El cajero debe poder finalizar la compra y se tienen que aplicar los descuentos correspondientes.
# - Precio total de la compra con descuentos aplicados.
# - Sistema tiene que indicar el cambio para el cliente.


#
class Caja(object):
    #inicializamos unas variables
    def __init__(self):
        self.lista_compra=[]
        self.lista_pesos=[]
        self.catalogo = Catalogo()
        self.total = 0

    #Método para la bienvenida y registro de los productos de la compra 
    def listado_compra(self):
        print("-------------FRUTERIAS MONTERO-------------")
        print("Siguiente cliente...")
        print("LISTADO DE LOS PRODUCTOS: ", self.catalogo.productos)
        print("Introduce los productos: (x para finalizar) ")

        while True:
            producto = input("Producto: ").lower()
            caja.comprobar_producto(producto)
            if producto == "x":
                return False
            else:
                if caja.comprobar_producto(producto) == True:
                    peso = input("Peso(kg): ")
                    self.lista_compra.append(producto)
                    self.lista_pesos.append(peso)
                    print("Lista de",len(self.lista_compra), "productos selecionados: ",self.lista_compra)

                else:
                    print("PRODUCTO NO DISPONIBLE, NO SE LE COBRARÁ.")


    #Método para comprobar que exista el producto introducido 
    def comprobar_producto(self, producto):
        acum = 0
        while acum < len(self.catalogo.productos):
            if producto == self.catalogo.productos[acum]:
                return True
            else: 
                acum +=1
        return False
    

    #Método para calcular el subtotal de la compra sin los descuentos 
    def calcular_subtotal_total(self):
        acum = 0
        acum2 = 0
        subtotal_compra = 0
        print("..................Desglose....................")
        #while para recorrer la lista de la compra introducida
        while acum2 < len(self.lista_compra):      
            #while para recorrer la lista de productos de la base de datos      
            while acum < len(self.catalogo.productos):
                #condicional para comparar el producto comprado con el de la base de datos 
                if self.lista_compra[acum2] == self.catalogo.productos[acum]:
                    #multiplicamos el precio del producto por el peso que compra, y vamos sumando en la variable "subtotal_compra" el total
                    precio_producto_sd= float (self.catalogo.precios[acum]) * float(self.lista_pesos[acum2])
                    subtotal_compra = subtotal_compra + precio_producto_sd
                    
                    #llamamos al metodo "calcular_descuentos()" y le pasamos la info del producto que estamos trabajando y nos retornara el
                    # precio total del producto con el descuento aplicado y lo vamos sumando a la variable "self.total" para obtener el total
                    precio_producto_cd = caja.calcular_descuentos(precio_producto_sd, self.catalogo.descuentos[acum], self.lista_pesos[acum2], self.lista_compra[acum2])
                    self.total = self.total + precio_producto_cd
                    acum = 0
                    break
                else:
                    acum +=1
            acum2 += 1
        print("..............................................")
        print("SUBTOTAL SIN DESCUENTOS APLICADOS:", round(subtotal_compra,2),"€")
        print("TOTAL CON DESCUENTOS APLICADOS:",round(self.total, 2),"€")
        print("..............................................")


    #Método para calcular los descuentos por cada producto
    def calcular_descuentos(self, precio_producto, descuento, peso, producto):
        #obtenemos la informacion del producto y extramos el precio del producto con el descuento aplicado
        precio_total_cd = precio_producto * (descuento /100)
        precio_total_cd = precio_producto - precio_total_cd
        print("-", producto,"*",peso,"kg......descuento de",descuento,"%:",round(precio_total_cd, 2),"€")

        #retorna el precio final del producto 
        return precio_total_cd



    #Método para calcular el cambio de la compra, pide la cantidad de dinero que da el cliente y lo resta al total de la compra.
    def pago_compra(self):
        pago = float(input("¿Cuanto paga el cliente? "))
        vuelta = pago - self.total
        print("Al cliente se le devuelve:",round(vuelta, 2), "€")

        

#Creamos una clase que haga de base de datos
class Catalogo(object):
    def __init__(self):
        #Estructura objeto: nombre, precio, descuento.
        self.productos = ['banana','manzana','melon','judias','limon','naranja']
        self.precios = [3.0 , 2.0 , 1.75 , 2.22 , 0.9 , 1.25]
        self.descuentos = [0 ,7 , 20 , 5 , 40 , 35]

#inicializamos un objeto caja y llamamos a los metodos
caja = Caja()
caja.listado_compra()
caja.calcular_subtotal_total()
caja.pago_compra()
