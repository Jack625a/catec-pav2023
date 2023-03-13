class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print("hola, bienvenido mi nombre es: ",self.nombre)

estudiante1=Persona("kevin",27)
estudiante2=Persona("juan",24)
estudiante3=Persona("albert",23)
estudiante4=Persona("maria",22)
print("el estudiante elegido es: ",estudiante1.nombre)
print(estudiante1.saludar())
print("el estudiante elegido es: ",estudiante4.nombre)
print(estudiante4.saludar())
print("la edad del estudiante es: ",estudiante2.edad)
#ENTRE ANIMALES
class animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def comer(Self):
        comida=input("quiero comida ")
        if comida=="":
            print("nesecito comida para sobrevivir ")
        else:
            print("muchas gracias")
    
perro=animal("tyson",2)
gato=animal("olivia",3)
caballo=animal("paco",1)

print("seleccione al animal que quiere alimentar ")
print("perro")
print("gato")
print("caballo")
seleccion=input("a que animal desea alimentar..?")
if seleccion== "perro":
    print("el animal seleccionado es un perro de nombre: ",perro.nombre," de edad: ",perro.edad,"años")
    perro.comer()
elif seleccion== "gato":
    print("el animal seleccionado es un gato de nombre: ",gato.nombre," de edad: ",gato.edad,"años")
    gato.comer()
if seleccion== "caballo":
    print("el animal seleccionado es un caballo de nombre: ",caballo.nombre," de edad: ",caballo.edad,"años")
    caballo.comer()
else:
    print("no tienen registro de ese animal ")
