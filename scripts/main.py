import serial
from scripts.utilities import *
from tkinter import *
import customtkinter as ctk
from scripts.led_pulse import led


# Testando github actions 4
def Arduino(porta):
    if porta != "Selecione a porta":
        Arduino = serial.Serial(porta, 115200, timeout=1)
        return Arduino
    else:
        return None


def open_new_page():
    if selected_port.get() != portas[0]:
        for widget in root.winfo_children():
            widget.pack_forget()

        root.geometry("500x500")
        root.title("Seleção de pulso")
        root.minsize(500, 250)
        root.resizable(True, True)
        main_label = ctk.CTkLabel(root, text=f"Porta: {selected_port.get()}\nArduino: {Arduino(selected_port.get())}",
                                  wraplength=500)
        main_label.pack()
        root.eval('tk::PlaceWindow . right')
        root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))

        pulso_unico_bnt = ctk.CTkButton(root, text="PULSO ÚNICO", command=pulso_unico,
                                        fg_color="purple", hover_color="#8B008B")
        pulso_periodico_bnt = ctk.CTkButton(root, text="PULSO PERIÓDICO", command=pulso_periodico,
                                            fg_color="purple", hover_color="#8B008B")
        pulso_unico_bnt.pack(pady=20)
        pulso_periodico_bnt.pack()

        instagram_link = ctk.CTkLabel(root, text="Instagram", text_color="magenta", cursor="hand2")
        github_link = ctk.CTkLabel(root, text="GitHub", text_color="magenta", cursor="hand2")

        instagram_link.bind("<Button-1>", lambda e: callback("https://www.instagram.com/veras_programmer"))
        github_link.bind("<Button-1>", lambda e: callback("https://www.github.com/Veras-D"))

        github_link.pack(side=ctk.BOTTOM)
        instagram_link.pack(side=ctk.BOTTOM)

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


def pulso_unico():
    for widget in root.winfo_children():
        widget.pack_forget()

    root.title("Pulso Único")
    pulse_label = ctk.CTkLabel(root, text="Pulso Único", wraplength=500)
    pulse_label.pack(pady=10)
    tempo1_entry = ctk.CTkEntry(root, placeholder_text="Tempo de Pulso (s)", justify='center')
    tempo1_entry.pack()

    def led_pulse():
        if tempo1_entry.get().strip() != "":
            led(porta=selected_port.get(), opc=1, tempo1=float(tempo1_entry.get()))
            open_new_page()
        else:
            port_error = ctk.CTkToplevel(root)
            port_error.title("Erro!")
            port_error.geometry("200x100")
            port_error.resizable(False, False)
            error_label = ctk.CTkLabel(port_error, text="Preencha os valores adequadamente!",
                                       wraplength=200)
            error_label.pack()

            error_button = ctk.CTkButton(port_error, text="OK", command=port_error.destroy,
                                         fg_color="red", hover_color="#8B008B")
            error_button.pack(pady=10)
            port_error.mainloop()

    start_bnt = ctk.CTkButton(root, text="Start Pulse", command=lambda port=None: led_pulse(),
                              fg_color="purple", hover_color="#8B008B")
    start_bnt.pack(pady=10)
    goHome = ctk.CTkButton(root, text="Go Home", command=open_new_page, fg_color="purple", hover_color="#8B008B")
    goHome.pack(pady=10)


def pulso_periodico():
    root.minsize(500, 300)
    for widget in root.winfo_children():
        widget.pack_forget()

    root.title("Pulso Periódico")
    pulse_label = ctk.CTkLabel(root, text="Pulso Periódico", wraplength=500)
    pulse_label.pack(pady=10)
    tempo1_entry = ctk.CTkEntry(root, placeholder_text="Tempo de Pulso (s)", justify='center')
    tempo1_entry.pack(pady=5)
    tempo2_entry = ctk.CTkEntry(root, placeholder_text="Tempo de Pausa (s)", justify='center')
    tempo2_entry.pack(pady=5)
    num_pulse_entry = ctk.CTkEntry(root, placeholder_text="Número de Pulsos", justify='center')
    num_pulse_entry.pack(pady=5)

    def led_pulse():
        if tempo1_entry.get().strip() != "" and tempo2_entry.get().strip() != "" and num_pulse_entry.get().strip() != "":
            led(porta=selected_port.get(), opc=2, tempo1=float(tempo1_entry.get()),
                tempo2=float(tempo2_entry.get()), num_pulse=int(num_pulse_entry.get()))
            open_new_page()
        else:
            port_error = ctk.CTkToplevel(root)
            port_error.title("Erro!")
            port_error.geometry("200x100")
            port_error.resizable(False, False)
            error_label = ctk.CTkLabel(port_error, text="Preencha os valores adequadamente!",
                                       wraplength=200)
            error_label.pack()

            error_button = ctk.CTkButton(port_error, text="OK", command=port_error.destroy,
                                         fg_color="red", hover_color="#8B008B")
            error_button.pack(pady=10)
            port_error.mainloop()

    start_bnt = ctk.CTkButton(root, text="Start Pulse", command=lambda port=None: led_pulse(), fg_color="purple",
                              hover_color="#8B008B")
    start_bnt.pack(pady=10)
    goHome = ctk.CTkButton(root, text="Go Home", command=open_new_page, fg_color="purple", hover_color="#8B008B")
    goHome.pack(pady=25)


portas = find_arduino()
root = ctk.CTk()
root.title("PyHolofotes")
root.geometry("300x120")
root.resizable(False, False)
ctk.set_appearance_mode("dark")
icon = get_base64_encoded_image("../img/icon.png")
root.iconphoto(True, PhotoImage(data=icon))


selected_port = StringVar()
selected_port.set("Selecione a porta")

dropdown = ctk.CTkOptionMenu(root, variable=selected_port, values=portas,
                             command=lambda port=None: arduino_conected(selected_port.get()),
                             fg_color="purple", button_color="#8B008B", button_hover_color="#9370DB")
dropdown.set(portas[0])
dropdown.pack(pady=5)


button = ctk.CTkButton(root, text="Continuar", command=open_new_page, fg_color="purple", hover_color="#8B008B")
button.pack(pady=25)

porta = selected_port.get()
root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))


root.mainloop()
