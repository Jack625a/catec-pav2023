import math
class calculadora:
    def __init__(self):
        print("bienvenido a la calculadora avanzada poa ")
    def operaciones_aritmeticas(self):
        print("seleccione una operacion aritmetica: ")
        print("1.- suma")
        print("2.- resta")
        print("3.- multiplicacion")
        print("4.- dvision")
    operacion=int(input("ingrese la operacion que desea realizar: "))
    num1=float(input("ingrese un numero: "))
    num2=float(input("ingrese un numero: "))
    if operacion == "1":
            resultado=num1+num2
            print("el resultado de la suma es: ",resultado)
    elif operacion == "2":
            resultado=num1-num2
            print("el resultado de la resta es: ",resultado)
    elif operacion == "3":
            resultado=num1*num2
            print("el resultado de la multiplicacion es: ",resultado)
    elif operacion == "4":
            resultado=num1/num2
            print("el resultado de la division es: ",resultado)
    else:
            print("seleccione una opcion valida")
def operaciones_trigonometricas(self):
    print("seleccione la operacion trigonometrica que desea realizar: ")
    print("seleccione una operacion geometrica")
    print("area del circulo= ac")
    print("area del triangulo= at")
    print("area del rectagulo= ar")
    operacion=input("eliga una opcion geometrica que desea realizar: ")
    num3=float(input("ingrese un numero: "))
    if operacion == "ac":
        radio=float(input("ingrese el radio del circulo: "))
        resultado=math.pi*radio**2
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
def operaciones_gometricas(self):
    print("seleccione una operacion geometrica")
    print("area del circulo= ac")
    print("area del triangulo= at")
    print("area del rectagulo= ar")
    operacion=input("eliga una opcion geometrica que desea realizar: ")
    if operacion == "ac":
        radio=float(input("ingrese el radio del circulo: "))
        resultado=math.pi*radio**2
        print("el radio del circulo ingresado",radio," es: ",resultado)
    elif operacion == "at":
        base=float(input("ingrese la base del triangulo: "))
        altura=float(input("ingrese la altura del triangulo: "))
        resultado=(base*altura)/2
        print("el area del triangulo es: ",resultado)
    elif operacion == "ar":
        base=float(input("ingrese la base del rectangulo: "))
        altura=float(input("ingrese la altura del rectangulo: "))
        resultado=(base*altura)
        print("el area del rectangulo es: ",resultado)
    else:
        print("error seleccione una opcion valida")
def operaciones_logaritmos(self):
    print("seleccione una operacion de logaritmos")
    print("logaritmo natural= ln")
    print("logaritmo en base 10= l10")
    print("logartimo en base 2= l2")
    operacion=input("eliga una opcion de logaritmo que desea realizar: ")
    num4=float(input("ingrese un numero: "))
    if operacion == "ln":
        resultado =math.log(num4)
        print=("el logaritmo natural de ",num4," es: ",resultado)
    elif operacion == "l10":
        resultado =math.log10(num4)
        print=("el logaritmo en base 10 de ",num4," es: ",resultado)
    elif operacion == "l2":
        resultado =math.log2(num4)
        print=("el logaritmo en base 2 de ",num4," es: ",resultado)
    else:
        print("error, debe seleccionar una opcion valida")
def suma(self,num1,num2):
     return num1+num2
def resta(self,num1,num2):
     return num1-num2
def multiplicacion(self,num1,num2):
     return num1*num2
def devision(self,num1,num2):
     if num2 ==0:
          print("error no se puede dividir entre 0")
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
def logaritmon(self,num4):
     return math.log(num4)
def logaritmo10(self,num4):
     return math.log10(num4)
def logaritmo2(self,num4):
     return math.log2(num4)