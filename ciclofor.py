suma=0
for i in range(1,10):
    suma+=i
    print("la suma total es: ",suma)
#impar
impares=1
for i in range(1,10,2):
    impares +=i
    print(impares)
#lista de 1 al 10 
pares=2
while pares<=100:
    print(pares)
    pares+=2
#lista de 1 al 10 en for
pares=1
for i in range(1,10):
    print(pares)
    pares+=1
#serie fibonaci
print("serie fibonaci")
x=0
y=1
q=1
sumatoria=1
while (q<=10):
    q +=1
    print(x)
    x=y
    y=sumatoria
    sumatoria=x+y
#serie fibonaci en for
a=0
b=1
n=1
resultado=1
for i in range(1,11):
    print(a)
    a=b
    b=resultado
    resultado=a+b
