#Ejercicio 1 - Numero del 1 al 100
numeros=1
while numeros<=10:
    print(numeros)
    numeros+=1
#Ejercicio 2 - Numero pares del 1 al 100
pares=2
while pares<=100:
    print("Números pares",pares)
    pares+=2
#Ejercicio 3 - Mostrar los numeros del 10 al 1
numero=10
while numero>=1:
    print(numero)
    numero-=1
#Ejercico 4 - Serie de Fibonaci
print("Serie de Fibonaci")
x=0
y=1
q=1
sumatoria=1
while(q<=20):
    q +=1
    print(x)
    x=y
    y=sumatoria
    sumatoria=x+y