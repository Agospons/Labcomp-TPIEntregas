while True:
    print("Bienvenido al sistema de medicion de la empresa, donde a su pedido le entregamos todo lo necesario "
          "para su proyecto :D ")

    Telefono = int(input("Ingrese su numero de telefono para el registro de clientes: "))
    nombre = input("Ingrese su nombre para el registro de clientes: ")
    e = open("lista_clientes.txt", "a")
    e.write("Cliente 3: ")
    e.write("Nombre: " + nombre + "\n")
    e.write("Telefono: " + str(Telefono) + "\n")
    print("Gracias por registrarse en la lista de clientes del sistema :D")

    longitud = int(input("Ingrese la longitud de la superficie a colocar el hormigon: "))
    ancho = int(input("Ingrese el ancho de la superficie del hormigon: "))
    espesor = float(input("Ingrese el espesor del hormigon: "))
    volumen = longitud * ancho * espesor

    while True:
        medida = int(input("\nIntroduzca la unidad de medida que utilizara: precione 1 para "
                           "unidad de sistema universal "
                           "(m, m2, m3, kg). O precione 2 para la unidad de sistema ingles "
                           "(pie, yarda, pulgada, libra, onza) "))
        if medida == 1:

            resistencia = int(input("Ingrese la resistencia que desea tener (kg, m3, litros) "))

            if resistencia <= 105:  ##FUNCIONA
                arena = volumen * 0.5
                grava = volumen * 1.0
                agua = volumen * 160
                cemento = (volumen * 210) * 1.05

            if resistencia <= 140 and resistencia > 105:  ##funciona
                arena = volumen * 0.63
                grava = volumen * 0.84
                agua = volumen * 170
                cemento = (volumen * 260) * 1.05

            if resistencia <= 175 and resistencia > 140:  ## no lo printea con 175 y lo imprime mal al resto
                arena = volumen * 0.48
                grava = volumen * 0.96
                agua = volumen * 170
                cemento = (volumen * 300) * 1.05

            if resistencia <= 210 and resistencia > 175:  ## no lo printea
                cemento = (volumen * 350) * 1.05
                arena = volumen * 0.56
                grava = volumen * 0.84
                agua = volumen * 180

            if resistencia > 210 and resistencia <= 246:  ##FUNCIONA
                arena = volumen * 0.67
                grava = volumen * 0.67
                agua = volumen * 220
                cemento = (volumen * 420) * 1.05
            break

        if medida == 2:

            resistencia = int(input("Ingrese la resistencia que desea tener (pulgadas, pies3, galeones )"))

            if resistencia <= 1500:
                arena = volumen * 5.38
                grava = volumen * 10.76
                agua = volumen * 42.26

            if resistencia <= 2000 and resistencia > 1500:
                arena = volumen * 6.78
                grava = volumen * 9.04
                agua = volumen * 44.9

            if resistencia <= 2500 and resistencia > 2000:
                arena = volumen * 5.16
                grava = volumen * 10.33
                agua = volumen * 44.9

            if resistencia <= 3000 and resistencia > 2500:
                arena = volumen * 6.02
                grava = volumen * 9.04
                agua = volumen * 47.55

            if resistencia <= 3500 and resistencia > 3000:
                arena = volumen * 7.21
                grava = volumen * 7.21
                agua = volumen * 55.11
            break

    ticket = open("ticket.txt", "a")
    ticket.write("--------------TICKET--------------")
    ticket.write(
        "\nSu valor de volumen calculado fue " + str(volumen) + "\nEl Resultado a base de sus necesidades fue: ")
    ticket.write(
        "\n- Arena: " + str(arena) + "\n- Grava: " + str(grava) + "\n- Cemento: " + str(cemento)
        + "\n- Agua: " + str(agua))

    respuesta = int(input("¿Desea terminar el proceso del sistema? si: 1 / no: 2 "))
    if respuesta == 1:
        print("Gracias por confiar :D \n¡Vuelva Pronto!")
    break

