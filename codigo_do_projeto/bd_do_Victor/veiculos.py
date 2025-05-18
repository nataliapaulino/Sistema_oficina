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