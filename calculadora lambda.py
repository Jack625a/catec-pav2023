#calculadora lambda
import math
#FUNCIONES LAMBDA para operaciones aritmeticas
suma=lambda x,y:x+y
resta=lambda x,y:x-y
multiplicacion=lambda x,y:x*y
division=lambda x,y:x/y
#FUNCIONES LAMBDA para operaciones trigonometricas
seno=lambda x:math.sin(x)
coseno=lambda x:math.cos(x)
tangente=lambda x:math.tan(x)
#FUNCIONES LAMBDA para operaciones geometricas
area_circulo=lambda r:math.pi*r**2
area_triangulo=lambda b,a:b*a*0.5
area_rectangulo=lambda b,a:b*a
#FUNCIONES LAMBDA para operaciones logaritmicas
logaritmoN=lambda x: math.log(x)
logaritmo10=lambda x: math.log10(x)
logaritmo2=lambda x: math.log2(x)
print("calculador PAV-2023")
print("seleccione las operacioneque desea realizar")
print("operaciones aritmeticas= OA")
print("OPERACIONES trigonometricas= OT")
print("operacione geometricas= OG")
print("logaritmos=LO")

opcion=input("Ingrese la operacion que desea realizar")
if opcion == "OA":
    print("selecione una operacion aritmetica")
    print("SUMA= S")
    print("RESTA= R")
    print("MULTIPLICACION= M")
    print("DIVISION= D")
    if operacion =="S":
        resultado=num1+num2
        print("el resultado de la suma es: ",reultado)
    elif operacion == "R":
        RESULTADO=num1 - num2
        print("el resultado de la resta es:",resultado)
    elif operacion == "M":
        RESULTADO=num1 * num2
        print("el resultado de la multiplicacion es:",resultado)
    elif operacion == "D":
        RESULTADO=num1 / num2
        print("el resultado de la division es:",resultado)
    else:
        print("selecione una operacion valida")
elif opcion == "OT":
    print("selecione una operacion aritmetica")
    print("seno= SE")
    print("Coseno= CS")
    print("Tangente= TA")
    operacion=input("ingrese la operacion que desea realizar: ")

    num3=float(input("ingrese un numero"))
    if operacion == "SE":
        resultado=math.sin(num3)
        print("El seno de ", num3, "es:" ,resultado)
    elif operacion == "CS":
        resultado=math.sin(num3)
        print("El coseno de ", num3, "es:" ,resultado)
    elif operacion == "TA":
        resultado=math.sin(num3)
        print("El tangente de ", num3, "es:" ,resultado)
    else: 
        print("error seleccione una opcion habilitada")
elif opcion == "OG":
    print("seleccione la operacion geometrica que desea realizar")
    print("area del circulo= AC")
    print("area del triangulo= AT")
    print("area del rectangulo= AR")
    operacion=input("ingrese una opcion para la operacion geometrica que decearealizar")
    if operacion == "AC":
        radio=float(input("ingrese el radio del circulo"))
        resultado=math.pi*radio**2
        print("el area del circulo ingresado",radio, " es: ",resultado )
    elif opercion =="AT":
        base=float(input("ingrese la base del tiangulo"))
        altura=float(input("ingrese la altura del triangulo"))
        resultado=(base*altura)/2
        print("el area del triangulo es: ", resultado)
    elif operacion == "AR":
        base=float(input("ingrese la base del rectangulo"))
        altura=float(input("ingrese la altura del rectangulo"))
        resultado=base*altura 
        print("el area del rectangulo es: ", resultado)
    else:
        print("error selecione una opcion valida")
elif opcion == "LO":
    print("selecione una operacion de logaritmos que desea realizar")
    print("Logaritmo natural = LN")
    print("Logaritmo en base 10= L10")
    print("Logaritmo en base 2= L2")
    operacion=input("ingrese la operacion logaritmicaque desea realizar: ")
    num=float(input("ingrese un numero"))

    if operacion == "LN":
        resultado=math.log(num)
        print("el logaritmo natural de ", num, " es: ", resultado)
    elif operacion =="L10":
        resultado= math.log10(num)
        print("el logaritmo en base 10", num, " es:", resultado)
    elif operacion =="L2":
        resultado= math.log2(num)
        print("el logaritmo en base 2", num, " es:", resultado)
    else:
        print("error debe ingresar una opcion valida")
else:
        print("error debe seleccionar uuna opcion valida")