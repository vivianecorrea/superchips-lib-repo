import streamlit as st

class Product: 
    def __init__(self, category, pct_size, name):
        self.category = category
        self.pct_size = pct_size
        self.name = name 

    def register_new_product(self, categoria, tamanho, nome_produto):
        if tamanho not in ["P (100 g)", "M (300g)", "G (500g)"]:
            return False
        categorias_validas = ["Banana", "Batata", "Amendoim"]
        if categoria not in categorias_validas:
            return False

        if len(nome_produto) > 100:
            return False

        return True

def show_product_register_form():
    st.title('Cadastrar novo produto')

    with st.form("my_form"):
        categoria = st.selectbox("Categoria:", ["Banana", "Batata", "Amendoim"])
        tamanho = st.selectbox("Tamanho:", ["P (100 g)", "M (300g)", "G (500g)"])
        nome_produto = st.text_input("Nome do Produto:")

        if st.form_submit_button("Cadastrar novo Produto"):
            update_product_list(nome_produto, categoria, tamanho)

def update_product_list(nome_produto, categoria, tamanho):
        new_product = {"nome_produto": nome_produto, "categoria": categoria, "tam_pac": tamanho}
        if 1 == 1:
            st.session_state['products'].append(new_product)
            st.success(f"Produto cadastrado: {nome_produto}, Categoria: {categoria}, Tamanho: {tamanho}")
        else:
            st.error("Falha ao cadastrar o produto. Verifique as informações.")
