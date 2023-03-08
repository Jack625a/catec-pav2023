#Ejercicio 1
contagios={"Santa Cruz":4, "Cochabamba":33, "La Paz":182, "Chuquisaca":11, "Tarija":4, "Potosi":2, "Oruro":9, "Beni":1, "Pando":1}
recuperados= {"Santa Cruz":15, "Cochabamba":20, "La Paz":253, "Chuquisaca":11, "Tarija":65, "Potosi":0, "Oruro":23, "Beni":0, "Pando":45}

print (contagios)
print(recuperados)
#Ejercicio 2
precios={"Estudiante":10, "AdultoMayor":15, "ClienteRegular":50}
x=50*0.20 #estudiante
y=50*0.30 #adulto mayor
z=50*1 #cliente regular
edad= int(input("Ingrese un edad"))
if edad <30:
    print("El precio descontado por estudiante es de:", x)
    x=50*0.20
elif edad >=60:
    print("El precio descontado por persona Adulto Mayor es de:", y)
else:
    print("El precio por ClienteRegular es de:", z)
#Ejercicio 3
x=[]

for i in range(0,5):
  pais= input("ingrese nombres de 5 paises")

x.append(pais)
numero= int(input("ingrese un numero del 0 al 5",))
print("el pais es", pais)
