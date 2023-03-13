import math

class Calculadora:
    def __init__(self):
        print("Bienvenido a la CALCULADORA AVANZADA POA")
    
    def operaciones_aritmeticas(self):
        print("Selecciones una operación aritmetica:")
        print("1. SUMA")
        print("2. RESTA")
        print("3. MULTIPLICACIÓN")
        print("4. DIVISIÓN")
        operacion=int(input("Ingrese la operación aritmetica que desea realizar:  "))
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese un numero: "))
        if operacion == 1:
            resultado=num1+num2
            print("El resultado de la suma es: ",resultado)
        elif operacion == 2:
            resultado=num1-num2
            print("El resultado de la resta es: ",resultado)
        elif operacion == 3:
            resultado=num1*num2
            print("El resultado de la multiplicación es: ",resultado)
        elif operacion == 4:
            resultado=num1/num2
            print("El resultado de la division es: ",resultado)
        else:
            print("Seleccione una opción valida")
    
    def operaciones_trigonometricas(self):
        print("Seleccione la operación trigonometrica que desea realizar")
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
    
    def operaciones_geometricas(self):
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

    def operciones_logaritmicas(self):
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

    def suma(self,num1,num2):
        return num1+num2
    def resta(self,num1,num2):
        return num1-num2
    def multiplicacion(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        if num2==0:
            print("Error no se puede dividir entre cero")
            return None
        else:
            return num1/num2
    def seno(self,num3):
        return math.sin(num3)
    def coseno(self,num3):
        return math.cos(num3)
    def tangente(self,num3):
        return math.tan(num3)
    def area_circulo(self,radio):
        return math.pi*radio**2
    def area_triangulo(self,base,altura):
        return (base*altura)/2
    def area_rectangulo(self,base,altura):
        return base*altura
    def logaritmo_natural(self,num):
        return math.log(num)
    def logaritmo_10(self,num):
        return math.log10(num)
    def logaritmo_2(self,num):
        return math.log2(num)
    
    
