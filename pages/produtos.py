import streamlit as st
from products import Product
from DBConn import DBConn

product = Product(DBConn())

st.title('Produtos Superchips')
st.subheader('Cadastrar novo produto')
input_produto = st.text_input('Nome do produto:')
input_peso = st.selectbox("Tamanho Pacote:", ["300 g", "500g", "700 g"])
input_sabor = st.selectbox("Sabor:", ["Tradicional", "Churrasco", "Banana", "Amendoim", "Outros"])
if st.button('Cadastrar'):
    product.inserir_registro(input_produto, input_peso, input_sabor)
    st.success('Registro adicionado com sucesso.')

st.subheader('Produtos Cadastrados')
df = product.obter_registros()

if not df.empty:
    st.table(df)
else:
    st.warning('Não há registros na tabela.')

st.subheader('Atualizar Produtos')
id_para_atualizar = st.text_input('ID do produto a ser atualizado:')
novo_produto = st.text_input('Novo nome do produto:')
novo_peso = st.selectbox('Novo tamanho do pacote:', ["300 g", "500g", "700 g"])
novo_sabor = st.selectbox('Novo sabor:', ["Tradicional", "Churrasco", "Banana", "Amendoim", "Outros"])
if st.button('Atualizar'):
    product.atualizar_registro(id_para_atualizar, novo_produto, novo_peso, novo_sabor)
    st.success('Registro atualizado com sucesso.')

st.subheader('Deletar Produtos')
id_para_deletar = st.text_input('ID do produto a ser deletado:')
if st.button('Deletar'):
    product.deletar_registro(id_para_deletar)
    st.success('Registro deletado com sucesso.')
