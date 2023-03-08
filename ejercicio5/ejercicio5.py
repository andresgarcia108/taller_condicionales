# Programa para calcular el gasto del agua

print ("----------------------------------------")
print ("-------Calcular el gasto del agua-------")
print ("----------------------------------------")

# input
gasto  = int(input("Digite el gasto del agua en metros cuadrados: "))

# processing

if gasto < 50:
    precio = 10000
    msj = ("El precio del agua es: ", (precio))
else:
    if gasto < 200:
         precio = (gasto - 50) *2000 + 10000
         msj = ("El precio del agua es: ", (precio))
    else:
        if gasto >200:
                precio = (gasto - 50) *3000 +10000
                msj = ("El precio del agua es: ", (precio))
        else:
            precio = (gasto - 50) *2000 + 10000
    print (msj)