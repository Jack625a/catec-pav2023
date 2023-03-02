#Ejercicio 1 - SUMA DE LOS 100 PRIMEROS NUMEROS 1-100
suma=0
for i in range(1,101):
    suma +=i
    print("la suma de los numeros del 1 al 100 es: ", suma)
#Ejercicio 2 - 30 primeros numeros impares
for i in range(1,31):
    if i %2!=0:
        print("Numero impar:", i)
#Ejercicio 3 - Crear un diccionario de la materia Programacion Avanzada
#Diccionario: Estudianates-> nombre, edad, ci, carrera
Estudiantes={
    "estudiante1":{"nombre":"Limbeth","edad":21,"ci":4568955,"carrera":"Sistemas Informaticos"},
    "estudiante2":{"nombre":"Jhonatan","edad":28,"ci":7485963,"carrera":"Sistemas Informaticos"},
    "estudiante3":{"nombre":"David","edad":23,"ci":7894561,"carrera":"Sistemas Informaticos"},
    "estudiante4":{"nombre":"Nayeli","edad":20,"ci":8655841,"carrera":"Sistemas Informaticos"},
    "estudiante5":{"nombre":"Isaac","edad":21,"ci":8569874,"carrera":"Sistemas Informaticos"},
    "estudiante6":{"nombre":"Brandon","edad":22,"ci":8789565,"carrera":"Sistemas Informaticos"}
}
print(Estudiantes)
#Pedir al usuario que ingrese la edad que desea buscar
edadBusqueda=int(input("Ingrese la edad que desee buscar"))

#Buscamos los estudiantes con la edad ingresada por teclado
estudianteBuscado=[]
for estudiante,info in Estudiantes.items():
    if info["edad"]==edadBusqueda:
        estudianteBuscado.append(estudiante)
#Imprimimos los resultados obtenidos 
if len(estudianteBuscado)==0:
    print("No se encontraron estudiantes con la edad ingresada")
else:
    print("Estudiantes con edad de ", edadBusqueda, "años")
    for estudiante in estudianteBuscado:
        print("-",Estudiantes[estudiante]["nombre"])