from src.structs import *
from src.login import *
import streamlit as st



# Função principal do aplicativo
def main():
    # Chama a função de login
    if login():
        # Se o login for bem-sucedido, exibe o restante do aplicativo
        st.success("Login bem-sucedido!")
        st.write("Conteúdo do aplicativo após a autenticação.")

        with st.sidebar:
            get_image()
            get_main_components()

# Chama a função principal do aplicativo
if __name__ == "__main__":
    main()



    