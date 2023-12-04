import streamlit as st
import sqlite3
import pandas as pd
import orde

create_sales_table()

st.title('Registro de Vendas')

sales_df = show_sales_summary()
st.write('### Resumo das Vendas')
st.write(sales_df)

st.write('### Adicionar Nova Venda')
product = st.text_input('Produto')
amount = st.number_input('Quantidade', min_value=1)
date = st.date_input('Data')
if st.button('Adicionar Venda'):
    add_sale(product, amount, date)
    st.success('Venda adicionada com sucesso!')

st.write('### Editar Venda Existente')
edit_id = st.number_input('ID da Venda a Editar', min_value=1)
edit_product = st.text_input('Novo Produto')
edit_amount = st.number_input('Nova Quantidade', min_value=1)
edit_date = st.date_input('Nova Data')
if st.button('Editar Venda'):
    edit_sale(edit_id, edit_product, edit_amount, edit_date)
    st.success('Venda editada com sucesso!')

st.write('### Excluir Venda')
delete_id = st.number_input('ID da Venda a Excluir', min_value=1)
if st.button('Excluir Venda'):
    delete_sale(delete_id)
    st.success('Venda excluída com sucesso!')