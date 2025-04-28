import tkinter as tk
from tkinter import ttk

from telas.ordem_servico import ordem_servico

def novo_veiculo(Dados):
  global janelanovoveiculo
  janelanovoveiculo = tk.Tk()
  janelanovoveiculo.title("Novo Veículo")

  # Canvas para a barra de rolagem
  canvas = tk.Canvas(janelanovoveiculo)
  scrollbar = ttk.Scrollbar(janelanovoveiculo, orient="vertical", command=canvas.yview)
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
  titulo_label = ttk.Label(scrollable_frame, text="Novo Veículo", font=("Arial", 16))
  titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20))

  # --- Frame para Dados do Cliente ---
  cliente_frame = ttk.LabelFrame(scrollable_frame, text="Dados do Cliente")
  cliente_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

  nome_label = ttk.Label(cliente_frame, text="Nome: " + Dados["Nome"])
  nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
#   nome_entry = ttk.Entry(cliente_frame, width=30)
#   nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

  cpf_label = ttk.Label(cliente_frame, text="CPF: " + Dados["CPF"])
  cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
#   cpf_entry = ttk.Entry(cliente_frame, width=20)
#   cpf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

  telefone_label = ttk.Label(cliente_frame, text="Telefone: " + Dados["Telefone"])
  telefone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
#   telefone_entry = ttk.Entry(cliente_frame, width=20)
#   telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

  email_label = ttk.Label(cliente_frame, text="E-mail: " + Dados["Email"])
  email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
#   email_entry = ttk.Entry(cliente_frame, width=30)
#   email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

  endereco_label = ttk.Label(cliente_frame, text="Endereço: " + Dados["Endereco"])
  endereco_label.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
#   endereco_entry = tk.Text(cliente_frame, height=3, width=30)
#   endereco_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

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
  forma_pagamento_opcoes = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"]
  # Adicione mais opções se necessário
  forma_pagamento_combo = ttk.Combobox(servico_frame, values=forma_pagamento_opcoes, width=20)
  forma_pagamento_combo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
  forma_pagamento_combo.set(forma_pagamento_opcoes[0]) # Define um valor padrão

  alterar_button = ttk.Button(scrollable_frame, text="Gerar Ordem de Serviço", command=botao_gerar_os)
  alterar_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

  novo_veiculo_button = ttk.Button(scrollable_frame, text="Cancelar", command=janelanovoveiculo.destroy)
  novo_veiculo_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

def botao_gerar_os():
    janelanovoveiculo.destroy()  # Fecha a janela após gerar a ordem de serviço
    ordem_servico()