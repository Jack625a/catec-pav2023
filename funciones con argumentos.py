#funciones con argumrntos
def saludar(nombre, mensaje="hola bienvenido"):
            print( mensaje +" "+ nombre)

saludar("kevin")
saludar("kevin","Buenos dias")

#funciones Lambda
suma= lambda x,y:x+y
print(" la suma es:", suma(7,2))
resta= lambda x,y:x-y
print(" la resta es:", resta(7,2))
multiplicar= lambda x,y:x*y
print(" la multiplicacion es:", multiplicar(7,2))
dividir= lambda x,y:x/y
print(" la divicion es:", dividir(7,2))

#ordenar una lista
numeros=(45,4,8,42,13,1,69,78,5,17,6)
ordenar=sorted(numeros,key=lambda x:x)
print (ordenar)
pares= list(filter(lambda x:x % 2==0,numeros))
print(pares)
