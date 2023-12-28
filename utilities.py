from serial import *
import serial.tools.list_ports
from tkinter import *

arduino = None


def find_arduino():
    arduino_ports = serial.tools.list_ports.comports()
    ports = ["Selecione a porta"]
    for port in arduino_ports:
        ports.append(port.device)
    return ports


def arduino_conected(portas):
    global arduino
    try:
        arduino = serial.Serial(portas, 115200, timeout=1)
        print("Arduino está conectado.")
    except serial.SerialException:
        print("Não foi possível conectar ao Arduino. Verifique a conexão e tente novamente.")  # Fazer esses textos aparecerem no programa
        pass


def on_closing():
    global arduino
    if arduino is not None:
        arduino.close()
        print('fechado')
