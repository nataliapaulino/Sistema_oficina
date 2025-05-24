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
    janela.geometry("600x780")

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

    tk.Button(janela, text="Cliente", command=abrir_tela_cliente).pack(pady=5)
    tk.Button(janela, text="Veículo", command=abrir_tela_veiculo).pack(pady=5)
    tk.Button(janela, text="Pagamento", command=abrir_tela_pagamento).pack(pady=5)

    listar_veiculos_combo()
    listar_servicos()
    janela.mainloop()
    conexao.close()