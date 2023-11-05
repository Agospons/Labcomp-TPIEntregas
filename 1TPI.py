print("Bienvenido al sistema de medicion de la empresa, donde a su pedido le entregamos todo lo necesario "
      "para su proyecto :D ")

longitud = int(input("Ingrese la longitud de la superficie a colocar el hormigon "))
ancho = int(input("Ingrese el ancho de la superficie del hormigon"))
espesor = float(input("Ingrese el espesor del hormigon "))
volumen = longitud * ancho * espesor

while True:
    medida = int(input("Introduzca la unidad de medida que utilizara: precione 1 para unidad de sistema universal "
                       "(m, m2, m3, kg). O precione 2 para la unidad de sistema ingles "
                       "(pie, yarda, pulgada, libra, onza) "))
    if medida == 1:

        resistencia = int(input("Ingrese la resistencia que desea tener (pulgadas o kg) "))
        if resistencia >= 105:
            arena = volumen * 0.5
            grava = volumen * 1.0
            agua = volumen * 160
            ###cemento
        elif 105 > resistencia >= 140:
            arena = volumen * 0.63
            grava = volumen * 0.84
            agua = volumen * 170
            cemento = volumen * 260
        elif 140 > resistencia >= 175:
            arena = volumen * 0.48
            grava = volumen * 0.96
            agua = volumen * 170
            ## cemento
        elif 170 > resistencia >= 210:
            cemento = (volumen * 7) * 1.05
            arena = volumen * 0.56
            grava = volumen * 0.84
            agua = volumen * 180
        elif 210 > resistencia >= 246:
            arena = volumen * 0.67
            grava = volumen * 0.67
            agua = volumen * 220
            ## cemento

    elif medida == 2:
        resistencia = int(input("Ingrese la resistencia que desea tener (pulgadas o kg) "))
        if resistencia > 1500:
            arena = volumen * 0.5
            grava = volumen * 1.0
            agua = volumen * 160
            ###cemento


## hormigon = float(input("Ingrese la cantidad total de hormigon que necesita "))

###medida = input("Ingrese la unidad de medida que desea utilizar para este proyecto: metros = 1 "
###            ", centimetros = 2, pies = 3, pulgada = 4 ")
###if medida == 1 or medida == 2:

###ingresar el valor del cemento arena y grava para el presupuesto estimado

### calculo(volumen ) = longitud x ancho x espesor
### se necesita saber el tipo de concreto
### resultado x sacos x

yoongitkm = int(input("¿Desea hacer un presupuesto estimado para los materiales? si = 1 "
                        "no = 2 "))

if presupuesto == 1:
    cemento = int(input("En ese caso, ingrese el valor estimado del cemento (por bolsa) "))
    arena = int(input("Arena (por bolsa) "))
    grava = int(input("Grava (por metro) "))
elif presupuesto == 2:
    print("Entendido")

presupuesto = input("¿Desea hacer un presupuesto estimado para los materiales? si/no ")
si = 1
no = 0

if presupuesto == si:
    cemento = int(input("En ese caso, ingrese el valor estimado del cemento (por bolsa) "))
    arena = int(input("Arena (por bolsa) "))
    grava = int(input("Grava (por metro) "))
elif presupuesto == no:
    print("Entendido")
