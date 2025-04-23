# Buscar Cliente

import tkinter as tk
from tkinter import ttk

def buscar_cliente():
    cpf = cpf_entry.get()
    print(f"Buscar cliente com CPF: {cpf}")
    # Aqui você colocaria a lógica para buscar o cliente no seu sistema

def novo_cliente():
    print("Abrir tela de Novo Cliente")
    # Aqui você colocaria a lógica para abrir a tela de novo cliente

# Cria a janela principal
janela = tk.Tk()
janela.title("Buscar Cliente")

# Título principal
titulo_label = ttk.Label(janela, text="Buscar Cliente", font=("Arial", 16))
titulo_label.grid(column=0, row=0, columnspan=2, padx=10, pady=(10, 20))

# Campo para o CPF
cpf_label = ttk.Label(janela, text="CPF:")
cpf_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

cpf_entry = ttk.Entry(janela, width=20)
cpf_entry.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

# Botão "Cliente"
buscar_button = ttk.Button(janela, text="Cliente", command=buscar_cliente)
buscar_button.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

# Botão "Novo Cliente"
novo_button = ttk.Button(janela, text="Novo Cliente", command=novo_cliente)
novo_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

# Configura o gerenciamento de layout para redimensionamento
janela.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()












# Dados do Cliente

import tkinter as tk
from tkinter import ttk

def salvar_dados():
    print("Dados do Cliente:")
    print(f"  Nome: {nome_entry.get()}")
    print(f"  CPF: {cpf_entry.get()}")
    print(f"  Telefone: {telefone_entry.get()}")
    print(f"  E-mail: {email_entry.get()}")
    print(f"  Endereço: {endereco_entry.get()}")
    print("\nDados do Veículo:")
    print(f"  Marca: {marca_entry.get()}")
    print(f"  Placa: {placa_entry.get()}")
    print(f"  Chassi: {chassi_entry.get()}")
    print(f"  Modelo: {modelo_entry.get()}")
    print(f"  Ano de Fabricação: {ano_fabricacao_entry.get()}")
    print(f"  Cor: {cor_entry.get()}")
    print(f"  Observações Adicionais: {observacoes_entry.get()}")
    print("\nServiço:")
    print(f"  Serviço Solicitado: {servico_entry.get()}")
    print(f"  Data e Hora do Atendimento: {data_hora_atendimento_entry.get()}")
    print(f"  Observações Adicionais: {observacoes_entry.get()}")
    print(f"  Forma de Pagamento: {forma_pagamento_combo.get()}")
    # Aqui você colocaria a lógica para salvar os dados

# Cria a janela principal
janela = tk.Tk()
janela.title("Dados do Cliente")

# Canvas para a barra de rolagem
canvas = tk.Canvas(janela)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Título principal na tela
titulo_label = ttk.Label(scrollable_frame, text="Dados do Cliente", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

# --- Frame para Dados do Cliente ---
cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

nome_label = ttk.Label(cliente_frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(cliente_frame, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

cpf_label = ttk.Label(cliente_frame, text="CPF:")
cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cpf_entry = ttk.Entry(cliente_frame, width=20)
cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

telefone_label = ttk.Label(cliente_frame, text="Telefone:")
telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
telefone_entry = ttk.Entry(cliente_frame, width=20)
telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(cliente_frame, text="E-mail:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = ttk.Entry(cliente_frame, width=30)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

endereco_label = ttk.Label(cliente_frame, text="Endereço:")
endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
endereco_entry = tk.Text(cliente_frame, height=3, width=30)
endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Dados do Veículo ---
veiculo_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Veículo")
veiculo_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

marca_label = ttk.Label(veiculo_frame, text="Marca:")
marca_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
marca_entry = ttk.Entry(veiculo_frame, width=20)
marca_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

placa_label = ttk.Label(veiculo_frame, text="Placa:")
placa_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
placa_entry = ttk.Entry(veiculo_frame, width=10)
placa_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

chassi_label = ttk.Label(veiculo_frame, text="Chassi:")
chassi_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
chassi_entry = ttk.Entry(veiculo_frame, width=30)
chassi_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

modelo_label = ttk.Label(veiculo_frame, text="Modelo:")
modelo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
modelo_entry = ttk.Entry(veiculo_frame, width=20)
modelo_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ano_fabricacao_label = ttk.Label(veiculo_frame, text="Ano de Fabricação:")
ano_fabricacao_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
ano_fabricacao_entry = ttk.Entry(veiculo_frame, width=10)
ano_fabricacao_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

cor_label = ttk.Label(veiculo_frame, text="Cor:")
cor_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
cor_entry = ttk.Entry(veiculo_frame, width=15)
cor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Serviço ---
servico_frame = ttk.LabelFrame(scrollable_frame, text="Serviço")
servico_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

servico_solicitado_label = ttk.Label(servico_frame, text="Serviço Solicitado:")
servico_solicitado_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
servico_entry = tk.Text(servico_frame, height=3, width=30)
servico_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

data_hora_atendimento_label = ttk.Label(servico_frame, text="Data e Hora do Atendimento:")
data_hora_atendimento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
data_hora_atendimento_entry = ttk.Entry(servico_frame, width=25)
data_hora_atendimento_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

observacoes_label = ttk.Label(servico_frame, text="Observações Adicionais:")
observacoes_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
observacoes_entry = tk.Text(servico_frame, height=3, width=30)
observacoes_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

forma_pagamento_label = ttk.Label(servico_frame, text="Forma de Pagamento:")
forma_pagamento_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"] # Adicione mais opções se necessário
forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

# --- Botões Adicionais ---
alterar_button = ttk.Button(scrollable_frame, text="Alterar")
alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

novo_veiculo_button = ttk.Button(scrollable_frame, text="Novo Veículo")
novo_veiculo_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

novo_servico_button = ttk.Button(scrollable_frame, text="Novo Serviço")
novo_servico_button.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

# Configura o gerenciamento de layout para redimensionamento da coluna principal
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1) # Permite que o canvas se expanda

scrollable_frame.columnconfigure(0, weight=1)
cliente_frame.columnconfigure(1, weight=1)
veiculo_frame.columnconfigure(1, weight=1)
servico_frame.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()













# Cadastrar Novo Cliente

import tkinter as tk
from tkinter import ttk

def salvar_dados():
    print("Cadastrar Novo Cliente:")
    print(f"  Nome: {nome_entry.get()}")
    print(f"  CPF: {cpf_entry.get()}")
    print(f"  Telefone: {telefone_entry.get()}")
    print(f"  E-mail: {email_entry.get()}")
    print(f"  Endereço: {endereco_entry.get()}")
    print("\nDados do Veículo:")
    print(f"  Marca: {marca_entry.get()}")
    print(f"  Placa: {placa_entry.get()}")
    print(f"  Chassi: {chassi_entry.get()}")
    print(f"  Modelo: {modelo_entry.get()}")
    print(f"  Ano de Fabricação: {ano_fabricacao_entry.get()}")
    print(f"  Cor: {cor_entry.get()}")
    print("\nServiço:")
    print(f"  Serviço Solicitado: {servico_entry.get()}")
    print(f"  Data e Hora do Atendimento: {data_hora_atendimento_entry.get()}")
    print(f"  Data da Entrega: {data_entrega_entry.get()}")
    print(f"  Observações Adicionais: {observacoes_entry.get()}")
    print(f"  Forma de Pagamento: {forma_pagamento_combo.get()}")
    # Aqui você colocaria a lógica para salvar os dados

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastrar Novo Cliente")

# Canvas para a barra de rolagem
canvas = tk.Canvas(janela)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Título principal na tela
titulo_label = ttk.Label(scrollable_frame, text="Cadastrar Novo Cliente", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

# --- Frame para Dados do Cliente ---
cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

nome_label = ttk.Label(cliente_frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(cliente_frame, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

cpf_label = ttk.Label(cliente_frame, text="CPF:")
cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cpf_entry = ttk.Entry(cliente_frame, width=20)
cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

telefone_label = ttk.Label(cliente_frame, text="Telefone:")
telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
telefone_entry = ttk.Entry(cliente_frame, width=20)
telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(cliente_frame, text="E-mail:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = ttk.Entry(cliente_frame, width=30)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

endereco_label = ttk.Label(cliente_frame, text="Endereço:")
endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
endereco_entry = tk.Text(cliente_frame, height=3, width=30)
endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Dados do Veículo ---
veiculo_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Veículo")
veiculo_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

marca_label = ttk.Label(veiculo_frame, text="Marca:")
marca_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
marca_entry = ttk.Entry(veiculo_frame, width=20)
marca_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

placa_label = ttk.Label(veiculo_frame, text="Placa:")
placa_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
placa_entry = ttk.Entry(veiculo_frame, width=10)
placa_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

chassi_label = ttk.Label(veiculo_frame, text="Chassi:")
chassi_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
chassi_entry = ttk.Entry(veiculo_frame, width=30)
chassi_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

modelo_label = ttk.Label(veiculo_frame, text="Modelo:")
modelo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
modelo_entry = ttk.Entry(veiculo_frame, width=20)
modelo_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ano_fabricacao_label = ttk.Label(veiculo_frame, text="Ano de Fabricação:")
ano_fabricacao_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
ano_fabricacao_entry = ttk.Entry(veiculo_frame, width=10)
ano_fabricacao_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

cor_label = ttk.Label(veiculo_frame, text="Cor:")
cor_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
cor_entry = ttk.Entry(veiculo_frame, width=15)
cor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Serviço ---
servico_frame = ttk.LabelFrame(scrollable_frame, text="Serviço")
servico_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

servico_solicitado_label = ttk.Label(servico_frame, text="Serviço Solicitado:")
servico_solicitado_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
servico_entry = tk.Text(servico_frame, height=3, width=30)
servico_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

data_hora_atendimento_label = ttk.Label(servico_frame, text="Data e Hora do Atendimento:")
data_hora_atendimento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
data_hora_atendimento_entry = ttk.Entry(servico_frame, width=25)
data_hora_atendimento_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

observacoes_label = ttk.Label(servico_frame, text="Observações Adicionais:")
observacoes_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
observacoes_entry = tk.Text(servico_frame, height=3, width=30)
observacoes_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

forma_pagamento_label = ttk.Label(servico_frame, text="Forma de Pagamento:")
forma_pagamento_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"] # Adicione mais opções se necessário
forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

# --- Botões Adicionais ---
alterar_button = ttk.Button(scrollable_frame, text="Gerar Ordem de Serviço")
alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")



# Configura o gerenciamento de layout para redimensionamento da coluna principal
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1) # Permite que o canvas se expanda

scrollable_frame.columnconfigure(0, weight=1)
cliente_frame.columnconfigure(1, weight=1)
veiculo_frame.columnconfigure(1, weight=1)
servico_frame.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()












# Adicionar Novo Veículo

import tkinter as tk
from tkinter import ttk

def salvar_dados():
    print("Adicionar Novo Veículo:")
    print(f"  Nome: {nome_entry.get()}")
    print(f"  CPF: {cpf_entry.get()}")
    print(f"  Telefone: {telefone_entry.get()}")
    print(f"  E-mail: {email_entry.get()}")
    print(f"  Endereço: {endereco_entry.get()}")
    print("\nDados do Veículo:")
    print(f"  Marca: {marca_entry.get()}")
    print(f"  Placa: {placa_entry.get()}")
    print(f"  Chassi: {chassi_entry.get()}")
    print(f"  Modelo: {modelo_entry.get()}")
    print(f"  Ano de Fabricação: {ano_fabricacao_entry.get()}")
    print(f"  Cor: {cor_entry.get()}")
    print("\nServiço:")
    print(f"  Serviço Solicitado: {servico_entry.get()}")
    print(f"  Data e Hora do Atendimento: {data_hora_atendimento_entry.get()}")
    print(f"  Observações Adicionais: {observacoes_entry.get()}")
    print(f"  Forma de Pagamento: {forma_pagamento_combo.get()}")
    # Aqui você colocaria a lógica para salvar os dados

# Cria a janela principal
janela = tk.Tk()
janela.title("Adicionar Novo Veículo")

# Canvas para a barra de rolagem
canvas = tk.Canvas(janela)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Título principal na tela
titulo_label = ttk.Label(scrollable_frame, text="Adicionar Novo Veículo", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

# --- Frame para Dados do Cliente ---
cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

nome_label = ttk.Label(cliente_frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(cliente_frame, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

cpf_label = ttk.Label(cliente_frame, text="CPF:")
cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cpf_entry = ttk.Entry(cliente_frame, width=20)
cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

telefone_label = ttk.Label(cliente_frame, text="Telefone:")
telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
telefone_entry = ttk.Entry(cliente_frame, width=20)
telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(cliente_frame, text="E-mail:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = ttk.Entry(cliente_frame, width=30)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

endereco_label = ttk.Label(cliente_frame, text="Endereço:")
endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
endereco_entry = tk.Text(cliente_frame, height=3, width=30)
endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Dados do Veículo ---
veiculo_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Veículo")
veiculo_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

marca_label = ttk.Label(veiculo_frame, text="Marca:")
marca_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
marca_entry = ttk.Entry(veiculo_frame, width=20)
marca_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

placa_label = ttk.Label(veiculo_frame, text="Placa:")
placa_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
placa_entry = ttk.Entry(veiculo_frame, width=10)
placa_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

chassi_label = ttk.Label(veiculo_frame, text="Chassi:")
chassi_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
chassi_entry = ttk.Entry(veiculo_frame, width=30)
chassi_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

modelo_label = ttk.Label(veiculo_frame, text="Modelo:")
modelo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
modelo_entry = ttk.Entry(veiculo_frame, width=20)
modelo_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ano_fabricacao_label = ttk.Label(veiculo_frame, text="Ano de Fabricação:")
ano_fabricacao_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
ano_fabricacao_entry = ttk.Entry(veiculo_frame, width=10)
ano_fabricacao_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

cor_label = ttk.Label(veiculo_frame, text="Cor:")
cor_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
cor_entry = ttk.Entry(veiculo_frame, width=15)
cor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Serviço ---
servico_frame = ttk.LabelFrame(scrollable_frame, text="Serviço")
servico_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

servico_solicitado_label = ttk.Label(servico_frame, text="Serviço Solicitado:")
servico_solicitado_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
servico_entry = tk.Text(servico_frame, height=3, width=30)
servico_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

data_hora_atendimento_label = ttk.Label(servico_frame, text="Data e Hora do Atendimento:")
data_hora_atendimento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
data_hora_atendimento_entry = ttk.Entry(servico_frame, width=25)
data_hora_atendimento_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

observacoes_label = ttk.Label(servico_frame, text="Observações Adicionais:")
observacoes_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
observacoes_entry = tk.Text(servico_frame, height=3, width=30)
observacoes_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

forma_pagamento_label = ttk.Label(servico_frame, text="Forma de Pagamento:")
forma_pagamento_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"] # Adicione mais opções se necessário
forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

# --- Botões Adicionais ---
alterar_button = ttk.Button(scrollable_frame, text="Gerar Ordem de Serviço")
alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

novo_veiculo_button = ttk.Button(scrollable_frame, text="Cancelar")
novo_veiculo_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")



# Configura o gerenciamento de layout para redimensionamento da coluna principal
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1) # Permite que o canvas se expanda

scrollable_frame.columnconfigure(0, weight=1)
cliente_frame.columnconfigure(1, weight=1)
veiculo_frame.columnconfigure(1, weight=1)
servico_frame.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()











# Adicionar Novo Serviço

import tkinter as tk
from tkinter import ttk

def salvar_dados():
    print("Adicionar Novo Serviço:")
    print(f"  Nome: {nome_entry.get()}")
    print(f"  CPF: {cpf_entry.get()}")
    print(f"  Telefone: {telefone_entry.get()}")
    print(f"  E-mail: {email_entry.get()}")
    print(f"  Endereço: {endereco_entry.get()}")
    print("\nDados do Veículo:")
    print(f"  Marca: {marca_entry.get()}")
    print(f"  Placa: {placa_entry.get()}")
    print(f"  Chassi: {chassi_entry.get()}")
    print(f"  Modelo: {modelo_entry.get()}")
    print(f"  Ano de Fabricação: {ano_fabricacao_entry.get()}")
    print(f"  Cor: {cor_entry.get()}")
    print("\nServiço:")
    print(f"  Serviço Solicitado: {servico_entry.get()}")
    print(f"  Data e Hora do Atendimento: {data_hora_atendimento_entry.get()}")
    print(f"  Observações Adicionais: {observacoes_entry.get()}")
    print(f"  Forma de Pagamento: {forma_pagamento_combo.get()}")
    # Aqui você colocaria a lógica para salvar os dados

# Cria a janela principal
janela = tk.Tk()
janela.title("Adicionar Novo Serviço")

# Canvas para a barra de rolagem
canvas = tk.Canvas(janela)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Título principal na tela
titulo_label = ttk.Label(scrollable_frame, text="Adicionar Novo Serviço", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

# --- Frame para Dados do Cliente ---
cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

nome_label = ttk.Label(cliente_frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(cliente_frame, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

cpf_label = ttk.Label(cliente_frame, text="CPF:")
cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cpf_entry = ttk.Entry(cliente_frame, width=20)
cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

telefone_label = ttk.Label(cliente_frame, text="Telefone:")
telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
telefone_entry = ttk.Entry(cliente_frame, width=20)
telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(cliente_frame, text="E-mail:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = ttk.Entry(cliente_frame, width=30)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

endereco_label = ttk.Label(cliente_frame, text="Endereço:")
endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
endereco_entry = tk.Text(cliente_frame, height=3, width=30)
endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Dados do Veículo ---
veiculo_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Veículo")
veiculo_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

marca_label = ttk.Label(veiculo_frame, text="Marca:")
marca_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
marca_entry = ttk.Entry(veiculo_frame, width=20)
marca_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

placa_label = ttk.Label(veiculo_frame, text="Placa:")
placa_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
placa_entry = ttk.Entry(veiculo_frame, width=10)
placa_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

chassi_label = ttk.Label(veiculo_frame, text="Chassi:")
chassi_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
chassi_entry = ttk.Entry(veiculo_frame, width=30)
chassi_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

modelo_label = ttk.Label(veiculo_frame, text="Modelo:")
modelo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
modelo_entry = ttk.Entry(veiculo_frame, width=20)
modelo_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ano_fabricacao_label = ttk.Label(veiculo_frame, text="Ano de Fabricação:")
ano_fabricacao_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
ano_fabricacao_entry = ttk.Entry(veiculo_frame, width=10)
ano_fabricacao_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

cor_label = ttk.Label(veiculo_frame, text="Cor:")
cor_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
cor_entry = ttk.Entry(veiculo_frame, width=15)
cor_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# --- Frame para Serviço ---
servico_frame = ttk.LabelFrame(scrollable_frame, text="Serviço")
servico_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

servico_solicitado_label = ttk.Label(servico_frame, text="Serviço Solicitado:")
servico_solicitado_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
servico_entry = tk.Text(servico_frame, height=3, width=30)
servico_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

data_hora_atendimento_label = ttk.Label(servico_frame, text="Data e Hora do Atendimento:")
data_hora_atendimento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
data_hora_atendimento_entry = ttk.Entry(servico_frame, width=25)
data_hora_atendimento_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

observacoes_label = ttk.Label(servico_frame, text="Observações Adicionais:")
observacoes_label.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
observacoes_entry = tk.Text(servico_frame, height=3, width=30)
observacoes_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

forma_pagamento_label = ttk.Label(servico_frame, text="Forma de Pagamento:")
forma_pagamento_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"] # Adicione mais opções se necessário
forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

# --- Botões Adicionais ---
alterar_button = ttk.Button(scrollable_frame, text="Gerar Ordem de Serviço")
alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

novo_veiculo_button = ttk.Button(scrollable_frame, text="Cancelar")
novo_veiculo_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")



# Configura o gerenciamento de layout para redimensionamento da coluna principal
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1) # Permite que o canvas se expanda

scrollable_frame.columnconfigure(0, weight=1)
cliente_frame.columnconfigure(1, weight=1)
veiculo_frame.columnconfigure(1, weight=1)
servico_frame.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()













# Ordem de Serviço

import tkinter as tk
from tkinter import ttk

def imprimir_os():
    print("Funcionalidade para imprimir a Ordem de Serviço será implementada aqui.")

def enviar_email_os():
    print("Funcionalidade para enviar a Ordem de Serviço por e-mail será implementada aqui.")

def cancelar_os():
    print("Funcionalidade para cancelar a Ordem de Serviço será implementada aqui.")

def ordem_de_servico_janela():
    janela = tk.Tk()
    janela.title("Ordem de Serviço")

    # Título principal
    titulo_label = ttk.Label(janela, text="Ordem de Serviço", font=("Arial", 16))
    titulo_label.grid(column=0, row=0, columnspan=3, padx=10, pady=(10, 20))

    # Espaçamento (aproximadamente 10 linhas)
    for i in range(1, 11):
        espaco_label = ttk.Label(janela, text="")
        espaco_label.grid(column=0, row=i, columnspan=3, pady=2)  # Ajuste o pady conforme necessário

    # Botão "Imprimir O.S."
    imprimir_button = ttk.Button(janela, text="Imprimir O.S.", command=imprimir_os)
    imprimir_button.grid(column=0, row=11, padx=10, pady=10, sticky="ew")

    # Botão "Enviar por e-mail O.S."
    enviar_email_button = ttk.Button(janela, text="Enviar por e-mail O.S.", command=enviar_email_os)
    enviar_email_button.grid(column=1, row=11, padx=10, pady=10, sticky="ew")

    # Botão "Cancelar O.S."
    cancelar_button = ttk.Button(janela, text="Cancelar O.S.", command=cancelar_os)
    cancelar_button.grid(column=2, row=11, padx=10, pady=10, sticky="ew")

    # Configura o gerenciamento de layout para redimensionamento das colunas
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)
    janela.columnconfigure(2, weight=1)

    janela.mainloop()

if __name__ == "__main__":
    ordem_de_servico_janela()

