import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import os 
from calendar import Calendar
from DBConn import DBConn 


calendar = Calendar(DBConn())
st.title('Calendário Logístico')

calendar.criar_tabela_eventos()

titulo = st.text_input('Título do Evento:')
descricao = st.text_area('Descrição do Evento:')
data = st.date_input('Data do Evento:', value=datetime.now())
hora = st.time_input('Hora do Evento:', value=datetime.now().time())

if st.button('Adicionar Evento'):
    calendar.inserir_evento(titulo, descricao, data, hora)
    st.success('Evento adicionado com sucesso.')


eventos = calendar.obter_eventos()
df_eventos = pd.DataFrame(eventos, columns=['Id_Evento', 'Título', 'Descrição', 'Data', 'Hora'])
st.subheader('Lista de Eventos:')
st.table(df_eventos)
