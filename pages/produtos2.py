import streamlit as st 
import products, structs
import sqlite3
import os 
import pandas as pd

#TODO:criar metodos de conexão com o banco com isso: 
db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
conn = sqlite3.connect(db_path)

def inserir_registro(produto, peso, sabor):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Produtos (Produto, Peso, Sabor) VALUES (?, ?, ?)', (produto, peso, sabor))
    conn.commit()
    conn.close()

st.title('Produtos Superchips')
st.subheader('Cadastrar novo produto')
input_produto = st.text_input('Nome do produto:')
input_peso = st.selectbox("Tamanho Pacote :", ["300 g", "500g", "700 g"])
input_sabor = st.selectbox("Sabor:", [ "Tradicional", "Churrasco", "Banana", "Amendoim", "Outros"])
if st.button('Cadastrar'):
    inserir_registro(input_produto, input_peso, input_sabor)
    st.success('Registro adicionado com sucesso.')





# Mostra os registros existentes na tabela

st.subheader('Produtos Cadatrados')
#TODO:criar metodos de mostrar produtos com isso : 
cursor = conn.cursor()

query = 'SELECT ID_Produto, Produto, Peso, Sabor FROM Produtos'
cursor.execute(query)
df = pd.read_sql_query(query, conn)
df = df.reset_index(drop=True)
registros = cursor.fetchall()
conn.close()

if registros:
    st.table(df)
else:
    st.warning('Não há registros na tabela.')

st.subheader('Atualizar Produtos')
st.subheader('Deletar Produtos')