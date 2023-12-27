import serial
from utilities import *
from tkinter import *

portas = find_arduino()  # Criar area para selecionar porta no tkinter, OptionMenu

root = Tk()
root.geometry("200x200")

selected_port = StringVar()
selected_port.set("Selecione a porta")

dropdown = OptionMenu(root, selected_port, "Selecione a porta", *portas, command=arduino_conected)
# dropdown = OptionMenu(root, selected_port, "Selecione a porta", *portas, command=lambda: arduino_conected(selected_port.get()))
dropdown.pack()

root.bind("<Destroy>", on_closing())

root.mainloop()

# arduino.write(b'1')  # esse b é de binario, equivalente high
# se o usuario fechar a janela -> arduino.close()