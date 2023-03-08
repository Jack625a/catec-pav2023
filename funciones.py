#funcion sumar
a1=int(input("ingrese primer valor: "))
a2=int(input("ingrese segundo valor: "))
print("sumar=s - resta=r - multiplicacion=m - divicion=d ")
operacion=input("seleccione una operacion: ")
if operacion == "s":
    resultadooperacion=sumar(a1,a2)
    print("el resultado de la suma es: ", resultadooperacion)
elif operacion == "r":
    resultadooperacion=resta(a1,a2)
    print("el resultado de la resta es: ", resultadooperacion)
elif operacion == "m":
    resultadooperacion=multiplicacion(a1,a2)
    print("el resultado de la multiplicacion es: ", resultadooperacion)
elif operacion == "d":
    resultadooperacion=divicion(a1,a2)
    print("el resultado de la divicion es: ", resultadooperacion)
else:
    print("error debe seleccionar una opcion sumar=s - resta=r - multiplicacion=m - divicon=d : ")


def sumar(x,y):
    resultado=x+y
    return resultado
s=sumar(a1,a2)
print(s)
#restar
def resta(x,y):
    resultado=x-y
    return resultado
r=resta(a1,a2)
print(r)
#multiplicacion
def multiplicacion(x,y):
    resultado=x*y
    return resultado
m=multiplicacion(a1,a2)
print(m)
#divicion
def divicion(x,y):
    resultado=x/y
    return resultado
d=divicion(a1,a2)
print(d)