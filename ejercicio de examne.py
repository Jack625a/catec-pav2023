#1 numeros del 10 al 1
for i in range(11,0,-1):
    print(i)
#2 suma de los 100 primeros numeros
suma=0
for i in range(1,101):
    suma +=i
    print("la suma de los numeros del 1 al 100 es: ", suma)
#3 30 primeros numeros impares
for i in range(1,31):
    if i%2!=0:
        print("numero impar: ", i)
#4 crear un diccionario de la materia programacion avanzada con los siguientes datos
#Diccionario: Estudiante->nombre,edad,ci,carrera
estudiantes={
    "Estudiante1":{"nombre":"Limberth","edad":21,"ci":7317760,"carrera":"sistemas informaticos"},
    "Estudiante2":{"nombre":"Jhonatan","edad":28,"ci":7345760,"carrera":"sistemas informaticos"},
    "Estudiante3":{"nombre":"David","edad":23,"ci":7317780,"carrera":"sistemas informaticos"},
    "Estudiante4":{"nombre":"Nayeli","edad":20,"ci":7315660,"carrera":"sistemas informaticos"},
    "Estudiante5":{"nombre":"Isaac","edad":21,"ci":731450,"carrera":"sistemas informaticos"},
    "Estudiante6":{"nombre":"Brandon","edad":22,"ci":7237760,"carrera":"sistemas informaticos"}
}
#pedir al usuario que ingrese la edad que desea buscar
edadbusqueda=int(input("ingrese la edad que desea buscar: "))
#buscamos los estudiantes con la edad ingresada por teclado
estudiantebuscado=[]
for estudiante,info in estudiantes.items():
    if info["edad"]==edadbusqueda:
        estudiantebuscado.append(estudiante)
#imprimimos los resultados optenidos
if len(estudiantebuscado)==0:
    print("no se encontraron estudiantes con la edad ingresada")
else:
    print("estudiantes con edad de ",edadbusqueda,"años")
    for estudiante in estudiantebuscado:
        print("-",estudiantes[estudiante]["nombre"])