import sqlite3
import tkinter as tk
from tkinter import messagebox

# Banco de dados
conexao = sqlite3.connect('oficina.db')  # <- nome do banco de dados que será criado
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
)
''')

# Criar tabela de veículos
cursor.execute('''
CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    marca TEXT,
    modelo TEXT,
    placa TEXT,
    chassi TEXT,
    ano INTEGER,
    cor TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

# Criar tabela de manutenções
cursor.execute('''
CREATE TABLE IF NOT EXISTS manutencoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    veiculo_id INTEGER,
    servico TEXT,
    dataHora TEXT,
    observacoes TEXT,
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
)
''')

# Criar tabela de formas de pagamento
cursor.execute('''
CREATE TABLE IF NOT EXISTS formas_pagamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manutencao_id INTEGER,
    dinheiro REAL,
    pix REAL,
    debito REAL,
    credito REAL,
    FOREIGN KEY (manutencao_id) REFERENCES manutencoes(id)
)
''')

conexao.commit()

# Funções
def adicionar_cliente():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and cpf and email:
        cursor.execute("INSERT INTO clientes (nome, cpf, email, telefone, endereco) VALUES (?, ?, ?, ?, ?)", 
                       (nome, cpf, email, telefone, endereco))
        conexao.commit()
        limpar_campos()
        listar_clientes()
        messagebox.showinfo("Sucesso", "Cliente adicionado!")
    else:
        messagebox.showwarning("Erro", "Nome, CPF e Email são obrigatórios.")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    lista_clientes.delete(0, tk.END)
    for c in dados:
        lista_clientes.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]} - {c[3]} - {c[4]} - {c[5]}")

def buscar_cliente():
    nome = entry_busca.get()
    lista_clientes.delete(0, tk.END)
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", (f"%{nome}%",))
    for c in cursor.fetchall():
        lista_clientes.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]} - {c[3]} - {c[4]} - {c[5]}")

def selecionar_cliente(event):
    try:
        index = lista_clientes.curselection()[0]
        dados = lista_clientes.get(index).split(" - ", 5)
        if len(dados) == 6:
            id_c, nome, cpf, email, telefone, endereco = dados
            entry_id.config(state='normal')
            entry_id.delete(0, tk.END)
            entry_id.insert(0, id_c)
            entry_id.config(state='readonly')
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome)
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, cpf)
            entry_email.delete(0, tk.END)
            entry_email.insert(0, email)
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, telefone)
            entry_endereco.delete(0, tk.END)
            entry_endereco.insert(0, endereco)
    except IndexError:
        pass

def editar_cliente():
    id_c = entry_id.get()
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if id_c and nome and cpf and email:
        cursor.execute("UPDATE clientes SET nome=?, cpf=?, email=?, telefone=?, endereco=? WHERE id=?", 
                       (nome, cpf, email, telefone, endereco, id_c))
        conexao.commit()
        listar_clientes()
        limpar_campos()
        messagebox.showinfo("Atualizado", "Cliente editado com sucesso.")
    else:
        messagebox.showwarning("Erro", "Selecione um cliente e preencha os dados obrigatórios.")

def excluir_cliente():
    id_c = entry_id.get()
    if id_c:
        cursor.execute("DELETE FROM clientes WHERE id=?", (id_c,))
        conexao.commit()
        listar_clientes()
        limpar_campos()
        messagebox.showinfo("Removido", "Cliente excluído com sucesso.")
    else:
        messagebox.showwarning("Erro", "Selecione um cliente para excluir.")

def limpar_campos():
    for e in [entry_id, entry_nome, entry_cpf, entry_email, entry_telefone, entry_endereco, entry_busca]:
        e.config(state='normal')
        e.delete(0, tk.END)
    entry_id.config(state='readonly')

# Interface
janela = tk.Tk()
janela.title("Gerenciador de Clientes - Oficina")
janela.geometry("520x600")

tk.Label(janela, text="ID (automático):").pack()
entry_id = tk.Entry(janela, state='readonly'); entry_id.pack()

tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela); entry_nome.pack()

tk.Label(janela, text="CPF:").pack()
entry_cpf = tk.Entry(janela); entry_cpf.pack()

tk.Label(janela, text="Email:").pack()
entry_email = tk.Entry(janela); entry_email.pack()

tk.Label(janela, text="Telefone:").pack()
entry_telefone = tk.Entry(janela); entry_telefone.pack()

tk.Label(janela, text="Endereço:").pack()
entry_endereco = tk.Entry(janela); entry_endereco.pack()

tk.Button(janela, text="Adicionar", command=adicionar_cliente).pack(pady=5)
tk.Button(janela, text="Editar", command=editar_cliente).pack(pady=5)
tk.Button(janela, text="Excluir", command=excluir_cliente).pack(pady=5)

tk.Label(janela, text="Clientes:").pack()
lista_clientes = tk.Listbox(janela, width=80)
lista_clientes.pack()
lista_clientes.bind('<<ListboxSelect>>', selecionar_cliente)

tk.Label(janela, text="Buscar por nome:").pack()
entry_busca = tk.Entry(janela); entry_busca.pack()
tk.Button(janela, text="Buscar", command=buscar_cliente).pack(pady=5)

listar_clientes()
janela.mainloop()
conexao.close()