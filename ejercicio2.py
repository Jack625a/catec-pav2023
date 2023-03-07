precios={"estudiante":10,"adultomayor":15,"clienteregular":50}
x=500.20
y=50*0.20
z=50*0
edad= int(input("ingrese la edad"))
if edad <30:
    print("el precio descontado es: ", x)
    x=50*0.20
elif edad>60:
    print("el precio con descuento para mayor es: ", y)
else:
    print("el precio por regular es: ", z)
    