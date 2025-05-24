import sqlite3
import tkinter as tk
from tkinter import messagebox

def tela_veiculo():

    from telas.clientes import tela_cliente
    from telas.servicos import tela_servico
    from telas.pagamento import tela_pagamento

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

    def abrir_tela_cliente():
        janela.destroy()
        tela_cliente()
    
    def abrir_tela_servico():
        janela.destroy()
        tela_servico()
    
    def abrir_tela_pagamento():
        janela.destroy()
        tela_pagamento()

    # Interface
    janela = tk.Tk()
    janela.title("Gerenciador de Veículos")
    janela.geometry("600x750")
    janela.configure(bg="#f0f0f0")

    fonte_label = ("Segoe UI", 10, "bold")
    fonte_entry = ("Segoe UI", 10)

    frame_principal = tk.Frame(janela, bg="#ffffff", padx=20, pady=20, bd=2, relief="groove")
    frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

    def adicionar_campo(texto, widget, linha):
        tk.Label(frame_principal, text=texto, font=fonte_label, bg="#ffffff").grid(row=linha, column=0, sticky="w", pady=5)
        widget.grid(row=linha, column=1, sticky="ew", pady=5, padx=(10, 0))

    # Campos
    entry_id = tk.Entry(frame_principal, state='readonly', font=fonte_entry)
    cliente_var = tk.StringVar()
    cliente_menu = tk.OptionMenu(frame_principal, cliente_var, "Selecione um cliente")
    entry_marca = tk.Entry(frame_principal, font=fonte_entry)
    entry_modelo = tk.Entry(frame_principal, font=fonte_entry)
    entry_placa = tk.Entry(frame_principal, font=fonte_entry)
    entry_chassi = tk.Entry(frame_principal, font=fonte_entry)
    entry_ano = tk.Entry(frame_principal, font=fonte_entry)
    entry_cor = tk.Entry(frame_principal, font=fonte_entry)

    campos = [
        ("ID (automático):", entry_id),
        ("Cliente:", cliente_menu),
        ("Marca:", entry_marca),
        ("Modelo:", entry_modelo),
        ("Placa:", entry_placa),
        ("Chassi:", entry_chassi),
        ("Ano:", entry_ano),
        ("Cor:", entry_cor)
    ]

    for i, (texto, widget) in enumerate(campos):
        adicionar_campo(texto, widget, i)

    # Botões principais
    frame_botoes = tk.Frame(frame_principal, bg="#ffffff")
    frame_botoes.grid(row=8, column=0, columnspan=2, pady=10)

    botoes_acao = [
        ("Adicionar", adicionar_veiculo),
        ("Editar", editar_veiculo),
        ("Excluir", excluir_veiculo)
    ]

    for texto, comando in botoes_acao:
        tk.Button(frame_botoes, text=texto, width=12, font=fonte_label, bg="#4CAF50", fg="white", command=comando).pack(side="left", padx=5)

    # Lista de veículos
    tk.Label(frame_principal, text="Veículos:", font=fonte_label, bg="#ffffff").grid(row=9, column=0, sticky="w", pady=(20, 5))
    lista_veiculos = tk.Listbox(frame_principal, width=60, height=8, font=fonte_entry)
    lista_veiculos.grid(row=10, column=0, columnspan=2, sticky="ew")
    lista_veiculos.bind('<<ListboxSelect>>', selecionar_veiculo)

    # Navegação
    frame_navegacao = tk.Frame(frame_principal, bg="#ffffff")
    frame_navegacao.grid(row=11, column=0, columnspan=2, pady=20)

    botoes_nav = [
        ("Cliente", abrir_tela_cliente),
        ("Serviço", abrir_tela_servico),
        ("Pagamento", abrir_tela_pagamento)
    ]

    for texto, comando in botoes_nav:
        tk.Button(frame_navegacao, text=texto, width=12, font=fonte_label, bg="#9C27B0", fg="white", command=comando).pack(side="left", padx=10)

    frame_principal.columnconfigure(1, weight=1)

    listar_clientes_combo()
    listar_veiculos()
    janela.mainloop()
    conexao.close()