import streamlit as st
import sqlite3
import os
import pandas as pd
from datetime import datetime, timedelta

class Order:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
        self.conn = sqlite3.connect(self.db_path)

    def obter_produtos(self):
        cursor = self.conn.cursor()
        query = 'SELECT ID_Produto, Produto FROM Produtos'
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos

    def inserir_pedido(self, id_produto, quantidade, data_pedido, status, data_entrega_prevista, operador_responsavel):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Pedidos (ID_Produto, Quantidade, Data_Pedido, Status, Data_Entrega_Prevista, Operador_Responsavel)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id_produto, quantidade, data_pedido, status, data_entrega_prevista, operador_responsavel))
        self.conn.commit()

    def obter_pedidos(self):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM Pedidos'
        cursor.execute(query)
        df = pd.read_sql_query(query, self.conn)
        df = df.reset_index(drop=True)
        return df
