#Ejercicio 1 - SUMA DE LOS 100 PRIMEROS NUMEROS 1-100
suma=0
for i in range(1,101):
    suma +=i
<<<<<<< HEAD
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
=======
    print("La suma de los numeros del 1 al 100 es: ", suma) 
#Ejercicio 2 - 30 primeros numeros impares
for i in range(1,31):
    if i %2!=0:
        print("Numero impar: ", i)
#Ejercicio 3 - Crear un diccionario de la materia Programacion AvanZada con lo siguientes datos
#Diccionario: Estudiantes-> nombre, edad, ci, carrera
Estudiantes={
    "estudiante1":{"nombre":"Limberth","edad":21,"ci":7317760,"carrera":"Sistemas Informaticos"},
    "estudiante2":{"nombre":"Jhonatan","edad":28,"ci":7123155,"carrera":"Sistemas Informaticos"},
    "estudiante3":{"nombre":"David","edad":23,"ci":7317765,"carrera":"Sistemas Informaticos"},
    "estudiante4":{"nombre":"Nayeli","edad":20,"ci":7315460,"carrera":"Sistemas Informaticos"},
    "estudiante5":{"nombre":"Isaac","edad":21,"ci":7477760,"carrera":"Sistemas Informaticos"},
    "estudiante6":{"nombre":"Brandon","edad":22,"ci":7847760,"carrera":"Sistemas Informaticos"},
    "estudiante7":{"nombre":"Pedro","edad":21,"ci":7317760,"carrera":"Sistemas Informaticos"},
    "estudiante8":{"nombre":"Juan","edad":28,"ci":7123155,"carrera":"Sistemas Informaticos"},
    "estudiante9":{"nombre":"Jose","edad":23,"ci":7317765,"carrera":"Sistemas Informaticos"},
    "estudiante10":{"nombre":"Jorge","edad":20,"ci":7315460,"carrera":"Sistemas Informaticos"},
    "estudiante11":{"nombre":"Ana","edad":21,"ci":7477760,"carrera":"Sistemas Informaticos"},
    "estudiante12":{"nombre":"Maria","edad":21,"ci":7317760,"carrera":"Sistemas Informaticos"},
    "estudiante13":{"nombre":"Rene","edad":28,"ci":7123155,"carrera":"Sistemas Informaticos"},
    "estudiante14":{"nombre":"Marco","edad":23,"ci":7317765,"carrera":"Sistemas Informaticos"},
    "estudiante15":{"nombre":"Saul","edad":20,"ci":7315460,"carrera":"Sistemas Informaticos"},
    "estudiante16":{"nombre":"Juan","edad":21,"ci":7477760,"carrera":"Sistemas Informaticos"},
    "estudiante17":{"nombre":"Carla","edad":21,"ci":7317760,"carrera":"Sistemas Informaticos"},
    "estudiante18":{"nombre":"Claudia","edad":28,"ci":7123155,"carrera":"Sistemas Informaticos"},
    "estudiante19":{"nombre":"Andrea","edad":23,"ci":7317765,"carrera":"Sistemas Informaticos"},
    "estudiante20":{"nombre":"Mariana","edad":20,"ci":7315460,"carrera":"Sistemas Informaticos"},
    "estudiante21":{"nombre":"Roberto","edad":21,"ci":7477760,"carrera":"Sistemas Informaticos"},
}
#Pedir al usuario que ingrese la edad que desea buscar
edadBusqueda=int(input("Ingrese la edad que desea buscar: "))
>>>>>>> c4a91e2925e73411c8a1d92a33c7d992b28eea79

#Buscamos los estudiantes con la edad ingresada por teclado
estudianteBuscado=[]
for estudiante,info in Estudiantes.items():
    if info["edad"]==edadBusqueda:
        estudianteBuscado.append(estudiante)
<<<<<<< HEAD
#Imprimimos los resultados obtenidos 
=======
#Imprimir los resultados obtenidos
>>>>>>> c4a91e2925e73411c8a1d92a33c7d992b28eea79
if len(estudianteBuscado)==0:
    print("No se encontraron estudiantes con la edad ingresada")
else:
    print("Estudiantes con edad de ", edadBusqueda, "años")
    for estudiante in estudianteBuscado:
<<<<<<< HEAD
        print("-",Estudiantes[estudiante]["nombre"])
=======
        print("°",Estudiantes[estudiante]["nombre"])

    
>>>>>>> c4a91e2925e73411c8a1d92a33c7d992b28eea79
