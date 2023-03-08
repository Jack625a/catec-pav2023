#Funcion Sumar
def sumar(x,y):
    resultado=x+y
    return resultado
#Resultado de la Funcion
c=sumar(18,5)
print(c)
#Funcion Restar
def restar(x,y):
    resultado=x-y
    return resultado
#Resultado de la Funcion
c=restar(18,5)
print(c)
#Funcion dividir
def dividir(x,y):
    resultado=x/y
    return resultado
#Resultado de la Funcion
c=dividir(18,5)
print(c)
#Funcion multiplicar
def multiplicar(x,y):
    resultado=x*y
    return resultado
#Resultado de la Funcion
c=multiplicar(18,5)
print(c)
a1=input(input"Igrese un Numero")
a2=input(input"Igrese un Numero")
print("SUMA=S - RESTA=R - MULTIPLICACION - DIVISION=D")
Operacion=input("Seleccione la operacion a Ralizar")
if operacion=="s":
    resultadoOperacion=sumar(a1,a2)
    print("El resultado de la suma es: ", resultadoOperacion)
elif operacion=="R":