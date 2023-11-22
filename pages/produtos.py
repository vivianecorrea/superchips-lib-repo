import streamlit as st 
import products, structs, conexao


#cursor = conexao.conecta_banco().cursor()

import streamlit as st

class ProductUI:
    def __init__(self):
        self.conn = st.connection('mysql', type='sql')

    def get_produtos_df(self):
        return self.conn.query('SELECT nome_produto, categoria, tam_pac from produtos;', ttl=600)

    def show_product_info(self, product, col1, col2, col3, col4):
        # Lógica de apresentação para mostrar informações de um produto
        col1.write(f"{product.nome_produto}")
        col2.write(f"{product.categoria}")
        col3.write(f"{product.tam_pac}")
        col4.button("Alterar", type="secondary", key=f"alter_{product.nome_produto}")

    def main(self):
        st.title('Olá Admin Superchips !')
        st.write(' Gerencie aqui os seus produtos')

        # Lógica de negócios para obter os dados dos produtos
        df = self.get_produtos_df()

        col1, col2, col3, col4 = st.columns(4)

        col1.subheader('Produto', divider='gray')
        col2.subheader('Categoria', divider='gray')
        col3.subheader('Tamanho', divider='gray')
        col4.subheader('Opções', divider='gray')

        # Lógica de apresentação para mostrar informações de cada produto
        for product in df.itertuples():
            self.show_product_info(product, col1, col2, col3, col4)

        st.subheader(' ', divider='gray')

        st.button('Adicionar novo produto', type="primary")

# Crie uma instância da classe e chame o método main




with st.sidebar:
    structs.get_image()
    structs.get_main_components()
    structs.back_home()
    

products.show_product_register_form()

col1, col2 = st.columns(2)
if col1.button(" Produtos Cadastrados", key ="Cadastrados", type="secondary", use_container_width=True):
   app = ProductUI()
   app.main()
    
col2.button("Estoque", key ="Estoque", type="secondary", use_container_width=True)


