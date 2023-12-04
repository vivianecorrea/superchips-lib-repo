import streamlit as st
import sqlite3
import os
import pandas as pd
from datetime import datetime, timedelta


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

st.title('Pedidos Superchips')

st.subheader('Novo Pedido')
produtos = obter_produtos()
id_produto_pedido = st.selectbox('Selecione o Produto:', produtos, format_func=lambda x: x[1])
quantidade_pedido = st.number_input('Quantidade:', min_value=1)
data_pedido = st.date_input('Data do Pedido:', datetime.now())
status_pedido = st.selectbox('Status do Pedido:', ['Em Andamento', 'Concluído'])
data_entrega_prevista = st.date_input('Data de Entrega Prevista:', datetime.now() + timedelta(days=2))
operador_responsavel = st.text_input('Operador Responsável:')

if st.button('Registrar Pedido'):
    inserir_pedido(
        id_produto_pedido[0],
        quantidade_pedido,
        data_pedido,
        status_pedido,
        data_entrega_prevista,
        operador_responsavel
    )
    st.success('Pedido registrado com sucesso.')

st.subheader('Pedidos Cadastrados')
df_pedidos = obter_pedidos()

if not df_pedidos.empty:
    st.table(df_pedidos)
else:
    st.warning('Não há pedidos cadastrados.')
