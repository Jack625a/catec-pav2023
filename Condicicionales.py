#Ejercicio 1 - Numero par o impar
numero= int(input("Ingrese un numero"))
if numero %2 ==0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")
#Ejercicio 2 - Calcular el numero mayor entre dos numeros
num1=int(input("Ingrese un Numero"))
num2=int(input("Ingrese un Numero"))
if num1>num2:
    print("El numero mayor es: ", num1)
elif num2>num1:
    print("El numero mayor es: ", num2)
else:
    print("Los numeros ingresado son Iguales")