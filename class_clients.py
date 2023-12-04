import streamlit as st
import sqlite3
import pandas as pd
import os

def conectar_banco():
    db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
    conn = sqlite3.connect(db_path)
    return conn

def obter_clientes():
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'SELECT * FROM Clientes'
    cursor.execute(query)
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def atualizar_cliente(id_cliente, nome, email, telefone, cidade):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'UPDATE Clientes SET Nome=?, Email=?, Telefone=?, Cidade=? WHERE Id_Cliente=?'
    cursor.execute(query, (nome, email, telefone, cidade, id_cliente))
    conn.commit()
    conn.close()

def deletar_cliente(id_cliente):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'DELETE FROM Clientes WHERE Id_Cliente=?'
    cursor.execute(query, (id_cliente,))
    conn.commit()
    conn.close()
