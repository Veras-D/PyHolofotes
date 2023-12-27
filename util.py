import serial
import serial.tools.list_ports


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
        print("Não foi possível conectar ao Arduino. Verifique a conexão e tente novamente.")
        pass

# arduino_port = find_arduino()
# print(arduino_port)
# if arduino_port is not None:
#     print(f"Arduino encontrado na porta {arduino_port}")
# else:
#     print("Arduino não encontrado")
