

print("---------------------------------------------------")
print("-----Programa para saber si a es múltiplo de b-----")
print("---------------------------------------------------")

# input

x = int(input("Digite el número a: "))
y = int(input("Digite el número b: "))

# processing

if x % y == 0:
    msj = (str(x) + " si es múltiplo de " + str(y))
else:
    msj = (str(x) + " no es múltiplo de " + str(y))

print(msj)