from pyfirmata import Arduino
import utilities
import serial
import time


def led(porta: str, opc: int, tempo1: float, tempo2: float = None, num_pulse: int = None):
    uno = Arduino(porta)
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
