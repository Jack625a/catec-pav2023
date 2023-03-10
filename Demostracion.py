class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print("hola, bienvenido mi nombre es: ",self.nombre)
alumno1=persona("Kevin",27)
alumno2=persona("Juan",25)
alumno3=persona("Jose",15)
alumno4=persona("Maria",24)
print("el estudiante seleccionado es ",alumno3.nombre)
print(alumno1.saludar())
print("el estudiante seleccionado es ",alumno2.nombre)
print(alumno2.saludar())
print("la edad del alumno 3 es ",alumno3.edad)

class animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def comer(self):
        comida=input("quiero comida")
        if comida=="":
            print("neccesito comida para sobrevivir")
        else:
            print("muchas gracias")
perro=animal("cachuchin",2)
gato=animal("olivia",3)
caballo=animal("paco",1)
print("seleccione al animal que desea alimentar")
print("perro")
print("gato")
print("caballo")
seleccion=input("a que anaimal desea alimenar? ")
if seleccion=="perro":
    print("el animal seleecionado es un perro de nombre: ",perro.nombre,"edad",perro.edad)
    perro.comer()
elif seleccion=="gato":
    print("el animal seleecionado es un gato de nombre: ",gato.nombre,"edad",gato.edad)
    gato.comer()
elif seleccion=="caballo":
    print("el animal seleecionado es un caballo de nombre: ",caballo.nombre,"edad",caballo.edad)
    caballo.comer()
else:
    print("no se tiene registros de ese animal")