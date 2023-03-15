class CuentaBancariaAutomatizada:
    def __init__(self,titular,saldo,password):
        self.titular=titular
        self.saldo=saldo
        self.password=password
    def depositar(self):
        cantidad=int(input("Ingrese la cantidad de dinero que desea depositar: "))
        self.saldo +=cantidad
        print("Se ha depositado ",cantidad,"Bs", "De la cuenta del titular: ",self.titular , "El saldo Total es: ", self.saldo)
    def retirar(self):
        cantidad=int(input("Ingrese la cantidad de dinero que desea retirar: "))
        if self.saldo >=cantidad:
            self.saldo -=cantidad
            print("Se ha retirado ",cantidad,"Bs", "De la cuenta del titular: ",self.titular, "El saldo Total es: ", self.saldo)
        else:
            print("Saldo insuficiente en la cuenta")
            return 0
    def verSaldo(self):
        print("El saldo disponible en su cuenta es: ",self.saldo,"Bs")
    def buscar_cuenta(self,password):
        if self.password==contrasena:
            return self
        else:
            return None
#crear lista de usuarios
cuentas=[
    CuentaBancariaAutomatizada("Kevin Arroyo",25000,"123"),
    CuentaBancariaAutomatizada("Brandom Choque",15000,"papita"),
    CuentaBancariaAutomatizada("David Ancachi",10000,"456"),
    CuentaBancariaAutomatizada("Nayeli Alvarado",14000,"789"),
    CuentaBancariaAutomatizada("David Copa",14000,"987"),
    CuentaBancariaAutomatizada("Limbeth Copa",15000,"852"),
    CuentaBancariaAutomatizada("Jhonathan Garcia",11000,"412")
]
#Crear un bucle para comprobar los accesos mediante contraseña
while True:
    contrasena=input("Ingrese su contraseña para ingresar a su Cuenta: ")
    cuenta_econtrada=None
    for cuenta in cuentas:
        cuenta_econtrada=cuenta.buscar_cuenta(contrasena)
        if cuenta_econtrada:
            break
    if cuenta_econtrada is None:
        print("Error contraseña incorrecta. Intente nuevamente")
    else:
        print("Depositar= D")
        print("Retirar= R")
        print("Ver Saldo= V")
        opcion=input("Selecione la operacion que desea realizar: ")
        if opcion== "D":
            #cantidad=int(input("Ingrese la cantidad de dinero que desea depositar: "))
            cuenta_econtrada.depositar()
        elif opcion== "R":
            #cantidad=int(input("Ingrese la cantidad de dinero que desea retirar: "))
            cuenta_econtrada.retirar()
        elif opcion== "V":
            cuenta_econtrada.verSaldo()
            #print("El saldo disponible en su cuenta es de: ",self.saldo,"Bs")
        else:
            print("Opcion invalida, debe seleccionar una operacion disponible")

            
            
        
