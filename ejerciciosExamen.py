#Ejercicio 1 - SUMA DE LOS 100 PRIMEROS NUMEROS 1-100
suma=0
for i in range(1,101):
    suma +=i
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
    "estudiante6":{"nombre":"Brandon","edad":22,"ci":7847760,"carrera":"Sistemas Informaticos"}
}
#Pedir al usuario que ingrese la edad que desea buscar
edadBusqueda=int(input("Ingrese la edad que desea buscar: "))
