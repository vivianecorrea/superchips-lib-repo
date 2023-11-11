import streamlit as st
import sqlalchemy
import pandas as pd
import numpy as np
from user import container_cadastrar_usuario
st.title('Olá Admin Superchips !')
st.write(' Gerencie aqui os seus usuários')
conn = st.connection('mysql', type='sql')


df = conn.query('SELECT username, role from usuarios;', ttl=600)
col1, col2, col3, col4 = st.columns(4)


col1.subheader('Usuário', divider='gray')
col2.subheader('Role', divider='gray')
col3.subheader('But', divider='gray')
col4.subheader('But', divider='gray')

for user in df.itertuples(): 
    col1.write(f"{user.username}")
    col2.write(f"{user.role}")
    col3.button("Excluir", type="secondary")
    col4.button("Alterar", type="secondary")

st.subheader(' ', divider='gray')

if st.button('Criar novo usuário', type="primary"):
    container_cadastrar_usuario()

