import serial
from find_arduino import find_arduino
from tkinter import *

porta = find_arduino()  # Criar area para selecionar porta no tkinter, OptionMenu

root = Tk()
root.geometry("200x200")

selected_port = StringVar()
selected_port.set(porta[0] if porta else "")  # Set the default option

dropdown = OptionMenu(root, selected_port, *porta)
dropdown.pack()

root.mainloop()


try:
    arduino = serial.Serial(porta, 115200, timeout=1)
    print("Arduino está conectado.")
except serial.SerialException:
    print("Não foi possível conectar ao Arduino. Verifique a conexão e tente novamente.")
finally:
    if arduino.isOpen():
        arduino.close()
