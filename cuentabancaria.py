class cuentabancariaautomatizada:
    def __init__(self,titular,saldo,password):
        self.titular=titular
        self.saldo=saldo
        self.password=password
    def depositar(self):
        cantidad=int(input("ingrese la cantidad que desea depositar: "))
        self.saldo += cantidad
        print("se a depositado: ",cantidad,"bs","de la cuenta del titular: ", self.titular, "EL SALDO TOTAL ES: ", self.saldo)
    def retirar(self):
        cantidad=int(input("ingrese la cantidad de dinero que desea retirar: "))
        if self.saldo >=cantidad:
            self.saldo -= cantidad
            print("se a retirado  ", cantidad,"bs","de la cuenta del titular: ",self.titular,"EL SALDO TOTAL ES: ", self.saldo)
        else:
            print("saldo insuficiente en la cuenta: ")
            return 0
    def versaldo(self):
        print("su saldo disponible en su cuenta es: ",self.saldo,"bs")
    def salir(self):
        print("gracias por usar el banco: ",)
        
    def buscar_cuenta(self,password):
        if self.password==contraseña:
            return self
        else:
            return None

#crear lista de usuarios
cuentas=[
    cuentabancariaautomatizada("brandon choque",10000,"123"),
    cuentabancariaautomatizada("kevin arroyo",15000,"456"),
    cuentabancariaautomatizada("david ancachi",10000,"789"),
    cuentabancariaautomatizada("david copa ",11000,"145"),
    cuentabancariaautomatizada("limberth garcia ",12000,"852")
]
#crear un bluke para comprovar los accesos mediante contraseña
while True:
    contraseña=input("ingrese su contraseña para ingresar a su cuenta: ")
    cuenta_encontrada=None
    for cuenta in cuentas:
        cuenta_encontrada=cuenta.buscar_cuenta(contraseña)
        if cuenta_encontrada:
            break
    if cuenta_encontrada is None:
        print("Error contraseña incorrecta. Intente nuevamente gil ")
    else:
        print("depositar= D")
        print("retirar= R")
        print("ver saldo= V")
        print("salir= S")
        opcion=input("Selecione la operacion que desea realizar \n")
        if opcion== "D":
           # cantidad=int(input("ingrese el monto que desea depositar: "))
            cuenta_encontrada=cuenta.depositar()
        elif opcion== "R":
            #cantidad=int(input("ingrese el monto que desea retirar: "))
            cuenta_encontrada=cuenta.retirar()
        elif opcion== "V":
            cuenta_encontrada.versaldo()
            #print("el saldo disponible es: ",self.saldo,"bs")
        elif opcion== "S":
            cuenta_encontrada.salir()
            break
        else:
            print("opcion invalida, debe realizar una opcion invalida")
        






