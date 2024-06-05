from users import *
from payments import *
from services import *
from clients import *
import tkinter as tk
from tkinter import PhotoImage

def main_window():
    root = tk.Tk()
    root.title("Norauto")
    root.geometry("600x400")
    root.configure(bg="#1f286d")

    menu_bar = tk.Menu(root, tearoff=0)

    menu_utilizadores = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Utilizadores", menu=menu_utilizadores)
    menu_utilizadores.add_command(label="Adicionar", command=add_user)
    menu_utilizadores.add_command(label="Remover", command=remove_user)
    menu_utilizadores.add_command(label="Mudar palavra-passe", command=change_password)
    menu_utilizadores.add_command(label="Atualizar fotografia", command=update_photo)

    menu_clientes = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Clientes", menu=menu_clientes)
    menu_clientes.add_command(label="Adicionar", command=add_client)
    menu_clientes.add_command(label="Remover", command=remove_client)
    menu_clientes.add_command(label="Lista de Clients", command=list_all_clients)

    menu_pagamentos = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Pagamentos", menu=menu_pagamentos)
    menu_pagamentos.add_command(label="Adicionar", command=add_payment)
    menu_pagamentos.add_command(label="Lista de Pagamentos", command=list_all_payments)

    menu_services = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Serviços", menu=menu_services)
    menu_services.add_command(label="Adicionar", command=create_service_page)
    menu_services.add_command(label="Atualizar", command=update_service_page)
    menu_services.add_command(label="Remover", command=delete_service_page)

    menu_bar.add_command(label="Sair", command=lambda: root.quit())

    root.config(menu=menu_bar)

    logo = PhotoImage(file="assets/logo.png", master=root)
    label_logo = tk.Label(root, image=logo, bg="#1f286d")
    label_logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()

# main_window()
