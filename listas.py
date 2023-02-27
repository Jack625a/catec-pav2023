colores = ["rojo","amarillo","verde"]
print ("lista de colores:", colores)
print (colores [0])
colores[1]="cafe"
print ("lista actualizada", colores)
#eliminar un valor de la lista
del colores[0]
print("lista atualizada:", colores)
#tupla
print("lista de frutas")
frutas=("frutilla","banana","pera","manzana")
print (frutas[0])
verduras=("cebolla","tomate","acelga")
tuplafinal=frutas+verduras
print(tuplafinal)
listaconvertida=tuple(colores)
print(listaconvertida)
tuplanueva=tuplafinal+listaconvertida
print ("union de la lista convertida con tupla", tuplanueva)