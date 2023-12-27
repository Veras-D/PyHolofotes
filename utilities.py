from serial import *
import serial.tools.list_ports
from tkinter import *


def find_arduino():
    arduino_ports = serial.tools.list_ports.comports()
    ports = []
    for port in arduino_ports:
        ports.append(port.device)
    return ports


def arduino_conected(portas):
    try:
        arduino = serial.Serial(portas, 115200, timeout=1)
        print("Arduino está conectado.")
    except serial.SerialException:
        print("Não foi possível conectar ao Arduino. Verifique a conexão e tente novamente.")  # Fazer esses textos aparecerem no programa
        pass


def on_closing():
    if 'arduino' in globals():  # Verificar se essa condição pode acontecer
        Serial.close()  # verificar se esta funcionando, aparentemente não esta
        print('fechado')

# arduino_port = find_arduino()
# print(arduino_port)
# if arduino_port is not None:
#     print(f"Arduino encontrado na porta {arduino_port}")
# else:
#     print("Arduino não encontrado")
