# Programa para indicar el precio de venta de un artículo dado

#input

pre_art = int(input("Digite el precio del artículo: "))

#processing

if pre_art < 3000:
    ganancia = pre_art*0.15
    pre_vent = pre_art + ganancia
else:
    if pre_art > 6000:
        ganancia = 500
        pre_vent = pre_art + ganancia
    else:
        ganancia = pre_art*0.25
        pre_vent = pre_art + ganancia
print ("El precio de venta es" (pre_vent))
