import serial
from utilities import *
from tkinter import *
import customtkinter as ctk

portas = find_arduino()

root = ctk.CTk()
root.title("PyHolofotes")
root.geometry("300x150")

selected_port = StringVar()
selected_port.set("Selecione a porta")

dropdown = ctk.CTkOptionMenu(root, variable=selected_port, values=portas, command=lambda port=None: arduino_conected(selected_port.get()))
dropdown.set(portas[0])
dropdown.pack()


def open_new_window():
    new_window = ctk.CTkToplevel(root)
    ctk.CTkLabel(new_window, text="Esta é a nova janela").pack()


button = ctk.CTkButton(root, text="Continuar", command=open_new_window)
button.pack(pady=30)

root.bind("<Destroy>", on_closing())

porta = selected_port.get()
if porta != "Selecione a porta":  # Colocar condição de botão continuar
    arduino = Serial(porta, 115200, timeout=1)

root.mainloop()
print(selected_port.get())
print(arduino)

# arduino.write(b'1')  # esse b é de binario, equivalente high
# se o usuario fechar a janela -> arduino.close()