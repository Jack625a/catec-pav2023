import math 
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
    operacion=input("ingrese una opcion")
    num1=float(input("ingrese un numero"))
    num2=float(input("ingrese un segundo numero"))
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
        
