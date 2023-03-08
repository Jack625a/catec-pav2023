#funciones con argumento
def saludar(nombre,mensaje="hola bienvenido"):
    print(mensaje + " "+ nombre)

saludar("kevin")
saludar("kevin","buenos dias")
#funciones lambda suma
suma= lambda x,y:x+y
print("la suma es: ", suma(7,2))
#funciones lambda resta
resta= lambda x1,y1:x1-y1
print("la resta es: ", suma(7,2))
#funciones lambda multiplicacion
multiplicar= lambda x2,y2:x2*y2
print("la multiplicacion es: ", suma(7,2))
#funciones lambda division
division= lambda x3,y3:x3/y3
print("la division es: ", suma(7,2))
#ordenar una lista
numeros=[45,4,8,42,13,1,69,78,5,17,6]
ordenar= sorted(numeros, key=lambda x:x)
print(ordenar)
pares= sorted(list(filter(lambda x:x % 2==0,numeros)))
print(pares)
    