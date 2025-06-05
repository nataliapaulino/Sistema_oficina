import sqlite3
import tkinter as tk
from tkinter import messagebox

def tela_servico():

    from telas.clientes import tela_cliente
    from telas.veiculos import tela_veiculo
    from telas.pagamento import tela_pagamento

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
            SELECT m.id, c.nome, v.modelo, v.placa, m.servico, m.dataHora, m.observacoes
            FROM manutencoes m
            JOIN veiculos v ON m.veiculo_id = v.id
            JOIN clientes c ON v.cliente_id = c.id
        ''')
        lista_servicos.delete(0, tk.END)
        for s in cursor.fetchall():
            lista_servicos.insert(tk.END, f"{s[0]} - {s[1]} - {s[2]} - {s[3]} - {s[4]} - {s[5]} - {s[6]}")

    def selecionar_servico(event):
        try:
            index = lista_servicos.curselection()[0]
            dados = lista_servicos.get(index).split(" - ", 6)
            entry_id.config(state='normal')
            entry_id.delete(0, tk.END)
            entry_id.insert(0, dados[0])
            entry_id.config(state='readonly')
            entry_servico.delete(0, tk.END)
            entry_servico.insert(0, dados[4])
            entry_data.delete(0, tk.END)
            entry_data.insert(0, dados[5])
            entry_obs.delete(0, tk.END)
            entry_obs.insert(0, dados[6])
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

    def abrir_tela_cliente():
        janela.destroy()
        tela_cliente()
    
    def abrir_tela_veiculo():
        janela.destroy()
        tela_veiculo()
    
    def abrir_tela_pagamento():
        janela.destroy()
        tela_pagamento()

    # Interface
    janela = tk.Tk()
    janela.title("Controle de Serviços")
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
    veiculo_var = tk.StringVar()
    veiculo_menu = tk.OptionMenu(frame_principal, veiculo_var, "Selecione um veículo")
    entry_servico = tk.Entry(frame_principal, font=fonte_entry)
    entry_data = tk.Entry(frame_principal, font=fonte_entry)
    entry_obs = tk.Entry(frame_principal, font=fonte_entry)

    campos = [
        ("ID (automático):", entry_id),
        ("Veículo:", veiculo_menu),
        ("Serviço realizado:", entry_servico),
        ("Data e Hora:", entry_data),
        ("Observações:", entry_obs)
    ]

    for i, (texto, widget) in enumerate(campos):
        adicionar_campo(texto, widget, i)

    # Botões principais
    frame_botoes = tk.Frame(frame_principal, bg="#ffffff")
    frame_botoes.grid(row=5, column=0, columnspan=2, pady=10)

    botoes_acao = [
        ("Adicionar", adicionar_servico),
        ("Editar", editar_servico),
        ("Excluir", excluir_servico)
    ]

    for texto, comando in botoes_acao:
        tk.Button(frame_botoes, text=texto, width=12, font=fonte_label, bg="#4CAF50", fg="white", command=comando).pack(side="left", padx=5)

    # Lista de serviços
    tk.Label(frame_principal, text="Serviços registrados:", font=fonte_label, bg="#ffffff").grid(row=6, column=0, sticky="w", pady=(20, 5))
    lista_servicos = tk.Listbox(frame_principal, width=60, height=8, font=fonte_entry)
    lista_servicos.grid(row=7, column=0, columnspan=2, sticky="ew")
    lista_servicos.bind('<<ListboxSelect>>', selecionar_servico)

    # Navegação
    frame_navegacao = tk.Frame(frame_principal, bg="#ffffff")
    frame_navegacao.grid(row=8, column=0, columnspan=2, pady=20)

    botoes_nav = [
        ("Cliente", abrir_tela_cliente),
        ("Veículo", abrir_tela_veiculo),
        ("Pagamento", abrir_tela_pagamento)
    ]

    for texto, comando in botoes_nav:
        tk.Button(frame_navegacao, text=texto, width=12, font=fonte_label, bg="#9C27B0", fg="white", command=comando).pack(side="left", padx=10)

    frame_principal.columnconfigure(1, weight=1)

    listar_veiculos_combo()
    listar_servicos()
    janela.mainloop()
    conexao.close()