#mostrar los numeros hasta el 10 con FOR
suma=0
for i in range(1,10):
    suma +=i
    print("la suma total es:",suma)
#impares
impares=1
for i in range(1,10,2):
    impares *=i
    print(impares)
#mostrar los numeros hasta el 10 con WHILE

#Ejercico 4 - Serie de Fibonaci con WHILE
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
#Ejercico 4 - Serie de Fibonaci con FOR
a=0
b=1
resultado=1
for i in range(1,11):
    print(a)
    a=b
    b=resultado
    resultado=a+b