class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print("hola bienvenido mi nombre es: ", self.nombre)

estudiante1=persona("kevin",27)       
estudiante2=persona("juan",25)
estudiante3=persona("jose",30)
estudiante4=persona("maria",22)
print("el estudiante selecccionado es: ",estudiante1.nombre)
print(estudiante1.saludar())
print("el estudiante selecccionado es: ",estudiante4.nombre)
print(estudiante4.saludar())
print("el estudiante selecccionado es: ",estudiante2.nombre)

class mascota:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def comer(self):
        comida=input("quiero comida")
        if comida== "":
            print("nesesito comida para sobrevivir")
        else:
            print("muchas gracias")

perro=mascota("cachuchin",2) 
gato=mascota("olivia",3)
caballo=mascota("Paco",1)

print("seleccione al animal que desea alimentar")
print("perro")
print("gato")
print("caballo")
seleccion=input("A que animaldesea alimentar")
if seleccion=="perro":
    print("el animal seleccionado es un perro de nombre: ", perro.nombre,"edad:",perro.edad,"años")
    perro.comer()
elif seleccion=="gato":
    print("el animal seleccionado es un gato de nombre: ", gato.nombre,"edad:",gato.edad,"años")
    perro.comer()
elif seleccion=="caballo":
    print("el animal seleccionado es un caballo de nombre: ", caballo.nombre,"edad:",caballo.edad,"años")
    perro.comer()
else:
    print("nose tiene registrado ese animal")