import streamlit as st
import sqlite3
import os
import pandas as pd

# TODO: Criar métodos de conexão com o banco com isso:
db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
conn = sqlite3.connect(db_path)

def inserir_registro(produto, peso, sabor):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Produtos (Produto, Peso, Sabor) VALUES (?, ?, ?)', (produto, peso, sabor))
    conn.commit()

def obter_registros():
    cursor = conn.cursor()
    query = 'SELECT ID_Produto, Produto, Peso, Sabor FROM Produtos'
    cursor.execute(query)
    df = pd.read_sql_query(query, conn)
    df = df.reset_index(drop=True)
    conn.commit()
    return df

def atualizar_registro(id_produto, novo_produto, novo_peso, novo_sabor):
    cursor = conn.cursor()
    query = 'UPDATE Produtos SET Produto=?, Peso=?, Sabor=? WHERE ID_Produto=?'
    cursor.execute(query, (novo_produto, novo_peso, novo_sabor, id_produto))
    conn.commit()

def deletar_registro(id_produto):
    cursor = conn.cursor()
    query = 'DELETE FROM Produtos WHERE ID_Produto=?'
    cursor.execute(query, (id_produto,))
    conn.commit()

st.title('Produtos Superchips')
st.subheader('Cadastrar novo produto')
input_produto = st.text_input('Nome do produto:')
input_peso = st.selectbox("Tamanho Pacote:", ["300 g", "500g", "700 g"])
input_sabor = st.selectbox("Sabor:", ["Tradicional", "Churrasco", "Banana", "Amendoim", "Outros"])
if st.button('Cadastrar'):
    inserir_registro(input_produto, input_peso, input_sabor)
    st.success('Registro adicionado com sucesso.')

# Mostra os registros existentes na tabela
st.subheader('Produtos Cadastrados')
df = obter_registros()

if not df.empty:
    st.table(df)
else:
    st.warning('Não há registros na tabela.')

# Atualizar Produtos
st.subheader('Atualizar Produtos')
id_para_atualizar = st.text_input('ID do produto a ser atualizado:')
novo_produto = st.text_input('Novo nome do produto:')
novo_peso = st.selectbox('Novo tamanho do pacote:', ["300 g", "500g", "700 g"])
novo_sabor = st.selectbox('Novo sabor:', ["Tradicional", "Churrasco", "Banana", "Amendoim", "Outros"])
if st.button('Atualizar'):
    atualizar_registro(id_para_atualizar, novo_produto, novo_peso, novo_sabor)
    st.success('Registro atualizado com sucesso.')

# Deletar Produtos
st.subheader('Deletar Produtos')
id_para_deletar = st.text_input('ID do produto a ser deletado:')
if st.button('Deletar'):
    deletar_registro(id_para_deletar)
    st.success('Registro deletado com sucesso.')
