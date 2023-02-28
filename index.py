#listas
colores=["rojo","amarrillo","verde","cafe"]
print("lista de colores: ",colores)
#update listas
print(colores[0])
colores[2]="morado"
print("lista nueva: ", colores)
#eliminar elemento de una lista
del colores[1]
print("lista con valor eliminado: ", colores)
#tuplas
frutas=("frutilla","banana","uva","pera")
print(frutas[0])
verduras=("cebolla","tomate",5)
tuplafinal=frutas+verduras
print(tuplafinal)
listaconvertida=tuple(colores)
print(listaconvertida)
tuplanueva=tuplafinal+listaconvertida
print("union de lista convertida con tupla", tuplanueva)