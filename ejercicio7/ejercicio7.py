# input

a = int(input("Digite el primer numero entero: "))
b = int(input("Digite el segundo numero entero: "))
c = int(input("Digite el tercer numero entero: "))

#processing

if a + b == c:
    msj = ("La suma de " + str(a) + " y " + str(b) + " es igual a " + str(c))
else:
    msj = ("La suma de " + str(a) + " y " + str(b) + " no es igual a " + str(c))
#output
print (msj)
