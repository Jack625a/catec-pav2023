class Cuentabancariaautomatizada:
    def __int__(self, titular, saldo,password):
        self.titular=titular
        self.saldo=saldo
        self.password=password
    def depositar(self):
        cantidad=float(input("ingrese la cantidad de dineroque desea depositar"))
        self.saldo +=cantidad
        print("se ha depositado ",cantidad,"bs", "de la cuenta del titular: ",self.titular)
    def retirar(self):
        cantidad=float(input("ingrese la cantidad de dinero qeu desea retirar: "))
        if self.saldo >=cantidad:
            self.saldo -=cantidad
            print("se ha retirado ",cantidad,"bs","de la cuenta del titular: ",self.titular)
        else:
            print("saldo insuficinente en la cuenta")
            return 0 
    def versaldo(self):
        print("ver saldo diponible en su cuenta: ",self.saldo,"bs")
    def buscar_cuenta(self,password):
        if self.password==contrasena:
            return self
        else:
            return None
#crear una lista de usuarios
cuentas=[
    Cuentabancariaautomatizada("kevin arroyo",2500,"123"),
    Cuentabancariaautomatizada("brandon choque",15000,"papita"),
    Cuentabancariaautomatizada("david ancachi",10000,"456"),
    Cuentabancariaautomatizada("nayely albarado",14000,"789"),
    Cuentabancariaautomatizada("david copa",14000,"987"),    
    Cuentabancariaautomatizada("limberth copa",15000,"852"),
    Cuentabancariaautomatizada("jhonatan garcia",11000,"412")
]
#crear un bucle para comprobar los accesos mediante contrasena
while True:
    contrasena=input("ingrese su contrasena para ingresar a su cuenta: ")
    cuenta_encontrada=None
    for cuenta in cuentas:
        cuenta_encontrada=cuenta.buscar_cuenta(contrasena)
        if cuenta_encontrada:
            break 
    if cuenta_encontrada is None:
        print("error contrasena incorresta. intente nuevamente") 
    else:
        print("depositar= D")
        print("retirar= R")
        print("ver saldo= V")
        opcion=input("seleccione la operacion qeu desea reallizar: ")
        if opcion== "D":
            #cantidad=int(input("ingrese la cantidad de dinero que desea depositar"))
            cuenta_encontrada=cuenta.depositar()
        elif opcion== "R":
            #cantidad=int(input("ingrese la cantidad de dinero que desea restirar"))
            cuenta_encontrada=cuenta.retirar()
        elif opcion== "V":
            cuenta_encontrada.versaldo()
            #print("el saldo disponible en su cuenta es de: ",self.saldo,"bs")
        else:
            print("opcion invali.debe seleccionar una operacion disponible")
