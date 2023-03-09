import math
print("Calculadora PAV-2023")
print("Seleccione las operaciones que desea realiZAr")
print("Operaciones Ariteticas= OA")
print("Operaciones Trigonometricas= OT")
print("Operaciones Geometricas= OG")
print("Logaritmos= LO")

opcion=input("Ingrese la operacion que desea realiZar")
if opcion == "OA":
    print("Seleccione una operacion aritmetica")
    print("SUMA= S")
    print("RESTA= R")
    print("MULTIPLICACION= M")
    print("DIVISION= D")
    operacion=input("Ingrese una opción: ")
    num1=float(input("Ingrese un primer numero: "))
    num2=float(input("Ingrese un segundo numero: "))
    if operacion == "S":
        resultado=num1+num2
        print("El resultado de la suma es: ",resultado)
    elif operacion == "R":
        resultado=num1-num2
        print("El resultado de la resta es: ",resultado)
    elif operacion == "M":
        resultado=num1*num2
        print("El resultado de la multiplicación es: ",resultado)
    elif operacion == "D":
        resultado=num1/num2
        print("El resultado de la division es: ",resultado)
    else:
        print("Seleccione una opción valida")
elif opcion == "OT":
    print("Seleccione una operación trigonometrica")
    print("Seno= SE")
    print("Coseno= CS")
    print("Tangente= TA")
    operacion=input("Ingrese la operacion que desea realiZar: ")

    num3=float(input("Ingrese un numero: "))
    if operacion == "SE":
        resultado=math.sin(num3)
        print("El seno de ", num3, "es: ",resultado)
    elif operacion == "CS":
        resultado=math.cos(num3)
        print("El coseno de ", num3, "es: ",resultado)
    elif operacion == "TA":
        resultado=math.tan(num3)
        print("La tangente de ", num3, "es: ",resultado)
    else:
        print ("Error seleccione una opción habilitada")
elif opcion == "OG":
    print("Seleccione la operación geometrica que dese realiZar")
    print("Area del circulo= AC")
    print("Area del triangulo= AT")
    print("Area del rectangulo= AR")
    operacion=input("Ingrese una opcion para la operacion geometrica que desea realiZar")
    if operacion == "AC":
        radio=float(input("Ingrese el radio del circulo"))
        resultado=math.pi*radio**2
        print("El area del circulo del radio ingresado ",radio, " es: ", resultado)
    elif operacion == "AT":
        base=float(input("Ingrese la base del triangulo"))
        altura=float(input("Ingrese la altura del triangulo"))
        resultado=(base*altura)/2
        print("El area del triangulo es: ", resultado)
    elif operacion == "AR":
        base=float(input("Ingrese la base del rectangulo: "))
        altura=float(input("Ingrese la altura del rectangulo: "))
        resultado=base*altura
        print("El area del rectangulo es: ", resultado)
    else:
        print("Error seleccione una opción valida")
elif opcion == "LO":
    print("Seleccione una operacion de logaritmos que desea calcular")
    print("Logaritmo Natural= LN")
    print("Logaritmo en base 10= L10")
    print("Logaritmo en base 2= L2")
    operacion=input("Ingrese la operacion logaritmica que desea realiZar: ")
    num=float(input("Ingrese un numero: "))

    if operacion == "LN":
        resultado=math.log(num)
        print("El logaritmo natural de ", num, " es: ", resultado)
    elif operacion == "L10":
        resultado=math.log10(num)
        print("El logaritmo en base 10 de ", num, " es: ", resultado)
    elif operacion == "L2":
        resultado=math.log2(num)
        print("El logaritmo en base 2 de ", num, " es: ", resultado)
    else:
        print("Error debe selccionar una opción valida")
else:
    print("Error debe selccionar una opción valida")