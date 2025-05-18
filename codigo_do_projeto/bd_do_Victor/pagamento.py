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