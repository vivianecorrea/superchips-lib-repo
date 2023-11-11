from hashlib import sha256
import streamlit as st

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    username = st.text_input('Insira aqui um novo username: ', 'username')
    password = st.text_input('Insira aqui a sua senha: ', 'password')
    role = st.selectbox('Selecione um perfil de acesso',
    ('Admin', 'User'))

    return username 

    