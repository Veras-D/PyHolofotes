import serial
from utilities import *
from tkinter import *
import customtkinter as ctk
from led_pulse import led


def Arduino(porta):
    if porta != "Selecione a porta":
        Arduino = serial.Serial(porta, 115200, timeout=1)
        return Arduino
    else:
        return None


def changeTheme():
    global color_bg
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
        color_bg = "#DBDBDB"
        open_new_page()
    else:
        ctk.set_appearance_mode("Dark")
        color_bg = "#2B2B2B"
        open_new_page()


def open_new_page():
    if selected_port.get() != ports[0]:
        root.geometry(f"500x500+{CENTER}+{CENTER}")
        frame(root)
        root.title("Seleção de pulso")
        root.resizable(False, False)

        for widget in root.winfo_children():
            widget.pack_forget()

        root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))

        tabview = ctk.CTkTabview(root, width=400, height=450, corner_radius=20, segmented_button_selected_color="purple",
                                 segmented_button_selected_hover_color="#8B008B", bg_color=color_bg)
        tabview.pack()
        tabview.add("SetUp")
        tabview.add("Configures")
        tabview.add("About")
        setup_tab = tabview.tab("SetUp")
        configures_tab = tabview.tab("Configures")
        about_tab = tabview.tab("About")

        pulso_unico_bnt = ctk.CTkButton(setup_tab, text="PULSO ÚNICO", command=pulso_unico,
                                        fg_color="purple", hover_color="#8B008B")
        pulso_periodico_bnt = ctk.CTkButton(setup_tab, text="PULSO PERIÓDICO", command=pulso_periodico,
                                            fg_color="purple", hover_color="#8B008B")
        pulso_unico_bnt.pack(pady=20)
        pulso_periodico_bnt.pack()

        change_theme_bnt = ctk.CTkButton(configures_tab, text="Theme", command=changeTheme,
                                         corner_radius=20, width=15)
        change_theme_bnt.place(x=290, y=0)
        main_label1 = ctk.CTkLabel(configures_tab,
                                   text=f"Porta: {selected_port.get()}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label1.place(x=0, y=20)  # {Arduino(selected_port.get())}

        main_label2 = ctk.CTkLabel(configures_tab,
                                   text=f"Arduino: ",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label2.place(x=0, y=45)

        arduino_get = Arduino(selected_port.get())
        main_label3 = ctk.CTkLabel(configures_tab,
                                   text=f"Taxa de Transmissão: {arduino_get.baudrate}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label3.place(x=10, y=70)

        main_label4 = ctk.CTkLabel(configures_tab,
                                   text=f"Tempo de Espera Maximo: {arduino_get.timeout}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label4.place(x=10, y=95)

        main_label5 = ctk.CTkLabel(configures_tab,
                                   text=f"Bytesize: {arduino_get.bytesize}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label5.place(x=10, y=120)

        main_label6 = ctk.CTkLabel(configures_tab,
                                   text=f"Controle de Fluxo XON/XOFF: {arduino_get.xonxoff}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label6.place(x=10, y=145)

        main_label7 = ctk.CTkLabel(configures_tab,
                                   text=f"Controle de Fluxo RTS/CTS: {arduino_get.rts}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label7.place(x=10, y=170)

        main_label8 = ctk.CTkLabel(configures_tab,
                                   text=f"Controle de Fluxo DSR/DTR: {arduino_get.dsr}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label8.place(x=10, y=195)

        main_label9 = ctk.CTkLabel(configures_tab,
                                   text=f"ID: {hex(id(arduino_get))}",
                                   wraplength=400, bg_color=color_bg, compound="left")
        main_label9.place(x=10, y=220)

        about_label = ctk.CTkLabel(about_tab,
                                   text="PyHolofotes é um programa Python para controlar um sistema Arduino RELE, "
                                        "injetando pulsos em superfícies para análises térmicas de defeitos não "
                                        "aparentes com uma câmera termográfica. Ele foi implementado no Laboratório de "
                                        "Transferência de Calor da UEMA, proporcionando uma plataforma eficiente e "
                                        "precisa para coleta de dados térmicos.",
                                   wraplength=400)
        about_label.pack()
        instagram_link = ctk.CTkLabel(root, text="Instagram", text_color="magenta", cursor="hand2",
                                      fg_color=color_bg)
        github_link = ctk.CTkLabel(root, text="GitHub", text_color="magenta", cursor="hand2", fg_color=color_bg)

        instagram_link.bind("<Button-1>", lambda e: callback("https://www.instagram.com/veras_programmer"))
        github_link.bind("<Button-1>", lambda e: callback("https://www.github.com/Veras-D"))

        instagram_link.place(x=20, y=root.winfo_height()-70)
        github_link.place(x=20, y=root.winfo_height()-45)
        # github_link.pack(side=ctk.BOTTOM)
        # instagram_link.pack(side=ctk.BOTTOM)

    else:
        port_error = ctk.CTkToplevel(root)
        port_error.title("Erro!")
        port_error.geometry("230x100")
        port_error.resizable(False, False)
        frame(port_error)
        error_label = ctk.CTkLabel(port_error, text="Você deve selecionar uma porta para iniciar o programa!",
                                   wraplength=200, fg_color=color_bg)
        error_label.pack()
        error_button = ctk.CTkButton(port_error, text="OK", command=port_error.destroy,
                                     fg_color="red", hover_color="#821D1A")
        error_button.pack(pady=10)
        port_error.mainloop()


def pulso_unico():
    for widget in root.winfo_children():
        widget.pack_forget()

    root.title("Pulso Único")
    frame(root)
    pulse_label = ctk.CTkLabel(root, text="Pulso Único", wraplength=500, fg_color=color_bg)
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
            port_error.geometry("230x100")
            port_error.resizable(False, False)
            frame(port_error)
            error_label = ctk.CTkLabel(port_error, text="Preencha os valores adequadamente!",
                                       wraplength=200, fg_color=color_bg)
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
    frame(root)
    pulse_label = ctk.CTkLabel(root, text="Pulso Periódico", wraplength=500, fg_color=color_bg)
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
            port_error.geometry("230x100")
            port_error.resizable(False, False)
            frame(port_error)
            error_label = ctk.CTkLabel(port_error, text="Preencha os valores adequadamente!",
                                       wraplength=200, fg_color=color_bg)
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


color_bg = "#2B2B2B"
ports = find_arduino()
root = ctk.CTk()
root.title("PyHolofotes")
root.update()
root.geometry(f"300x120+{CENTER}+{CENTER}")
root.resizable(False, False)
ctk.set_appearance_mode("dark")
# icon = get_base64_encoded_image("../img/icon.png")
# root.iconphoto(True, PhotoImage(data=icon))
frame(root)


selected_port = StringVar()
selected_port.set("Selecione a porta")

dropdown = ctk.CTkOptionMenu(root, variable=selected_port, values=ports,
                             command=lambda port=None: arduino_conected(selected_port.get()),
                             fg_color="purple", button_color="#8B008B", button_hover_color="#9370DB")
dropdown.set(ports[0])
dropdown.pack(pady=5)


button = ctk.CTkButton(root, text="Continuar", command=open_new_page, fg_color="purple", hover_color="#8B008B")
button.pack(pady=25)

porta = selected_port.get()
root.bind("<Destroy>", lambda event: on_closing(event, Arduino(selected_port.get())))


root.mainloop()
