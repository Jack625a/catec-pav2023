#Ejercicio 1
contagios={"Oruro":4,"Cochabamba":7,"Santa CruZ":10,"Chuquisaca":8,"La paZ":5,"Potosi":4,"Tarija":7,"Beni":4,"Pando":4}
recuperados={"Oruro":3,"Cochabamba":2,"Santa CruZ":1,"Chuquisaca":10,"La paZ":3,"Potosi":4,"Tarija":0,"Beni":8,"Pando":2}
print("Nuevos contagios por Departamento")
for departamento, contagio in contagios.items():
    print(f"{departamento}:{contagio}")
print("Nuevos recuperados por Departamento")
for departamento, recuperado in recuperados.items():
    print(f"{departamento}:{recuperado}")
#Ejercicio 2
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
#Ejercicio 3
paises=[]
for i in range(1,6):
    pais=input("Ingrese el nombre de un Pais: ")
    paises.append(pais)
print(paises)
numero=int(input("Ingrese un numero del 1 al 5"))
print("El pais seleccionado es: ", paises[numero])




