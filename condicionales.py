
#numero par o impar
numero= int(input("ingrese un numero"))
if numero %2 ==0:
    print ("el numero ingresado es par")
else:
    print("el numero ingresado es impar ")

#ejercicio 2 calcular el numero mayor entre 2 numeros 

num1= int(input("ingrese un numero"))
num2= int(input("ingrese un numero"))
if num1>num2:
    print("el numero mayor es: ", num1)
elif num2>num1:
    print("el numero mayor es:", num2)
else:
    print("los numeros son iguales")
