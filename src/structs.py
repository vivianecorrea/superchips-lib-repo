import streamlit as st
from PIL import Image



def get_image():
    image = Image.open('img\superchips-logo.png')
    st.image(image)


def get_main_components():
    buttons = ["Produtos", "Estoque", "Pedidos", "Vendas", "Admin"]
    return [st.button(button, use_container_width=True) for button in buttons]

def back_home():
    st.button("Home", use_container_width = True)

