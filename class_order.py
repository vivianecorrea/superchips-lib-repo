import streamlit as st
import sqlite3
import os
import pandas as pd
from datetime import datetime, timedelta

class Order:
    def __init__(self, db_connection: DBConn):
        self.db_connection = db_connection

    db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
    conn = sqlite3.connect(db_path)

    def obter_produtos():
        cursor = conn.cursor()
        query = 'SELECT ID_Produto, Produto FROM Produtos'
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos

    def inserir_pedido(id_produto, quantidade, data_pedido, status, data_entrega_prevista, operador_responsavel):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Pedidos (ID_Produto, Quantidade, Data_Pedido, Status, Data_Entrega_Prevista, Operador_Responsavel)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id_produto, quantidade, data_pedido, status, data_entrega_prevista, operador_responsavel))
        conn.commit()

    def obter_pedidos():
        cursor = conn.cursor()
        query = 'SELECT * FROM Pedidos'
        cursor.execute(query)
        df = pd.read_sql_query(query, conn)
        df = df.reset_index(drop=True)
        return df