#Funcion Sumar
def sumar(x,y):
    resultado=x+y
    return resultado
#Funcion Restar
def restar(x1,y2):
    resultado1=x1-y2
    return resultado1
#Funcion Dividir
def dividir(x2,y3):
    resultado2=x2/y3
    return resultado2
#Funcion Multiplicar
def multiplicar(x3,y4):
    resultado3=x3*y4
    return resultado3
#Resultado de la Funsion
print("Funcion Sumar")
c=sumar(18,5)
print(c)

print("Funcion Restar")
d=restar(5,8)
print(d)

a1=int(input("Ingrese un Numero"))
a2=int(input("Ingrese un Numero"))
print("SUMA=S - RESTA=R - MULTIPLICACION=M - DIVISION=D")
operacion=input("Seleccione la operacion a RealiZAr")
if operacion=="S":
    resultadoOperacion=sumar(a1,a2)
    print("El resultado de la suma es: ", resultadoOperacion)
elif operacion=="R":
    resultadoOperacion=restar(a1,a2)
    print("El resultado de la resta es: ", resultadoOperacion)
elif operacion=="M":
    resultadoOperacion=multiplicar(a1,a2)
    print("El resultado de la multiplicacion es: ", resultadoOperacion)
elif operacion=="D":
    resultadoOperacion=dividir(a1,a2)
    print("El resultado de la division es: ", resultadoOperacion)
else:
    print("Error debe seleccionar una operacion: SUMA=S - RESTA=R - MULTIPLICACION=M - DIVISION=D")
    


