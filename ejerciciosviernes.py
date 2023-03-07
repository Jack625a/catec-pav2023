#crear un diccionario para una tienda
# en los cuales se agregaran productos
# los productos se ingresaran por teclado 
#tiend--> productos= id, nombre, precio y cantidad
# que solo nos permita ingresar 20 productos 
# creando diccionario vacio
#tienda={} #diccionario
#tienda=()   #tupla   
#tienda=[]   #lista
tienda={}
#solicitar al usuario que ingrese los 20 productos 
for i in range(1,21):
#verificacion de los 20 productos 
    if len(tienda)==20:
        print("ya llego al maximo de los productos: ")
        break
#solicitar que ingrese los productos
    print("ingrese los nombres del producto", i,"o precione enter para salir ")
    id=input("ID")
#si el usuario presiona enter sin agregar nada al id salimos del bucle
    if id=="":
    break

nombre=input("ingrese el nombre del producto")
precio=float(input("ingrese el precio del producto"))
cantidad=int(input("ingrese la cantidad de producto"))

#agregar estas variables al diccionario 
tienda[id]={"nombre":nombre,"precio":precio,"cantidad":cantidad}

#mimprimir en pantalla el diccionario completo
print("los productos de la tienda son: ")
for id, producto in tienda.items():
    print("ID:{id} - nombre: {producto['nombre']} - precio: {producto['precio']} - cantidad: {producto['cantidad']}")







