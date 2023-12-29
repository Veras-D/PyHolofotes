from serial import *
import serial.tools.list_ports
from tkinter import *
import webbrowser
import base64


arduino = None


def callback(url):
    webbrowser.open_new_tab(url)


def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')



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


def on_closing(event, arduino):
    if event.widget == event.widget.winfo_toplevel():
        if arduino is not None:
            arduino.close()
            print('fechado')
