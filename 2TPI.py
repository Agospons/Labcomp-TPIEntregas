print("Bienvenido al sistema de medicion de la empresa, donde a su pedido le entregamos todo lo necesario "
      "para su proyecto :D ")

longitud = int(input("Ingrese la longitud de la superficie a colocar el hormigon "))
ancho = int(input("Ingrese el ancho de la superficie del hormigon "))
espesor = float(input("Ingrese el espesor del hormigon "))
volumen = longitud * ancho * espesor

resistencia = int(input("Ingrese la resistencia que desea tener "))
if resistencia <= 105: ##FUNCIONA
    arena = volumen * 0.5
    grava = volumen * 1.0
    agua = volumen * 160
    cemento = (volumen * 5) * 1.05
    ###cemento
    print(cemento, arena, grava, agua)
if resistencia <= 140 and resistencia > 105: ##funciona
    arena = volumen * 0.63
    grava = volumen * 0.84
    agua = volumen * 170
    cemento = (volumen * 6) * 1.05
    print(cemento, arena, grava, agua)
if resistencia <= 175 and resistencia > 140: ## no lo printea con 175 y lo imprime mal al resto
    arena = volumen * 0.48
    grava = volumen * 0.96
    agua = volumen * 170
    cemento = (volumen * 6) * 1.05
    ## cemento
    print(cemento, arena, grava, agua)
if resistencia <= 210 and resistencia > 175:  ## no lo printea
    cemento = (volumen * 7) * 1.05
    arena = volumen * 0.56
    grava = volumen * 0.84
    agua = volumen * 180
    print(cemento, arena, grava, agua)
if resistencia > 210 and resistencia <= 246: ##FUNCIONA
    arena = volumen * 0.67
    grava = volumen * 0.67
    agua = volumen * 220
    cemento = (volumen * 9) * 1.05
    print(cemento, arena, grava, agua)
