#Listas
colores=['rojo','verde','amarillo','negro']
print ("lista de colores:", colores)
print (colores[0])
#Actualizacion de listas
colores[2]='morado'
print ("Lista Nueva:", colores)
colores[1]= 'blanco'
print ("Lista Actualizada:", colores)
#Eliminar elemento de una lista
del colores[1]
print("Lista con valor eliminado:", colores)
#Tuplas
frutas=('frutilla','Manzana','Uva','Pera')
print(frutas[0])
verduras=('Cebolla','Tomate',5)
tuplafinal=frutas+verduras
print (tuplafinal)
listaconvertida=tuple(colores)
print (listaconvertida)
tuplanueva=tuplafinal+listaconvertida
print ("Union de lista convertida", tuplanueva)