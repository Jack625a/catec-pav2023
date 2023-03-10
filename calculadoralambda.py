import math
suma=lambda x,y:x+y
resta=lambda x,y:x-y
multiplicacion=lambda x,y:x*y
division=lambda x,y:x/y

seno=lambda x:math.sin(x)
coseno=lambda x:math.cos(x)
tangente=lambda x:math.tan(x)

area_circulo=lambda r:math.pi*r**2
area_triangulo=lambda b,a:b*a*0.5
area_rectangulo=lambda b,a:b*a 

logaritmon=lambda x:math.log(x)
logaritmol10=lambda x:math.log10(x)
logaritmol2=lambda x:math.log2(x)

print("calculadora pav-2023")
print("seleccione las operaciones que desea realizar")
print("operaciones aritmeticas= oa")
print("operaciones trigonometricas= ot")
print("operaciones geometricas= og")
print("logaritmos= lo")

opcion= input("ingrese la operacion que desea realizar ")
if opcion == "oa":
    print("seleccione una operacion arrritmetica")
    print("suma= s")
    print("resta= r")
    print("multiplicacion= m")
    print("division= d")
    operacion= input("ingrese una opccion ")
    num1=float(input("ingrese un primer numero"))
    num2=float(input("ingrese un segundo numero"))
    if operacion == "s":
        resultado=suma(num1,num2)
        print("el resultado de la suma es: ",resultado)
    elif operacion == "r":
        resultado=resta(num1,num2)
        print("el resultado de la resta es: ",resultado)
    elif operacion == "m":
        resultado=multiplicacion(num1,num2)
        print("el resultado de la multiplicacion es: ",resultado)
    elif operacion == "d":
        resultado=division(num1,num2)
        print("el resultado de la division es: ",resultado)
    else:
        print("seleccione una opcion valida")

elif opcion == "ot":
    print("seleccione una operacion trigonometrica")
    print("seno= se")
    print("coseno= cs")
    print("tangente= ta")
    operacion= input("ingrese la operacion que desea realizar: ")

    num3=float(input("ingrese un numero: "))
    if operacion == "se":
        resultado=seno(num3)
        print("el seno de ",num3, "es: ",resultado)
    elif operacion == "cs":
        resultado=coseno(num3)
        print("el coseno de ",num3, "es: ",resultado)
    elif operacion == "ta":
        resultado=tangente(num3)
        print("el tangente de ",num3, "es: ",resultado)
    else:
        print("error, seleccione una opcion habilitada")
elif opcion == "og":
    print("seleccione una operacion geometrica")
    print("area del circulo= ac")
    print("area del triangulo= at")
    print("area del rectagulo= ar")
    operacion=input("eliga una opcion geometrica que desea realizar: ")
    if operacion == "ac":
        radio=float(input("ingrese el radio del circulo: "))
        resultado=area_circulo*radio**2
        print("el radio del circulo ingresado",radio," es: ",resultado)
    elif operacion == "at":
        base=float(input("ingrese la base del triangulo"))
        altura=float(input("ingrese la altura del triangulo"))
        resultado=(base*altura)/2
        print("el area del triangulo es: ",resultado)
    elif operacion == "ar":
        base=float(input("ingrese la base del rectangulo"))
        altura=float(input("ingrese la altura del rectangulo"))
        resultado=(base*altura)
        print("el area del rectangulo es: ",resultado)
    else:
        print("error seleccione una opcion valida")
elif opcion == "lo":
    print("seleccione una operacion de logaritmos")
    print("logaritmo natural= ln")
    print("logaritmo en base 10= l10")
    print("logartimo en base 2= l2")
    operacion=input("eliga una opcion de logaritmo que desea realizar: ")
    num=float(input("ingrese un numero: "))
    if operacion == "ln":
        resultado =logaritmon(num)
        print=("el logaritmo natural de ",num," es: ",resultado)
    elif operacion == "l10":
        resultado =logaritmol10(num)
        print=("el logaritmo en base 10 de ",num," es: ",resultado)
    elif operacion == "l2":
        resultado =logaritmol2(num)
        print=("el logaritmo en base 2 de ",num," es: ",resultado)
    else:
        print("error, debe seleccionar una opcion valida")
else:
    print("error, debe seleccionar una opcion valida")