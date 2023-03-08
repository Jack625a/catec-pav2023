def saludar(nombre,mensaje='Hola bienvenida'):
    print(mensaje+ " "+ nombre)

saludar('Nayeli')
saludar('Nayeli','Buenos dias')

#Funciones Lambda
suma= lambda x,y:x+y
print("La suma es :", suma(9,7))
#Funciones Lambda para restar
resta= lambda x,y:x-y
print("La resta es :", resta(9,7))
 #Funciones Lambda para multiplicar
multiplicar= lambda x,y:x*y
print("La multiplicacion es :", multiplicar(9,7))
#Funciones Lambda para dividir
dividir= lambda x,y:x/y
print("La division es :", dividir(9,7))

#Ordenar una lista 
numeros=[45,8,65,9,78,4,5,2,8,10]
ordenar= sorted(numeros,key= lambda x:x)
print(ordenar)
pares= list(filter(lambda x:x % 2==0,numeros))
print(pares)


