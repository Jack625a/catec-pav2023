precios={"Estudiante":10, "AdultoMayor":15, "ClienteRegular":50}
x=50*0.20 #estudiante
y=50*0.30 #adulto mayor
z=50*1 #cliente regular
edad= int(input("Ingrese un edad"))
if edad <30:
    print("El precio descontado por estudiante es de:", x)
    x=50*0.20
elif edad >=60:
    print("El precio descontado por persona Adulto Mayor es de:", y)
else:
    print("El precio por ClienteRegular es de:", z)
    