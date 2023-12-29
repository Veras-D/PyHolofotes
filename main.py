import serial
from utilities import *
from tkinter import *
import customtkinter as ctk

portas = find_arduino()


def Arduino(porta):
    if porta != "Selecione a porta":
        Arduino = serial.Serial(porta, 115200, timeout=1)
        return Arduino
    else:
        return None


root = ctk.CTk()
root.title("PyHolofotes")
root.geometry("300x120")
root.resizable(False, False)
ctk.set_appearance_mode("dark")

selected_port = StringVar()
selected_port.set("Selecione a porta")

dropdown = ctk.CTkOptionMenu(root, variable=selected_port, values=portas,
                             command=lambda port=None: arduino_conected(selected_port.get()))
dropdown.set(portas[0])
dropdown.pack()


def open_new_page():
    for widget in root.winfo_children():
        widget.pack_forget()

    root.geometry("500x500")
    root.resizable(True, True)
    main_label = ctk.CTkLabel(root, text=f"Porta: {selected_port.get()}\nArduino: {Arduino(selected_port.get())}")
    main_label.pack()
    root.eval('tk::PlaceWindow . right')


button = ctk.CTkButton(root, text="Continuar", command=open_new_page)  # Usuario só pode continuar se lelecionar uma porta
button.pack(pady=30)

root.bind("<Destroy>", on_closing())

porta = selected_port.get()
if porta != "Selecione a porta":  # Colocar condição de botão continuar
    arduino = Serial(porta, 115200, timeout=1)

root.mainloop()

# arduino.write(b'1')  # esse b é de binario, equivalente high
# se o usuario fechar a janela -> arduino.close()