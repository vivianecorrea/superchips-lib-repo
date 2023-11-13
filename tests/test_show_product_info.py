import pytest 
import streamlit as st 

class FakeStreamlitColumn:
    def __init__(self):
        self.content = None
        self.button_label = None
        self.button_type = None
        self.button_key = None

    def write(self, content):
        self.content = content

    def button(self, label, type, key):
        self.button_label = label
        self.button_type = type
        self.button_key = key

class ProductUI:
    def __init__(self):
        self.conn = st.connection('mysql', type='sql')


    def show_product_info(self, product, col1, col2, col3, col4):
        # Lógica de apresentação para mostrar informações de um produto
        col1.write(f"{product.nome_produto}")
        col2.write(f"{product.categoria}")
        col3.write(f"{product.tam_pac}")
        col4.button("Alterar", type="secondary", key=f"alter_{product.nome_produto}")

@pytest.mark.skip(reason="Débito técnico problemas de conexão com o banco ")
def test_show_product_info():
    product_ui = ProductUI()
    fake_product = ('Produto1', 'Banana', 'P (100 g)')
    col1 = FakeStreamlitColumn()
    col2 = FakeStreamlitColumn()
    col3 = FakeStreamlitColumn()
    col4 = FakeStreamlitColumn()

    product_ui.show_product_info(fake_product, col1, col2, col3, col4)
    assert col1.content == 'Produto1'
    assert col2.content == 'Banana'
    assert col3.content == 'P (100 g)'
    assert col4.button_label == "Alterar"
    assert col4.button_type == "secondary"
    assert col4.button_key == "alter_Produto1"
