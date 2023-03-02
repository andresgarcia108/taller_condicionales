# Programa para realizar un préstamo bancario

# input

ingresos = int(input("¿Cuáles son sus ingresos mensuales?: "))

# processing

if ingresos > 945200:
    deudas = int(input("¿Cuántas deudas tiene actualmente?: "))
    if deudas == 0:
        msj =("¡Felicidades, su préstamo ha sido aprobado!")
    else:
        msj = ("Lo sentimos, su préstamo ha sido denegado")
else:
    msj = ("Lo sentimos, su préstamo ha sido denegado")
#output
print (msj)