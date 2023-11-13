import streamlit as st

#from structs import get_main_components  -- débito técnico: erro de import

def get_main_components():
    buttons = ["Produtos", "Estoque", "Pedidos", "Vendas", "Admin"]
    return [st.button(button, use_container_width=True) for button in buttons]

def test_get_main_components():
    components = get_main_components()
    assert len(components) == 5
   