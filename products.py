import streamlit as st
import  conexao


cursor = conexao.conecta_banco().cursor()

class Product: 
    def __init__(self, category, pct_size, name):
        self.category = category
        self.pct_size = pct_size
        self.name = name 

    def set_product_info(self, category, pct_size, name):
        query = f"INSERT INTO produtos (nome_produto, categoria, tam_pac) VALUES ('{name}', '{category}', '{pct_size}');"
        return query 

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
        cadastrar_produto_submit = st.form_submit_button(label="Cadastrar Novo Produto", type="secondary", use_container_width=True)

        if cadastrar_produto_submit:
            new_product = Product(categoria, tamanho, nome_produto)
            if new_product.register_new_product(categoria, tamanho, nome_produto):
                #cursor.execute(new_product.set_product_info(categoria, tamanho[0],nome_produto) )
                cursor.execute("INSERT INTO produtos (nome_produto, categoria, tam_pac) VALUES  (%s, %s, %s);",['TESTEE', 'Amendoim', 'P'] )
                conexao.commit()
                #FIXME: débito técnico 
                st.success(f"Produto cadastrado: {nome_produto}, Categoria: {categoria}, Tamanho: {tamanho}")
            else:
                st.error("Falha ao cadastrar o produto. Verifique as informações.")

