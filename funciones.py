def sumar(x,y):
    resultado=x+y
    return resultado

a=18
b=12
c=sumar(a,b)
print (c)
#resta
def restar(x,y):
    resultado=x-y
    return resultado
x=20
y=18
c=restar(x,y)
print (c)

#multiplicacion
def multiplicar(x,y):
    resultado=x*y
    return resultado
x=2
y=8
c=multiplicar(x,y)
print (c)

#dividir
def dividir(x,y):
    resultado=x/y
    return resultado
x=40
y=5
c=dividir(x,y)
print (c)

#todas las funciones
a1= int(input("Ingrese un numero"))
a2=int(input("ingrese un numero"))

print ("funcion multiplicar")
f=multiplicar(a1,a2)
print(f)

print ("funcion dividir")
f=dividir(a1,a2)
print(f)

print ("funcion sumar")
f=sumar(a1,a2)
print(f)

print ("funcion restar")
f=restar(a1,a2)
print(f)

#otra forma de todas las funciones
a1=int(input("ingrese un numero"))
a2=int(input("ingrese un numero"))
print("SUMA=S . RESTA=R - MULTIPLICACION=M - DIVISION=D")
operacion=input("Seleccione la operacion a realizar")
if operacion=="S":
    resultadooperacion=sumar(a1,a2)
    print("El resultado de la suma es: ", resultadooperacion)
elif operacion =="R":
    resultadooperacion=restar(a1,a2)
    print("El resultado de la resta es:", resultadooperacion)
elif operacion =="M":
    resultadooperacion=multiplicar(a1,a2)
    print("El resultado de la multiplicacion es: ", resultadooperacion)
elif operacion =="D":
    resultadooperacion=dividir(a1,a2)
    print("El resultado de la division es: ", resultadooperacion)
else:
    print("Error, debe seleccionar una operacion: SUMA=S - RESTA=R - MULTIPLICACION=M - DIVISION=D")