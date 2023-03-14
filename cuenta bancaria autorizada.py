class cuentabancariaAutomatizada:
    def __init__(self,titular,saldo,password):
        self.titular=titular
        self.saldo=saldo
        self.password=password
    def depositar(self):
        cantidad=int(input("ingrese el monto a depositar: "))
        self.saldo +=cantidad
        print("se ha depositado",cantidad,"bs","de la cuenta del titular: ",self.titular)
    def retirar(self):
        cantidad=int(input("ingrese el monto a retirar: "))
        if self.saldo >=cantidad:
            self.saldo -=cantidad
            print("se ha retirado",cantidad,"bs","de la cuenta del titular ",self.titular)
        else:
            print("saldo insuficiente en la cuenta")
            return 0
    def versaldo(self):
        print("el saldo disponible es: ",self.saldo,"bs")
    def buscar_cuenta(self,password):
        if self.password== contraseña:
            return self
        else:
            return None
#
cuentas=[
    cuentabancariaAutomatizada("1.- kevin arroyo",25565,"123"),
    cuentabancariaAutomatizada("2.- david copa",25355,"2563"),
    cuentabancariaAutomatizada("3.- nayeli vargas",21455,"1263"), 
    cuentabancariaAutomatizada("4.- jhonatan garcia",22585,"1823"),
    cuentabancariaAutomatizada("5.- yelsit ancachi",23575,"1293"),
    cuentabancariaAutomatizada("6.- limberth copa",25955,"1233")
]
#creamos un bucle 
while True:
    contraseña=input("ingrese su contraseña para ingresar a su cuenta: ")
    cuenta_encontrada=None
    for cuenta in cuentas:
        cuenta_encontrada=cuenta.buscar_cuenta(contraseña)
        if cuenta_encontrada:
            break 
    if cuenta_encontrada is None:
        print("error, contraseña incorrecta. intente nuevamente")
    else:
        print("depositar = d")
        print("retirar = r")
        print("ver saldo = v")
        opcion=input("seleccione la operacion que desea realizar: \n")
        if opcion== "d":
            #cantidad=int(input("ingrese la cantidad de dinero que desea depositar: "))
            cuenta_encontrada.cuenta.depositar()
        elif opcion== "r":
            #cantidad=int(input("ingrese la cantidad de dinero que desea retirar: "))
            cuenta_encontrada.cuenta.retirar()
        elif opcion== "v":
            cuenta_encontrada.versaldo()
        else:
            print("opcion invalida, debe seleccionar una operacion disponible ")