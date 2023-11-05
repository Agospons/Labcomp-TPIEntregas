print("Bienvenido al sistema de medicion de la empresa, donde a su pedido le entregamos todo lo necesario "
      "para su proyecto :D ")

longitud = int(input("Ingrese la longitud de la superficie a colocar el hormigon "))
ancho = int(input("Ingrese el ancho de la superficie del hormigon "))
espesor = float(input("Ingrese el espesor del hormigon "))
volumen = longitud * ancho * espesor

resistencia = int(input("Ingrese la resistencia que desea tener "))
if resistencia >= 1500:
    arena = volumen * 5.38
    grava = volumen * 10.76
    agua = volumen * 42.26
if 1500 > resistencia <= 2000:
    arena = volumen * 6.78
    grava = volumen * 9.04
    agua = volumen * 44.9
if 2000 > resistencia <= 2500:
    arena = volumen * 5.16
    grava = volumen * 10.33
    agua = volumen * 44.9
if 2500 > resistencia <= 3000:
    arena = volumen * 6.02
    grava = volumen * 9.04
    agua = volumen * 47.55
if 3000 > resistencia <= 3500:
    arena = volumen * 7.21
    grava = volumen * 7.21
    agua = volumen * 55.11
