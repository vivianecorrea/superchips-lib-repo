import streamlit as st

def login():
    st.title("Login Form")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "vivi" and password == "1234":
        #TODO: conectar com o banco 
            return True
        else:
            st.error("Credenciais inválidas. Tente novamente.")
    
    return False