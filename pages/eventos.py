import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import os 

# Método de conexão com o banco de dados SQLite
def conectar_banco():
    db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
    conn = sqlite3.connect(db_path)
    return conn

# Método para criar a tabela de eventos no banco de dados
def criar_tabela_eventos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Eventos (
            Id_Evento INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo VARCHAR(100) NOT NULL,
            Descricao TEXT,
            Data DATE NOT NULL,
            Hora TIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Método para inserir um evento na tabela de eventos
def inserir_evento(titulo, descricao, data, hora):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Eventos (Titulo, Descricao, Data, Hora) VALUES (?, ?, ?, ?)', (titulo, descricao, data, hora))
    conn.commit()
    conn.close()

# Método para obter todos os eventos da tabela
def obter_eventos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Eventos')
    eventos = cursor.fetchall()
    conn.close()
    return eventos

# Criar a tabela de eventos (chamado uma vez)
criar_tabela_eventos()

# Streamlit UI
st.title('Calendário Logístico')

# Formulário para adicionar um novo evento
titulo = st.text_input('Título do Evento:')
descricao = st.text_area('Descrição do Evento:')
data = st.date_input('Data do Evento:', value=datetime.now())
hora = st.time_input('Hora do Evento:', value=datetime.now().time())

if st.button('Adicionar Evento'):
    inserir_evento(titulo, descricao, data, hora)
    st.success('Evento adicionado com sucesso.')

# Exibir a lista de eventos na tabela
eventos = obter_eventos()
df_eventos = pd.DataFrame(eventos, columns=['Id_Evento', 'Título', 'Descrição', 'Data', 'Hora'])
st.subheader('Lista de Eventos:')
st.table(df_eventos)
