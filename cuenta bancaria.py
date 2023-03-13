class cuentabancaria:
    def __init__(self,titular,saldo,contraseña):
        self.titular=titular
        self.saldo=saldo
        self.contraseña=contraseña
    def depositar(self):
        cantidad=float(int("ingrese el monto a depositar: "))
        self.saldo +=cantidad
        print("se ha depositado",cantidad,"bs","de la cuenta del titular: ",self.titular)
    def retirar(self):
        cantidad=float(int("ingrese el monto a retirar: "))
        if self.saldo>= cantidad:
            self.saldo -=cantidad
            print("se ha retirado",cantidad,"bs","de la cuenta del titular ",self.titular)
        else:
            print("saldo insuficiente en la cuenta")
            return 0
    def saldo(self):
        print("el saldo total es: ",cuenta.saldo)
#
cuenta1=cuentabancaria("kevin arroyo",25009,"123")
cuenta2=cuentabancaria("brandon choque",23200,"papita")
cuenta3=cuentabancaria("davin ancachi",24500,"456")
cuenta4=cuentabancaria("nayeli alvarado",25500,"0423")
cuenta5=cuentabancaria("david copa",32500,"1265")
cuenta6=cuentabancaria("limberth copa",52500,"1634")
cuenta7=cuentabancaria("jhonatan garcia",12500,"6545")

contraseña=input("ingrese su contraseña: ")
if contraseña== cuenta1.contraseña:
    cuenta=cuenta1
elif contraseña== cuenta2.contraseña:
    cuenta=cuenta2
elif contraseña== cuenta3.contraseña:
    cuenta=cuenta3
elif contraseña== cuenta4.contraseña:
    cuenta=cuenta4
elif contraseña== cuenta5.contraseña:
    cuenta=cuenta5
elif contraseña== cuenta6.contraseña:
    cuenta=cuenta6
elif contraseña== cuenta7.contraseña:
    cuenta=cuenta7
else:
    print("contraseña no valida")
#
operacion=input("ingrese la operacion que desea ralizar: d=deposito - r=retiro - v=ver saldo: ")
if operacion== "d":
    cuenta.depositar()
elif operacion== "r":
    cuenta.retirar()
elif operacion== "v":
    cuenta.saldo()
else:
    print("error debe selecionar una opcion valida")