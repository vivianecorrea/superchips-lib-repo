import streamlit as st 
import products, structs

import streamlit as st

class ProductUI:
    def __init__(self):
        #self.conn = st.connection('mysql', type='sql')
        pass

    def get_produtos_df(self):
        # return self.conn.query('SELECT nome_produto, categoria, tam_pac from produtos;', ttl=600)
        return [{"nome_produto": "Amendoim Sortido pequeno", "categoria": "Amendoim", "tam_pac": "P (300g)"}]

    def show_product_info(self, product, col1, col2, col3, col4):
        col1.write(f"{product['nome_produto']}")
        col2.write(f"{product['categoria']}")
        col3.write(f"{product['tam_pac']}")
        col4.button("Alterar", type="secondary", key=f"alter_{product['nome_produto']}")

    def main(self):
        st.title('Olá Admin Superchips !')
        st.write(' Gerencie aqui os seus produtos')

        df = self.get_produtos_df()

        if 'products' not in st.session_state:
            st.session_state['products'] = df

        col1, col2, col3, col4 = st.columns(4)

        col1.subheader('Produto', divider='gray')
        col2.subheader('Categoria', divider='gray')
        col3.subheader('Tamanho', divider='gray')
        col4.subheader('Opções', divider='gray')

        for product in st.session_state['products']:
            self.show_product_info(product, col1, col2, col3, col4)

        st.subheader(' ', divider='gray')
            
            



with st.sidebar:
    structs.get_image()
    structs.get_main_components()
    structs.back_home()


app = ProductUI()
app.main()

products.show_product_register_form()


