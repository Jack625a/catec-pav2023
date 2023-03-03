#crear un diccionario de una tienda
#los productos se ingresan por teclado
#tienda-productos:id, Nombre, precio, Cantidad
#solamente acepta ingresar 20 productos

#creamos nuestro diccionario vacio.
tienda={} #diccionario
#solicitar los 20 productos
for i in range(1,21):
    #verificacion que de los 20 productos
    if len(tienda) ==20:
        print ("ya se agregaron los 20 productos a la tienda ")
        break
    #solicitar que ingrese el rpoducto, si no esta lleno el inventario
    print("ingrese los datos del producto ",i, "o presione enter para salir")
    id=input("id: ")
    #si el usuario preciona enter sin agregar el producto 
    if id=="":
        print("saliendo del registro del producto")
        break

    nombre=input("ingrese el nombre del producto: ")
    precio=float(input("ingrese el precio del producto: "))
    cantidad=int(input("ingrese la cantidad del producto: "))

#agregamos los productos ingresados al diccionario
tienda[id]={"nombre":nombre,"precio":precio,"cantidad":cantidad}
#imprimimos en pantalla el diccionario completo
print("los productos de la tienda son: ")
for id, producto in tienda.items():
    print("*","id":{id}, "- nombre:"{producto['nombre']} "- precio:" {producto['precio']} "- cantidad:" {producto['cantidad']}")
