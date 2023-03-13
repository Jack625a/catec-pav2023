#persona
class persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad=edad

    def saludar(self):
        print("hola bienvenido mi nombre es: ",self.nombre)

estudiante1=persona("brandon",23)
estudiante2=persona("mubafex",25)
estudiante3=persona("maria",32)
estudiante4=persona("jose",22)
print("el estudiante selecionado es: ",estudiante1.nombre)
print(estudiante1.saludar())
print("el estudiante selecionado es: ",estudiante2.nombre)
print(estudiante2.saludar)
print("la edad del estudiante es: ",estudiante2.edad)


#animal
class animal:
    def __init__(self,nombre,raza):
        self.nombre= nombre
        self.raza=raza

    def presentarse(self):
        print("hola mi raza es: ", self.raza)

animal1.animal
