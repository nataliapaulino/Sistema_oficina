import sqlite3
import tkinter as tk
from tkinter import messagebox

def criar_bd():

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
  conexao.close()