# Buscar Cliente

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from buscar_se_cliente_existe import buscar_se_cliente_existe
from abrir_tela_dados_do_cliente import abrir_tela_dados_do_cliente

from abrir_tela_cadastrar_novo_cliente import abrir_tela_cadastrar_novo_cliente



def buscar_cliente():
    cpf = cpf_entry.get()
    respostabd = buscar_se_cliente_existe(cpf)
    if respostabd:
        abrir_tela_dados_do_cliente(cpf)
    else:
        messagebox.showwarning("Aviso", "Cliente não encontrado!")

# Cria a janela principal
janelaprincipal = tk.Tk()
janelaprincipal.title("Buscar Cliente")

# Título principal
titulo_label = ttk.Label(janelaprincipal, text="Buscar Cliente", font=("Arial", 16))
titulo_label.grid(column=0, row=0, columnspan=2, padx=10, pady=(10, 20))

# Campo para o CPF
cpf_label = ttk.Label(janelaprincipal, text="CPF:")
cpf_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

cpf_entry = ttk.Entry(janelaprincipal, width=20)
cpf_entry.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

# Botão "Cliente"
buscar_button = ttk.Button(janelaprincipal, text="Cliente", command=buscar_cliente)
buscar_button.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

# Botão "Novo Cliente"
novo_button = ttk.Button(janelaprincipal, text="Novo Cliente", command=abrir_tela_cadastrar_novo_cliente)
novo_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

# Configura o gerenciamento de layout para redimensionamento
janelaprincipal.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janelaprincipal.mainloop()