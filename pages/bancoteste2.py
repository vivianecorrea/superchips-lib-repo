import streamlit as st
import sqlite3
import os

# Obtém o caminho absoluto para o arquivo do banco de dados

# Obtém o caminho absoluto para o arquivo do banco de dados
db_path = os.path.join(os.getcwd(), 'db', 'meu_banco.db')

# Função para criar a tabela se ela não existir
def criar_tabela():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo registro na tabela
def inserir_registro(nome, idade):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO registros (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()
    conn.close()

# Streamlit UI
st.title('Teste de Conexão SQLite e Inserção de Registros')

# Cria a tabela se não existir
criar_tabela()

# Formulário para inserir um novo registro
nome = st.text_input('Nome:')
idade = st.number_input('Idade:')
if st.button('Adicionar Registro'):
    inserir_registro(nome, idade)
    st.success('Registro adicionado com sucesso.')

# Mostra os registros existentes na tabela
st.title('Registros na Tabela')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('SELECT * FROM registros')
registros = cursor.fetchall()
conn.close()

if registros:
    st.table(registros)
else:
    st.warning('Não há registros na tabela.')
