#diccionario contagios y recuperados
Contagios={"Oruro": 9,"La Paz": 182,"Cochabamba": 33,"Pando": 1,"Potosi":2,"Beni":1,"Santa Cruz":4,"Chuquisaca":3,"Tarija":4 }
recuperados={"Oruro": 23,"La Paz": 253,"Cochabamba": 20,"Pando": 45,"Potosi":0,"Beni":0,"Santa Cruz":15,"Chuquisaca":11,"Tarija":65 }
print(Contagios)
print(recuperados)
print(Contagios["Contagios"])
print(recuperados["recuperados"])
#lista descuento en cine
precios={"regular":50,"estudiante":40,"adulto mayor":35}
p1=50
p2=40
p3=35
edad=int(input("Ingrese su edad"))
if edad <=30:
    print("El precio con descuento es: ",precios['estudiante'])
elif edad>=60:
    print ("El precio con descuento es: ", precios['adulto mayor'])
else:
    print ("El precio de la entrada es: " ,precios['regular'])

 #ingresar lista 5 paises
paises=[]
for i in range (1,6):
  pais= input("ingrese nombre de pais:")
  paises.append(pais) 
print=(paises)
