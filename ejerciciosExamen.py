#ejercico de resta de numeros del 10 al 1 
for i in range (11,0,-1):
    print(i)

#ejercicio 1 - suma de los 100 primeros numeros 1-100
suma=0
for i in range (1,101):
    suma +=i
    print("la suma de los numeros es: ", suma)
#ejercicio 2 los 30 primeros inpares
for i in range(1,31):
    if i %2!=0:
        print("numero impar: ", i)

#ejercicio 3 crear un diccionario de la materia programacion avanzada con los siguientes datos
# estudiantes : estudiantes -- nombre edad ci carrera

estudiantes={
    "estudiante1":{"nombre":"brandon","edad":22,"ci":7485987,"carrera":"sistemas informaticos"},
    "estudiante2":{"nombre":"yeltsin","edad":22,"ci":5488956,"carrera":"sistemas informaticos"},
    "estudiante3":{"nombre":"nayeli","edad":19,"ci":1547851,"carrera":"sistemas informaticos"},
    "estudiante4":{"nombre":"issac","edad":22,"ci":4587998,"carrera":"sistemas informaticos"},
    "estudiante5":{"nombre":"jhonatan","edad":22,"ci":898745585,"carrera":"sistemas informaticos"},
    "estudiante6":{"nombre":"juan","edad":25,"ci":7485987,"carrera":"sistemas informaticos"},
    "estudiante7":{"nombre":"claudia","edad":26,"ci":5488956,"carrera":"sistemas informaticos"},
    "estudiante8":{"nombre":"mario","edad":19,"ci":1547851,"carrera":"sistemas informaticos"},
    "estudiante9":{"nombre":"morti","edad":25,"ci":4587998,"carrera":"sistemas informaticos"},
    "estudiante10":{"nombre":"jhanet","edad":26,"ci":898745585,"carrera":"sistemas informaticos"},
}
#pedir al usuario que ingrese la edad que desea buscar

edadb=int(input("ingrese la edad que desea buscar: "))

#buscamos los estudiantes con la edad ingresada por teclado 
estudianteb=[]
for estudiante,info in estudiantes.items():
    if info["edad"]==edadb:
        estudianteb.append(estudiante)

#imprimir los resultados obtenidos

if len(estudianteb)==0:
    print("no se encontro ningun estudiante de esa edad")
else:
    print("estudiantes con edad de: ", edadb, "años")
    for estudiante in estudianteb:
        print("***", estudiantes[estudiante]["nombre"])






