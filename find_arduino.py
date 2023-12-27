import serial.tools.list_ports


def find_arduino():
    arduino_ports = serial.tools.list_ports.comports()
    for port in arduino_ports:
        ports = []
        ports.append(port.device)
        return ports
    return None


# arduino_port = find_arduino()
# print(arduino_port)
# if arduino_port is not None:
#     print(f"Arduino encontrado na porta {arduino_port}")
# else:
#     print("Arduino não encontrado")
