#crear un diccionario para un tienda, en los cuales se agregan
#Los prductos se ingresan por teclado
#Tienda->Productos:id,Nombres,Precio,Cantidad
#Solamente acepte ingresar 20 productos

#Crearemos nuestro diccionario vacio
tienda={} #Diccionario
tienda=() #Tuplas
tienda=[] #Listas
#Solicitar al usuario que ingrese los 20 productos
for i in range(1,21):
    #Verficacion de los 20 productos
    if len(tienda)==20:
        print("ya se agregaron los 20 productos a la tienda")
    break
#Solicitamos el ingreso de nuevos productos
print("Ingrese los datos del producto",i,"o precione enter para salir")
id=input("ID")
#Si el usuario presiona enter sin agregar nada al id salimos del bucle
#if id=="":
    ##break
nombre=input("Ingrese el Nombre del producto")
precio=float(input("Ingrese el Precio del Producto"))
cantidad=int(input("Ingrese la Cantidad del Producto"))


#Agregamos los productos ingresados al diccionario
tienda[id]={":nombre":nombre,"Precio":precio,"cantida":cantidad}

#Imprimimos en panatalla el diccionario Completo
print("Los productos de la tienda son: ")
for id,producto in tienda.items():
    print("ID:{id}-"- Nombre":{producto['nombre']} - "- Precio": {producto['Precio']} - Cantidad:{Producto['cantidad']})