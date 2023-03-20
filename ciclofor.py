suma=0
for i in range(1,10):
    suma +=i
    print("La suma total es: ",suma)
#Impares
impares=1
for i in range(1,20,2):
    impares *=i
    print(impares)
#Mostrar los numeros hasta el 10 WHILE
numeros=1
while numeros<=10:
    print(numeros)
    numeros+=1
#Mostrar los numeros hasta el 10 FOR
numero=1
for i in range(1,11):
    print(numero)
    numero +=1

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
#Ejercico 4 - Serie de Fibonaci en FOR}
print("Serie de Fibonaci en FOR")
a=0 
b=1 
resultado=1
for i in range(1,21):
    print(a)
    a=b
    b=resultado
    resultado=a+b

#Numeros del 10 al 1
for i in range (11,0,-1):
    print(i)      