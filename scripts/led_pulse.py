from pyfirmata import Arduino
import time
import customtkinter as ctk


def led(uno, opc: int, tempo1: float, tempo2: float = None, num_pulse: int = None):
    match opc:
        case 1:
            print('Pulso Unico')
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
