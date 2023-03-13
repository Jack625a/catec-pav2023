class CuentaBancaria:
    def __init__(self,titular,saldo,contrasena):
        self.titular=titular
        self.saldo=saldo
        self.contrasena=contrasena
    def depositar(self):
        cantidad=float(input("Ingrese la cantidad de dinero que desea depositar: "))
        self.saldo +=cantidad
        print("Se ha depositado ",cantidad,"Bs", "De la cuenta del titular: ",self.titular , "El saldo Total es: ", self.saldo)
    def retirar(self):
        cantidad=float(input("Ingrese la cantidad de dinero que desea retirar: "))
        if self.saldo >=cantidad:
            self.saldo -=cantidad
            print("Se ha retirado ",cantidad,"Bs", "De la cuenta del titular: ",self.titular, "El saldo Total es: ", self.saldo)
        else:
            print("Saldo insuficiente en la cuenta")
            return 0

#Crear los objetos de la clase Cuenta Bancaria
cuenta1=CuentaBancaria("Kevin Arroyo",2500,"123")
cuenta2=CuentaBancaria("Brandom Choque",15000,"papita")
cuenta3=CuentaBancaria("David Ancachi",10000,"456")
cuenta4=CuentaBancaria("Nayeli Alvarado",14000,"789")
cuenta5=CuentaBancaria("David Copa",14000,"987")
cuenta6=CuentaBancaria("Limbeth Copa",15000,"852")
cuenta7=CuentaBancaria("Jhonathan Garcia",11000,"412")

contrasena=input("Ingrese su contraseña: ")
if contrasena == cuenta1.contrasena:
    cuenta=cuenta1
elif contrasena == cuenta2.contrasena:
    cuenta=cuenta2
elif contrasena == cuenta3.contrasena:
    cuenta=cuenta3
elif contrasena == cuenta4.contrasena:
    cuenta=cuenta4
elif contrasena == cuenta5.contrasena:
    cuenta=cuenta5
elif contrasena == cuenta6.contrasena:
    cuenta=cuenta6
elif contrasena == cuenta7.contrasena:
    cuenta=cuenta7
else:
    print("Contraseña invalida")   

#mostrar opciones para realiZAr en la cuenta bancaria
operacion=input("Ingrese la operación que desea realiZar - D=Deposito - R=Retiro: ")
if operacion=="D":
    cuenta.depositar()
elif operacion == "R":
    cuenta.retirar()
else:
    print("Error debe seleccionar una opción valida")

