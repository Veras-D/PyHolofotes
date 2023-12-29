from pyfirmata import Arduino
import utilities
import time


def led(uno, opc, tempo1, tempo2, num_pulse):
    match opc:
        case 1:
            print('Pulso Unico')
            tempo1 = float(input("Escolha o tempo de pulso (Em segundos): "))
            uno.digital[2].write(1)
            time.sleep(tempo1)
            print('Ligado')
            uno.digital[2].write(0)
        case 2:
            for i in range(0, num_pulse):
                print('Pulso Periodico')
                uno.digital[2].write(1)
                print('Ligado')
                time.sleep(tempo1)

                uno.digital[2].write(0)
                print('Desligado')
                time.sleep(tempo2)
