import sqlite3
import tkinter as tk
from tkinter import messagebox

# Banco de dados
conexao = sqlite3.connect('oficina.db')  # <- nome do novo banco de dados
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









import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco
conexao = sqlite3.connect('oficina.db')
cursor = conexao.cursor()

# Funções
def listar_clientes_combo():
    cursor.execute("SELECT id, nome FROM clientes")
    clientes = cursor.fetchall()
    menu = [f"{c[0]} - {c[1]}" for c in clientes]
    cliente_menu['menu'].delete(0, 'end')
    for item in menu:
        cliente_menu['menu'].add_command(label=item, command=tk._setit(cliente_var, item))

def adicionar_veiculo():
    cliente = cliente_var.get()
    if not cliente:
        messagebox.showwarning("Erro", "Selecione um cliente.")
        return
    cliente_id = cliente.split(" - ")[0]
    dados = (cliente_id, entry_marca.get(), entry_modelo.get(), entry_placa.get(),
             entry_chassi.get(), entry_ano.get(), entry_cor.get())
    cursor.execute('''
        INSERT INTO veiculos (cliente_id, marca, modelo, placa, chassi, ano, cor)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', dados)
    conexao.commit()
    listar_veiculos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Veículo adicionado.")

def listar_veiculos():
    cursor.execute('''
        SELECT v.id, c.nome, v.marca, v.modelo, v.placa, v.ano, v.cor
        FROM veiculos v
        JOIN clientes c ON v.cliente_id = c.id
    ''')
    lista_veiculos.delete(0, tk.END)
    for v in cursor.fetchall():
        lista_veiculos.insert(tk.END, f"{v[0]} - {v[1]} - {v[2]} {v[3]} - {v[4]} - {v[5]} - {v[6]}")

def selecionar_veiculo(event):
    try:
        index = lista_veiculos.curselection()[0]
        dados = lista_veiculos.get(index).split(" - ")
        entry_id.config(state='normal')
        entry_id.delete(0, tk.END)
        entry_id.insert(0, dados[0])
        entry_id.config(state='readonly')
        entry_marca.delete(0, tk.END)
        entry_marca.insert(0, dados[2].split()[0])
        entry_modelo.delete(0, tk.END)
        entry_modelo.insert(0, dados[2].split()[1])
        entry_placa.delete(0, tk.END)
        entry_placa.insert(0, dados[3])
        entry_ano.delete(0, tk.END)
        entry_ano.insert(0, dados[4])
        entry_cor.delete(0, tk.END)
        entry_cor.insert(0, dados[5])
    except IndexError:
        pass

def editar_veiculo():
    veiculo_id = entry_id.get()
    if not veiculo_id:
        messagebox.showwarning("Erro", "Selecione um veículo para editar.")
        return
    dados = (
        entry_marca.get(),
        entry_modelo.get(),
        entry_placa.get(),
        entry_chassi.get(),
        entry_ano.get(),
        entry_cor.get(),
        veiculo_id
    )
    cursor.execute('''
        UPDATE veiculos
        SET marca=?, modelo=?, placa=?, chassi=?, ano=?, cor=?
        WHERE id=?
    ''', dados)
    conexao.commit()
    listar_veiculos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Veículo editado.")

def excluir_veiculo():
    veiculo_id = entry_id.get()
    if not veiculo_id:
        messagebox.showwarning("Erro", "Selecione um veículo para excluir.")
        return
    cursor.execute("DELETE FROM veiculos WHERE id=?", (veiculo_id,))
    conexao.commit()
    listar_veiculos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Veículo excluído.")

def limpar_campos():
    for e in [entry_id, entry_marca, entry_modelo, entry_placa, entry_chassi, entry_ano, entry_cor]:
        e.config(state='normal')
        e.delete(0, tk.END)
    entry_id.config(state='readonly')

# Interface
janela = tk.Tk()
janela.title("Gerenciador de Veículos")
janela.geometry("600x600")

tk.Label(janela, text="ID (automático):").pack()
entry_id = tk.Entry(janela, state='readonly'); entry_id.pack()

tk.Label(janela, text="Cliente:").pack()
cliente_var = tk.StringVar()
cliente_menu = tk.OptionMenu(janela, cliente_var, "")
cliente_menu.pack()

tk.Label(janela, text="Marca:").pack()
entry_marca = tk.Entry(janela); entry_marca.pack()

tk.Label(janela, text="Modelo:").pack()
entry_modelo = tk.Entry(janela); entry_modelo.pack()

tk.Label(janela, text="Placa:").pack()
entry_placa = tk.Entry(janela); entry_placa.pack()

tk.Label(janela, text="Chassi:").pack()
entry_chassi = tk.Entry(janela); entry_chassi.pack()

tk.Label(janela, text="Ano:").pack()
entry_ano = tk.Entry(janela); entry_ano.pack()

tk.Label(janela, text="Cor:").pack()
entry_cor = tk.Entry(janela); entry_cor.pack()

tk.Button(janela, text="Adicionar", command=adicionar_veiculo).pack(pady=5)
tk.Button(janela, text="Editar", command=editar_veiculo).pack(pady=5)
tk.Button(janela, text="Excluir", command=excluir_veiculo).pack(pady=5)

tk.Label(janela, text="Veículos:").pack()
lista_veiculos = tk.Listbox(janela, width=100)
lista_veiculos.pack()
lista_veiculos.bind('<<ListboxSelect>>', selecionar_veiculo)

listar_clientes_combo()
listar_veiculos()
janela.mainloop()
conexao.close()












import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco
conexao = sqlite3.connect('oficina.db')
cursor = conexao.cursor()

# Funções
def listar_veiculos_combo():
    cursor.execute("""
        SELECT veiculos.id, clientes.nome, veiculos.modelo, veiculos.placa 
        FROM veiculos 
        JOIN clientes ON veiculos.cliente_id = clientes.id
    """)
    veiculos = cursor.fetchall()
    menu = [f"{v[0]} - {v[1]} - {v[2]} - {v[3]}" for v in veiculos]
    veiculo_menu['menu'].delete(0, 'end')
    for item in menu:
        veiculo_menu['menu'].add_command(label=item, command=tk._setit(veiculo_var, item))

def adicionar_servico():
    veiculo = veiculo_var.get()
    if not veiculo:
        messagebox.showwarning("Erro", "Selecione um veículo.")
        return
    veiculo_id = veiculo.split(" - ")[0]
    dados = (veiculo_id, entry_servico.get(), entry_data.get(), entry_obs.get())
    cursor.execute('''
        INSERT INTO manutencoes (veiculo_id, servico, dataHora, observacoes)
        VALUES (?, ?, ?, ?)
    ''', dados)
    conexao.commit()
    listar_servicos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Serviço adicionado.")

def listar_servicos():
    cursor.execute('''
        SELECT m.id, c.nome, v.modelo, v.placa, m.servico, m.dataHora 
        FROM manutencoes m
        JOIN veiculos v ON m.veiculo_id = v.id
        JOIN clientes c ON v.cliente_id = c.id
    ''')
    lista_servicos.delete(0, tk.END)
    for s in cursor.fetchall():
        lista_servicos.insert(tk.END, f"{s[0]} - {s[1]} - {s[2]} - {s[3]} - {s[4]} - {s[5]}")

def selecionar_servico(event):
    try:
        index = lista_servicos.curselection()[0]
        dados = lista_servicos.get(index).split(" - ", 5)
        entry_id.config(state='normal')
        entry_id.delete(0, tk.END)
        entry_id.insert(0, dados[0])
        entry_id.config(state='readonly')
        entry_servico.delete(0, tk.END)
        entry_servico.insert(0, dados[4])
        entry_data.delete(0, tk.END)
        entry_data.insert(0, dados[5])
    except IndexError:
        pass

def editar_servico():
    servico_id = entry_id.get()
    if not servico_id:
        messagebox.showwarning("Erro", "Selecione um serviço para editar.")
        return
    dados = (entry_servico.get(), entry_data.get(), entry_obs.get(), servico_id)
    cursor.execute('''
        UPDATE manutencoes 
        SET servico=?, dataHora=?, observacoes=?
        WHERE id=?
    ''', dados)
    conexao.commit()
    listar_servicos()
    limpar_campos()
    messagebox.showinfo("Atualizado", "Serviço editado com sucesso.")

def excluir_servico():
    servico_id = entry_id.get()
    if not servico_id:
        messagebox.showwarning("Erro", "Selecione um serviço para excluir.")
        return
    cursor.execute("DELETE FROM manutencoes WHERE id=?", (servico_id,))
    conexao.commit()
    listar_servicos()
    limpar_campos()
    messagebox.showinfo("Removido", "Serviço excluído com sucesso.")

def limpar_campos():
    for e in [entry_id, entry_servico, entry_data, entry_obs]:
        e.config(state='normal')
        e.delete(0, tk.END)
    entry_id.config(state='readonly')

# Interface
janela = tk.Tk()
janela.title("Controle de Serviços")
janela.geometry("650x600")

tk.Label(janela, text="ID (automático):").pack()
entry_id = tk.Entry(janela, state='readonly'); entry_id.pack()

tk.Label(janela, text="Veículo:").pack()
veiculo_var = tk.StringVar()
veiculo_menu = tk.OptionMenu(janela, veiculo_var, "")
veiculo_menu.pack()

tk.Label(janela, text="Serviço realizado:").pack()
entry_servico = tk.Entry(janela); entry_servico.pack()

tk.Label(janela, text="Data e Hora:").pack()
entry_data = tk.Entry(janela); entry_data.pack()

tk.Label(janela, text="Observações:").pack()
entry_obs = tk.Entry(janela); entry_obs.pack()

tk.Button(janela, text="Adicionar", command=adicionar_servico).pack(pady=5)
tk.Button(janela, text="Editar", command=editar_servico).pack(pady=5)
tk.Button(janela, text="Excluir", command=excluir_servico).pack(pady=5)

tk.Label(janela, text="Serviços registrados:").pack()
lista_servicos = tk.Listbox(janela, width=100)
lista_servicos.pack()
lista_servicos.bind('<<ListboxSelect>>', selecionar_servico)

listar_veiculos_combo()
listar_servicos()
janela.mainloop()
conexao.close()















import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco
conexao = sqlite3.connect('oficina.db')
cursor = conexao.cursor()

# Funções
def listar_manutencoes_combo():
    cursor.execute('''
        SELECT m.id, c.nome, v.modelo, v.placa, m.servico, m.dataHora 
        FROM manutencoes m
        JOIN veiculos v ON m.veiculo_id = v.id
        JOIN clientes c ON v.cliente_id = c.id
    ''')
    manutencoes = cursor.fetchall()
    menu = [f"{m[0]} - {m[1]} - {m[2]} - {m[3]} - {m[4]} - {m[5]}" for m in manutencoes]
    manutencao_menu['menu'].delete(0, 'end')
    for item in menu:
        manutencao_menu['menu'].add_command(label=item, command=tk._setit(manutencao_var, item))

def adicionar_pagamento():
    if not manutencao_var.get():
        messagebox.showwarning("Erro", "Selecione uma manutenção.")
        return
    manutencao_id = manutencao_var.get().split(" - ")[0]
    try:
        valores = (
            manutencao_id,
            float(entry_dinheiro.get() or 0),
            float(entry_pix.get() or 0),
            float(entry_debito.get() or 0),
            float(entry_credito.get() or 0)
        )
    except ValueError:
        messagebox.showwarning("Erro", "Preencha os valores numéricos corretamente.")
        return

    cursor.execute('''
        INSERT INTO formas_pagamento (manutencao_id, dinheiro, pix, debito, credito)
        VALUES (?, ?, ?, ?, ?)
    ''', valores)
    conexao.commit()
    listar_pagamentos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Pagamento registrado.")

def listar_pagamentos():
    cursor.execute('''
        SELECT fp.id, c.nome, v.modelo, v.placa, m.servico, fp.dinheiro, fp.pix, fp.debito, fp.credito
        FROM formas_pagamento fp
        JOIN manutencoes m ON fp.manutencao_id = m.id
        JOIN veiculos v ON m.veiculo_id = v.id
        JOIN clientes c ON v.cliente_id = c.id
    ''')
    lista_pagamentos.delete(0, tk.END)
    for p in cursor.fetchall():
        total = p[5] + p[6] + p[7] + p[8]
        lista_pagamentos.insert(tk.END, f"{p[0]} - {p[1]} - {p[2]} - {p[3]} - {p[4]} | R$ {total:.2f}")

def selecionar_pagamento(event):
    try:
        index = lista_pagamentos.curselection()[0]
        dados = lista_pagamentos.get(index).split(" - ", 5)
        pagamento_id = dados[0]
        cursor.execute("SELECT * FROM formas_pagamento WHERE id=?", (pagamento_id,))
        p = cursor.fetchone()
        if p:
            entry_id.config(state='normal')
            entry_id.delete(0, tk.END)
            entry_id.insert(0, str(p[0]))
            entry_id.config(state='readonly')
            entry_dinheiro.delete(0, tk.END); entry_dinheiro.insert(0, str(p[2]))
            entry_pix.delete(0, tk.END); entry_pix.insert(0, str(p[3]))
            entry_debito.delete(0, tk.END); entry_debito.insert(0, str(p[4]))
            entry_credito.delete(0, tk.END); entry_credito.insert(0, str(p[5]))
    except IndexError:
        pass

def editar_pagamento():
    pagamento_id = entry_id.get()
    if not pagamento_id:
        messagebox.showwarning("Erro", "Selecione um pagamento para editar.")
        return
    try:
        valores = (
            float(entry_dinheiro.get() or 0),
            float(entry_pix.get() or 0),
            float(entry_debito.get() or 0),
            float(entry_credito.get() or 0),
            pagamento_id
        )
    except ValueError:
        messagebox.showwarning("Erro", "Preencha os valores numéricos corretamente.")
        return

    cursor.execute('''
        UPDATE formas_pagamento 
        SET dinheiro=?, pix=?, debito=?, credito=?
        WHERE id=?
    ''', valores)
    conexao.commit()
    listar_pagamentos()
    limpar_campos()
    messagebox.showinfo("Atualizado", "Pagamento editado com sucesso.")

def excluir_pagamento():
    pagamento_id = entry_id.get()
    if not pagamento_id:
        messagebox.showwarning("Erro", "Selecione um pagamento para excluir.")
        return
    cursor.execute("DELETE FROM formas_pagamento WHERE id=?", (pagamento_id,))
    conexao.commit()
    listar_pagamentos()
    limpar_campos()
    messagebox.showinfo("Removido", "Pagamento excluído com sucesso.")

def limpar_campos():
    for e in [entry_id, entry_dinheiro, entry_pix, entry_debito, entry_credito]:
        e.config(state='normal')
        e.delete(0, tk.END)
    entry_id.config(state='readonly')

# Interface
janela = tk.Tk()
janela.title("Pagamentos - Oficina")
janela.geometry("600x600")

tk.Label(janela, text="ID (automático):").pack()
entry_id = tk.Entry(janela, state='readonly'); entry_id.pack()

tk.Label(janela, text="Manutenção:").pack()
manutencao_var = tk.StringVar()
manutencao_menu = tk.OptionMenu(janela, manutencao_var, "")
manutencao_menu.pack()

tk.Label(janela, text="Dinheiro:").pack()
entry_dinheiro = tk.Entry(janela); entry_dinheiro.pack()

tk.Label(janela, text="Pix:").pack()
entry_pix = tk.Entry(janela); entry_pix.pack()

tk.Label(janela, text="Débito:").pack()
entry_debito = tk.Entry(janela); entry_debito.pack()

tk.Label(janela, text="Crédito:").pack()
entry_credito = tk.Entry(janela); entry_credito.pack()

tk.Button(janela, text="Adicionar", command=adicionar_pagamento).pack(pady=5)
tk.Button(janela, text="Editar", command=editar_pagamento).pack(pady=5)
tk.Button(janela, text="Excluir", command=excluir_pagamento).pack(pady=5)

tk.Label(janela, text="Pagamentos registrados:").pack()
lista_pagamentos = tk.Listbox(janela, width=100)
lista_pagamentos.pack()
lista_pagamentos.bind('<<ListboxSelect>>', selecionar_pagamento)

listar_manutencoes_combo()
listar_pagamentos()
janela.mainloop()
conexao.close()