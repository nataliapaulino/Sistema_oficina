import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def tela_cliente():

    from telas.veiculos import tela_veiculo
    from telas.servicos import tela_servico
    from telas.pagamento import tela_pagamento

    # Banco de dados
    conexao = sqlite3.connect('oficina.db')  # <- nome do banco de dados que será criado
    cursor = conexao.cursor()

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

    def abrir_tela_veiculo():
        janela.destroy()
        tela_veiculo()

    def abrir_tela_servico():
        janela.destroy()
        tela_servico()
    
    def abrir_tela_pagamento():
        janela.destroy()
        tela_pagamento()

    # Interface
    janela = tk.Tk()
    janela.title("Gerenciador de Clientes - Oficina")
    janela.geometry("600x750")
    janela.configure(bg="#f0f0f0")

    fonte_label = ("Segoe UI", 10, "bold")
    fonte_entry = ("Segoe UI", 10)

    frame_principal = tk.Frame(janela, bg="#ffffff", padx=20, pady=20, bd=2, relief="groove")
    frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

    # Campos
    def adicionar_campo(texto, entry_widget, linha):
        tk.Label(frame_principal, text=texto, font=fonte_label, bg="#ffffff").grid(row=linha, column=0, sticky="w", pady=5)
        entry_widget.grid(row=linha, column=1, sticky="ew", pady=5, padx=(10, 0))

    entry_id = tk.Entry(frame_principal, state='readonly', font=fonte_entry)
    entry_nome = tk.Entry(frame_principal, font=fonte_entry)
    entry_cpf = tk.Entry(frame_principal, font=fonte_entry)
    entry_email = tk.Entry(frame_principal, font=fonte_entry)
    entry_telefone = tk.Entry(frame_principal, font=fonte_entry)
    entry_endereco = tk.Entry(frame_principal, font=fonte_entry)

    campos = [
        ("ID (automático):", entry_id),
        ("Nome:", entry_nome),
        ("CPF:", entry_cpf),
        ("Email:", entry_email),
        ("Telefone:", entry_telefone),
        ("Endereço:", entry_endereco)
    ]

    for i, (texto, widget) in enumerate(campos):
        adicionar_campo(texto, widget, i)

    # Botões principais
    frame_botoes = tk.Frame(frame_principal, bg="#ffffff")
    frame_botoes.grid(row=6, column=0, columnspan=2, pady=10)

    botoes_acao = [
        ("Adicionar", adicionar_cliente),
        ("Editar", editar_cliente),
        ("Excluir", excluir_cliente)
    ]

    for texto, comando in botoes_acao:
        tk.Button(frame_botoes, text=texto, width=12, font=fonte_label, bg="#4CAF50", fg="white", command=comando).pack(side="left", padx=5)

    # Lista de clientes
    tk.Label(frame_principal, text="Clientes:", font=fonte_label, bg="#ffffff").grid(row=7, column=0, sticky="w", pady=(20, 5))
    lista_clientes = tk.Listbox(frame_principal, width=60, height=8, font=fonte_entry)
    lista_clientes.grid(row=8, column=0, columnspan=2, sticky="ew")
    lista_clientes.bind('<<ListboxSelect>>', selecionar_cliente)

    # Campo de busca
    tk.Label(frame_principal, text="Buscar por nome:", font=fonte_label, bg="#ffffff").grid(row=9, column=0, sticky="w", pady=(20, 5))
    entry_busca = tk.Entry(frame_principal, font=fonte_entry)
    entry_busca.grid(row=9, column=1, sticky="ew", pady=(20, 5))
    tk.Button(frame_principal, text="Buscar", width=10, font=fonte_label, bg="#2196F3", fg="white", command=buscar_cliente).grid(row=10, column=1, sticky="e", pady=5)

    # Navegação
    frame_navegacao = tk.Frame(frame_principal, bg="#ffffff")
    frame_navegacao.grid(row=11, column=0, columnspan=2, pady=20)

    botoes_nav = [
        ("Veículo", abrir_tela_veiculo),
        ("Serviço", abrir_tela_servico),
        ("Pagamento", abrir_tela_pagamento)
    ]

    for texto, comando in botoes_nav:
        tk.Button(frame_navegacao, text=texto, width=12, font=fonte_label, bg="#9C27B0", fg="white", command=comando).pack(side="left", padx=10)

    frame_principal.columnconfigure(1, weight=1)

    listar_clientes()
    janela.mainloop()
    conexao.close()

