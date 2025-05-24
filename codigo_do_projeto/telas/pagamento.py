import sqlite3
import tkinter as tk
from tkinter import messagebox

def tela_pagamento():

    from telas.clientes import tela_cliente
    from telas.veiculos import tela_veiculo
    from telas.servicos import tela_servico
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

    def abrir_tela_cliente():
        janela.destroy()
        tela_cliente()
    
    def abrir_tela_veiculo():
        janela.destroy()
        tela_veiculo()
    
    def abrir_tela_servico():
        janela.destroy()
        tela_servico()

    # Interface
    janela = tk.Tk()
    janela.title("Pagamentos - Oficina")
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
    manutencao_var = tk.StringVar()
    manutencao_menu = tk.OptionMenu(frame_principal, manutencao_var, "Selecione a manutenção")
    entry_dinheiro = tk.Entry(frame_principal, font=fonte_entry)
    entry_pix = tk.Entry(frame_principal, font=fonte_entry)
    entry_debito = tk.Entry(frame_principal, font=fonte_entry)
    entry_credito = tk.Entry(frame_principal, font=fonte_entry)

    campos = [
        ("ID (automático):", entry_id),
        ("Manutenção:", manutencao_menu),
        ("Dinheiro:", entry_dinheiro),
        ("Pix:", entry_pix),
        ("Débito:", entry_debito),
        ("Crédito:", entry_credito)
    ]

    for i, (texto, widget) in enumerate(campos):
        adicionar_campo(texto, widget, i)

    # Botões principais
    frame_botoes = tk.Frame(frame_principal, bg="#ffffff")
    frame_botoes.grid(row=6, column=0, columnspan=2, pady=10)

    botoes_acao = [
        ("Adicionar", adicionar_pagamento),
        ("Editar", editar_pagamento),
        ("Excluir", excluir_pagamento)
    ]

    for texto, comando in botoes_acao:
        tk.Button(frame_botoes, text=texto, width=12, font=fonte_label, bg="#4CAF50", fg="white", command=comando).pack(side="left", padx=5)

    # Lista de pagamentos
    tk.Label(frame_principal, text="Pagamentos registrados:", font=fonte_label, bg="#ffffff").grid(row=7, column=0, sticky="w", pady=(20, 5))
    lista_pagamentos = tk.Listbox(frame_principal, width=60, height=8, font=fonte_entry)
    lista_pagamentos.grid(row=8, column=0, columnspan=2, sticky="ew")
    lista_pagamentos.bind('<<ListboxSelect>>', selecionar_pagamento)

    # Navegação
    frame_navegacao = tk.Frame(frame_principal, bg="#ffffff")
    frame_navegacao.grid(row=9, column=0, columnspan=2, pady=20)

    botoes_nav = [
        ("Cliente", abrir_tela_cliente),
        ("Veículo", abrir_tela_veiculo),
        ("Serviço", abrir_tela_servico)
    ]

    for texto, comando in botoes_nav:
        tk.Button(frame_navegacao, text=texto, width=12, font=fonte_label, bg="#9C27B0", fg="white", command=comando).pack(side="left", padx=10)

    frame_principal.columnconfigure(1, weight=1)

    listar_manutencoes_combo()
    listar_pagamentos()
    janela.mainloop()
    conexao.close()