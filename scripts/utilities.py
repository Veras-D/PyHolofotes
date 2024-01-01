import serial.tools.list_ports
import customtkinter as ctk
import webbrowser


arduino = None


def frame(root):
    root.update()
    largura = root.winfo_width()
    altura = root.winfo_height()
    x = 15
    y = 0
    return ctk.CTkFrame(root, largura - 2 * x, altura - x).place(x=x, y=y)


def callback(url):
    webbrowser.open_new_tab(url)


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
        print("Não foi possível conectar ao Arduino. Verifique a conexão e tente novamente.")
        pass


def on_closing(event, arduino):
    if event.widget == event.widget.winfo_toplevel():
        if arduino is not None:
            arduino.close()
            print('fechado')
