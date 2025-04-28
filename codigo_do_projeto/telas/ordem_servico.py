import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from funcoes_bd.salvar_dados import salvar_dados

def ordem_servico():
    global janelaos
    janelaos = tk.Tk()
    janelaos.title("Ordem de Serviço")

    # Título principal
    titulo_label = ttk.Label(janelaos, text="Ordem de Serviço", font=("Arial", 16))
    titulo_label.grid(column=0, row=0, columnspan=3, padx=10, pady=(10, 20))

    # Espaçamento (aproximadamente 10 linhas)
    for i in range(1, 11):
        espaco_label = ttk.Label(janelaos, text="")
        espaco_label.grid(column=0, row=i, columnspan=3, pady=2)  # Ajuste o pady conforme necessário


    # Botão "Gerar"
    enviar_email_button = ttk.Button(janelaos, text="Gerar", command=gerar_ordem_servico)
    enviar_email_button.grid(column=1, row=11, padx=10, pady=10, sticky="ew")

    # Botão "Cancelar"
    cancelar_button = ttk.Button(janelaos, text="Cancelar", command=cancelar_ordem_servico)
    cancelar_button.grid(column=2, row=11, padx=10, pady=10, sticky="ew")

    # Configura o gerenciamento de layout para redimensionamento das colunas
    janelaos.columnconfigure(0, weight=1)
    janelaos.columnconfigure(1, weight=1)
    janelaos.columnconfigure(2, weight=1)

    janelaos.mainloop()

if __name__ == "__main__":
    ordem_servico()

def gerar_ordem_servico():
    salvar_dados()  # Chama a função para salvar os dados

    janelaos.destroy()  # Fecha a janela após gerar a ordem de serviço

def cancelar_ordem_servico():
    janelaos.destroy()  # Fecha a janela ao cancelar a ordem de serviço
    messagebox.showwarning("Ordem de Serviço", "Ordem de serviço cancelada!")

