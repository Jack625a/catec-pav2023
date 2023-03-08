#Funciones con Argumento
def saludar(nombre, mensaje='Hola bienvenido'):
    print(mensaje + " "+ nombre)
saludar('Luis')
saludar('Luis','Buenos dias')

#Funciones Lambda
suma=lambda x,y: x+y
print("La suma es:", suma(7,2))

resta=lambda x,y: x-y
print("La resta es:", resta(10,5))

multiplicar=lambda x,y: x*y
print("La multiplicacion es:", multiplicar(2,8))

dividir=lambda x,y: x/y
print("La division es:", dividir(10,5))

#ordenar una lista de los numeros de menor a mayor
numeros=[3,6,8,43,23,12,7,13,43,32]
ordenar= sorted(numeros, key=lambda x:x)
print(ordenar) 
pares=list(filter(lambda x:x % 2==0, numeros))
print(pares)



    