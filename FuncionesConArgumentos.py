#Funciones con Argumento
def saludar(nombre,mensaje='Hola bienvenido'):
    print(mensaje + " "+ nombre)

saludar('Kevin')
saludar('Kevin','Buenos dias')

#Funciones Lambda para sumar
suma= lambda x,y:x+y
print("La suma es:", suma(7,2))
#Funciones Lambda para restar
resta= lambda a,b:a-b
print("La resta es:", resta(7,2))
#Funciones Lambda para Multiplicar
multiplicar= lambda a1,b1:a1*b1
print("La Multiplicacion es:", multiplicar(7,2))
#Funciones Lambda para dividir
dividir= lambda a2,b2:a2/b2
print("La División es:", dividir(7,2))

#Ordenar una lista
numeros=[45,4,8,42,13,1,69,78,5,17,6]
ordenar= sorted(numeros, key=lambda x:x)
print(ordenar)
paress= list(filter(lambda x:x % 2==0,numeros))
print(paress)


        



