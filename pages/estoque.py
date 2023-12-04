import streamlit as st
import pandas as pd
from DBConn import DBConn
from supply import Supply

supply = Supply(DBConn())

st.title('Controle de Estoque')

df_estoque = supply.obter_produtos_e_estoque()
df_estoque['Quantidade_estoque'] = df_estoque['Quantidade_estoque'].fillna(0).astype(int)


st.subheader('Produtos e Estoque')
if not df_estoque.empty:
    st.table(df_estoque)
else:
    st.warning('Não há produtos cadastrados ou informações de estoque.')

st.subheader('Atualizar Quantidade em Estoque')
id_produto_estoque = st.text_input('ID do produto:')
nova_quantidade_estoque = st.number_input('Nova Quantidade em Estoque:',step = 1)
if st.button('Atualizar Estoque'):
    supply.atualizar_quantidade_estoque(id_produto_estoque, nova_quantidade_estoque)
    st.success('Estoque atualizado com sucesso.')
