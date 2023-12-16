# Fecha: 10/12/2023
# Autor: Adrian Alfaro Hernandez
# Descripcion: Programa de facturacion, permite ingreso de productos, creacion de factura, generacion de reporte

import random as rd

# Recursos del programa ---------------------------------------------------------------------------------------- 
# Incluidos en el mismo archivo para facilitar la prueba, de lo contrario consideraria pasarlo a un modulo

class Producto:
    cantidad_max_productos = 1000 #Limita la cantidad de codigos posibles, actualmente del 1 a 1000
    lista_codigos = []

    def __init__(self, codigo="default", nombre="default", precio_unitario="default"):
        self.nombre = nombre
        self.codigo = codigo
        self.precio_unitario = precio_unitario

    def ingreso_producto(self):
        self.nombre = input("Por favor ingrese el nombre del producto: ")
        self.precio_unitario = float(input(f"Por favor ingrese el precio unitario de {self.nombre}: "))

        falta_codigo_prod = True

        while falta_codigo_prod:

            modo = input("Desea crear el codigo Manualmente o Automaticamente? (M/A): " ).lower()
        
            if  modo == "m":
                try:
                    codigo = int(input("Por favor ingrese el codigo: ")) 
                except:
                    print("Parece que no ingreso un numero entero, una segunda otra oportunidad")
                    codigo = int(input("Por favor ingrese el codigo: "))

                if codigo not in Producto.lista_codigos:
                    self.codigo = codigo
                    falta_codigo_prod = False
            elif modo =="a":
                codigo = rd.randint(1, Producto.cantidad_max_productos)
                print(f"Codigo:  {codigo}")
                if codigo not in Producto.lista_codigos:
                    self.codigo = codigo
                    falta_codigo_prod = False
            else:
                print(f"Por favor intente de nuevo, {modo} no es una de las opciones")

        Producto.lista_codigos.append(codigo)
        

    def describir_producto(self):
        print(f'Producto: {self.nombre} | Codigo: {self.codigo} | Precio Unitario: {self.precio_unitario}')

def mostrar_productos():
    print("\nLista de productos\n")
    lista_productos = productos.keys()
    for key in lista_productos:
        productos[key].describir_producto()

class Cliente:
    def __init__(self, nombre, id):
        self.id = id
        self.nombre = nombre
        self.carrito = {}

    def agregar_prod(self, item, cantidad):
        self.carrito[item] = cantidad
    
    def remover_prod(self): # No se ha testeado y por lo tanto no se ofrece como opcion al usuario
        item = input("Por favor ingrese el codigo del producto que quiere remover")
        self.carrito.pop(item)

    def mostrar_cliente(self):
        print(f'Cliente: {self.nombre} Client_id: {self.id} Carrito: {self.carrito}')

menu = '''
Actualmente contamos con las siguientes opciones:
      
    1.Ingresar Producto
    2.Mostrar Productos
    3.Nueva factura
    4.Generar Reporte
    5.Salir del programa

    Elijo la opcion: '''

def reporte_ventas():
    print("REPORTE DE VENTAS".center(64))
    cantidad_clientes = 0
    total_vendido = 0      
    for cliente in clientes:
                print(f"\nId Cliente: {cliente.id}  Nombre Cliente: {cliente.nombre}")
                print(" --------------------------------------------------------------- ")
                print("|   Producto   |   Cantidad   |   Precio unitario   |   Total   |") 
                print(" --------------------------------------------------------------- ")
    
                lista_carrito = cliente.carrito.keys()
                total_factura = 0
                for i in lista_carrito:
                    producto = productos[i]
                    precio_u = producto.precio_unitario
                    cantidad = cliente.carrito[i]
                    total_linea = cantidad * precio_u
                    print(f"|{producto.nombre.center(14)}|{str(cantidad).center(14)}|{str(precio_u).center(21)}|{str(total_linea).center(11)}|")
                    total_factura += total_linea
                print(" --------------------------------------------------------------- ")
                print("Total Factura:                                      ", total_factura)
                
    
                cantidad_clientes += 1
                total_vendido += total_factura
    
    print("\nCantidad de clientes: ", cantidad_clientes)
    print("Total Vendido: ", total_vendido) 



# Comienzo del programa principal --------------------------------------------------------------------------------------
print("Bienvenido al programa de facturacion")

productos = {}
clientes = []
continuar = "continuar"
codigo_clientes = []

while continuar == "continuar":
    opcion = input(menu).lower()
    print(f"\nUsted eligio: {opcion}\n\n")

    if opcion in ["uno", "1"]:
        prod_temp = "nada"
        prod_temp = Producto()
        prod_temp.ingreso_producto()
        productos[prod_temp.codigo] = prod_temp
        mostrar_productos()

    elif opcion in ["dos", "2"]:
        mostrar_productos()

    elif opcion in ["tres", "3"]:
        cliente_temp = "vacio"
        nombre_temp = input("Por favor ingrese el nombre del cliente: ").capitalize()
        codigo_temp = input("Por favor ingrese el id del cliente: ")
        while codigo_temp in codigo_clientes:
             print("Ese codigo ya esta ocupado, por favor escoja otro codigo")
             codigo_temp = input("Por favor ingrese el id del cliente: ")
             
        cliente_temp = Cliente(nombre_temp, codigo_temp)
        codigo_clientes.append(codigo_temp)
 
        continuar_factura = True
        continuar_count = 1
        while continuar_factura:
            codigo_temp = int(input(f"\nPor favor escriba el codigo del producto #{continuar_count} : "))
            while codigo_temp not in Producto.lista_codigos:
                 print("Ese producto no existe")
                 mostrar_productos()
                 codigo_temp = int(input(f"\nPor favor escriba el codigo del producto #{continuar_count} : "))
                 
            cliente_temp.agregar_prod(codigo_temp,int(input(f"Por favor ingrese la cantidad de producto #{continuar_count}: ")) )
            continuar_count += 1
            if input("Desea agregar mas productos a la factura?: ").lower() == "no":
                continuar_factura = False
                clientes.append(cliente_temp)
       
    elif opcion in ["cuatro", "4"]:
        reporte_ventas()

    elif opcion in ["cinco", "5", "salir"]:
        continuar = "no"
        print("Saliendo del programa")

    else:
        print(f"{opcion} no es una opcion valida, por favor intente nuevamente")

print("El programa termino exitosamente")

# Notas para la siguiente actualizacion:
# - Refactorizar para mejorar la legibilidad 
# - Agregar opciones para agregar producto o ver productos cuando se escoge un codigo incorrecto
# - Probar e implementar opcion para eliminar productos
# - Crear "memoria a largo plazo" al pasar diccionario de productos y lista de clientes a un archivo permanente (actualmente solo existe en memoria)
# - Probablemente estaria bien poder actualizar precios si tener que eliminar el producto