class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad= edad
    
    def saludar(self):
        print("Hola, bienvenido mi nombre es: ", self.nombre)
        
estudiante1=Persona("Kevin",27)
estudiante2=Persona("Juan",25)
estudiante3=Persona("Jose",30)
estudiante4=Persona("Maria",22)
print("El estudiante seleccionado es: ",estudiante1.nombre)
print(estudiante1.saludar())
print("El estudiante seleccionado es: ",estudiante4.nombre)
print(estudiante4.saludar())
print("La edad del estudiante 2 es : ",estudiante2.edad)

class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad= edad
    
    def comer(self):
        comida=input("Quiero comida")
        if comida== "":
            print("Necesito comida para sobrevivir")
        else:
            print("Muchas gracias")

perro=Animal("Cachuchin",2)
gato=Animal("Olivia",3)
caballo=Animal("Paco",1)

print("Seleccione al animal que desea alimentar")
print("Perro")
print("Gato")
print("Caballo")
seleccion=input("A que animal desea alimentar?")
if seleccion== "Perro":
    print("El animal selccionado es un perro de nombre: ", perro.nombre, "de edad: ", perro.edad, "años")
    perro.comer()
elif seleccion== "Gato":
    print("El animal selccionado es un gato de nombre: ", gato.nombre, "de edad: ", gato.edad, "años")
    gato.comer()
elif seleccion== "Caballo":
    print("El animal selccionado es un caballo de nombre: ", caballo.nombre, "de edad: ", caballo.edad, "años")
    caballo.comer()
else:
    print("No se tiene registros de ese animal")
