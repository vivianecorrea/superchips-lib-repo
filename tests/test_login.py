import streamlit as st
import pytest
from unittest.mock import Mock


def login():
    st.title("Login Form")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Verifica as credenciais (substitua por sua lógica de autenticação real)
        if username == "user" and password == "password":
            return True
        else:
            st.error("Credenciais inválidas. Tente novamente.")
    
    return False

def test_login_valid_credentials(mocker):
    # Simula a entrada de texto e o botão do Streamlit
    mocker.patch.object(st, 'text_input', side_effect=["user", "password"])
    mocker.patch.object(st, 'button', return_value=True)

    # Chama a função de login
    result = login()

    # Verifica se o login foi bem-sucedido
    assert result is True

def test_login_invalid_credentials(mocker):
    # Simula a entrada de texto e o botão do Streamlit com credenciais inválidas
    mocker.patch.object(st, 'text_input', side_effect=["user", "wrong_password"])
    mocker.patch.object(st, 'button', return_value=True)
    mocker.patch.object(st, 'error')

    # Chama a função de login
    result = login()

    # Verifica se a função de erro foi chamada
    st.error.assert_called_once()

    # Verifica se o login foi mal-sucedido
    assert result is False
