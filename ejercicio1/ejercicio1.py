# Programa para leer cordenadas de un plano cartesiano e indicar el cuadrante


print("\x1b[;31m"+"-------------------------------------------------------"+'\033[0;m')
print("\033[4;35m"+"Programa para indicar el cuadrante de  unas coordenadas"+'\033[0;m')
print("\x1b[;31m"+"-------------------------------------------------------"+'\033[0;m')

#input

x = int(input("Digite la coordenada x: "))
y = int(input("Digite la coordenada y: "))

# processing

if x == 0:
    if y == 0:
        msj = ("Las coordenadas corresponden al origen")
    else:
        msj = ("Las coordenadas corresponden al eje y")
else:
    if y == 0:
        msj = ("Las coordenadas corresponden al eje x")
    else:
        if x > 0:
            if y > 0:
                msj = ("Las coordenadas corresponden al cuadrante 1")
            else:
                msj = ("Las coordenadas corresponden al cuadrante 4")
        else:
            if y < 0:
                msj = ("Las coordenadas corresponden al cuadrante 3")
            else:
                msj = ("Las coordenadas corresponden al cuadrante 2")
# output
print (msj)
        