class cuentabancaria:
    def __init__(self,titular,saldo,contraseña):
        self.titular=titular
        self.saldo=saldo
        self.contraseña=contraseña
    def versaldo(self):
        cantidad=float(input("su saldo total es: "))
        self.saldo==cantidad
        print("su saldo total es: ",self.saldo)
    def depositar(self):
        cantidad=float(input("ingrese la cantidad que desea depositar: "))
        self.saldo += cantidad
        print("se a depositado: ",cantidad,"bs","de la cuenta del titular: ", self.titular, "EL SALDO TOTAL ES: ", self.saldo)
    def retirar(self):
        cantidad=float(input("ingrese la cantidad de dinero que desea retirar: "))
        if self.saldo >=cantidad:
            self.saldo -= cantidad
            print("se a retirado  ", cantidad,"bs","de la cuenta del titular: ",self.titular,"EL SALDO TOTAL ES: ", self.saldo)
        else:
            print("saldo insuficiente en la cuenta: ")
            return 0
        
#crear los objetos de la clase cuenta bancaria
cuenta1=cuentabancaria("brandon choque",2000,"123")
cuenta2=cuentabancaria("kevin arroyo",15000,"456")
cuenta3=cuentabancaria("david ancachi",10000,"789")
cuenta4=cuentabancaria("david copa ",11000,"145")
cuenta5=cuentabancaria("limberth garcia ",12000,"852")

contraseña=input("intrese su contraseña: ")
if contraseña == cuenta1.contraseña:
    cuenta=cuenta1 
elif contraseña == cuenta2.contraseña:
    cuenta=cuenta2
elif contraseña == cuenta3.contraseña:
    cuenta=cuenta3
elif contraseña == cuenta4.contraseña:
    cuenta=cuenta4
elif contraseña == cuenta5.contraseña:
    cuenta=cuenta5  
else:
    print("contraseña incorrecta: ")

#mostrar opciones para realizar en la cuenta bancaria 
operacion=input("ingrese que opcion desea realizar - V=versaldo - D=deposito - R=retiro: ")
if operacion=="D":
    cuenta.depositar()
elif operacion=="R":
    cuenta.retirar()
elif operacion=="V":
    cuenta.versaldo()
else:
    print("error debe selecionar una opcion valida")





