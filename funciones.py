#sumar
def sumar(x,y):
    resultado=x+y
    return resultado
#restar
def restar(a,b):
    result=a-b
    return result
#multiplicar
def multiplica(a2,b2):
    resultado1=a2*b2
    return multiplica
#dividir
def dividir(x1,y2):
    resultado1=x1/y2
    return dividir
#ingresar por teclado
a1=int(input("ingrese un numero: "))
a2=int(input("ingrese un numero: "))
print("suma=s - resta=r - multiplicacion=m - division=d")
operacion=input("seleccione la operacion a realizar ")
if operacion=="s":
    resultadooperacion=sumar(a1,a2)
    print("el resultado de la operacion es: ",resultadooperacion)
elif operacion=="r":
    resultadooperacion=restar(a1,a2)
    print("el resultado de la operacion es: ",resultadooperacion)
if operacion=="m":
    resultadooperacion=multiplica(a1,a2)
    print("el resultado de la operacion es: ",resultadooperacion)
if operacion=="d":
    resultadooperacion=dividir(a1,a2)
    print("el resultado de la operacion es: ",resultadooperacion)        
else:
    print("error, debe seleccionar una operacion correcta: suma=s - resta=r - multiplicacion=m - division=d")