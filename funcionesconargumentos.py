#funciones con argumento
print("FUNCIONES CON ARGUMENTO")
def saludar(nombre,mensaje='hola bienvenido: ' ):
    print(mensaje + ""+ nombre)
    
saludar('brandon  Choque Heredia')
saludar('brandon','buenos dias ')

#funciones lambda
print("FUNCIONES LAMBDA")
suma = lambda x,y:x+y
print("la suma es ", suma(7,2))

resta = lambda x,y:x-y
print("la resta es ", resta(7,2))

multiplicacion = lambda x,y:x*y
print("la multiplicacion es ", multiplicacion(7,2))

divicion = lambda x,y:x/y
print("la divicion es ", divicion(7,2))

#ordenar una lista
print("ORDENANDO LISTAS")
numeros=[10,15,12,14,13,18,16,17,19,20,11]
ordenar= sorted(numeros, key=lambda x:x)
print(ordenar)
paress= list(filter(lambda x:x % 2==0,numeros))
print(paress)

