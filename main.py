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
dropdown.pack(pady=5)


def open_new_page():
    if selected_port.get() != portas[0]:
        for widget in root.winfo_children():
            widget.pack_forget()

        root.geometry("500x500")
        root.minsize(500, 200)
        root.resizable(True, True)
        main_label = ctk.CTkLabel(root, text=f"Porta: {selected_port.get()}\nArduino: {Arduino(selected_port.get())}",
                                  wraplength=500)
        main_label.pack()
        root.eval('tk::PlaceWindow . right')
        root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))

        pulso_unico_bnt = ctk.CTkButton(root, text="PULSO ÚNICO")
        pulso_periodico_bnt = ctk.CTkButton(root, text="PULSO PERIÓDICO")
        pulso_unico_bnt.pack(pady=20)
        pulso_periodico_bnt.pack()

    else:
        port_error = ctk.CTkToplevel(root)
        port_error.title("Erro!")
        port_error.geometry("200x100")
        port_error.resizable(False, False)
        error_label = ctk.CTkLabel(port_error, text="Você deve selecionar uma porta para iniciar o programa!",
                                   wraplength=200)
        error_label.pack()
        error_button = ctk.CTkButton(port_error, text="OK", command=port_error.destroy,
                                     fg_color="red", hover_color="#821D1A")
        error_button.pack(pady=10)
        port_error.mainloop()



button = ctk.CTkButton(root, text="Continuar", command=open_new_page)  # Usuario só pode continuar se selecionar uma porta
button.pack(pady=25)

porta = selected_port.get()
root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))

root.mainloop()

# arduino.write(b'1')  # esse b é de binario, equivalente high
# se o usuario fechar a janela -> arduino.close()