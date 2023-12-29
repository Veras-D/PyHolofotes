from pyfirmata import Arduino, util
import time

# Transformar isso em uma função, def led(uno, opc, tempo1, tempo2, num_pulse):

uno = Arduino("/dev/ttyUSB0")

while True:
    print('='*32)
    print("""=    [ 1 ] - Pulso Único       =
=    [ 2 ] - Pulso Periodico   =
=    [ 0 ] - Exit              =""")
    print('='*32)
    opc = int(input("Escolha uma opção: "))

    match opc:
        case 1:
            print('Pulso Unico')
            tempo1 = float(input("Escolha o tempo de pulso (Em segundos): "))
            uno.digital[2].write(1)
            time.sleep(tempo1)
            print('Ligado')
            uno.digital[2].write(0)
        case 2:
            tempo1 = float(input("Escolha o tempo de pulso (Em segundos): "))
            tempo2 = float(input("Escolha o tempo de pausa (Em segundos): "))
            num = int(input("Escolha o numero de pulsos: "))

            for i in range(0, num):
                print('Pulso Periodico')
                uno.digital[2].write(1)
                print('Ligado')
                time.sleep(tempo1)

                uno.digital[2].write(0)
                print('Desligado')
                time.sleep(tempo2)
        case 0:
            break
