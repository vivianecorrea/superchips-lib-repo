import streamlit as st
from PIL import Image

def get_image():
    image = Image.open('img\superchips-logo.png')
    st.image(image)

def get_main_components():
    buttons = ["Produtos", "Estoque", "Pedidos", "Vendas", "Admin"]
    return [st.button(button, use_container_width=True) for button in buttons]

def back_home():
    st.button("Home", use_container_width=True)

def run_test():
    st.title("Teste da Classe")

    st.header("Imagem:")
    get_image()

    st.header("Componentes Principais:")
    components = get_main_components()

    st.header("Botão Home:")
    back_home()

if __name__ == "__main__":
    run_test()
