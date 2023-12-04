import streamlit as st
from datetime import date
from class_sales import Sales  

Sales.create_sales_table()

Sales.add_sale('Product A', 100, date.today())

sales_summary = Sales.show_sales_summary()
st.write("Resumo das vendas:")
st.write(sales_summary)

Sales.edit_sale(1, 'Product B', 150, date.today())

updated_sales_summary = Sales.show_sales_summary()
st.write("Resumo das vendas após edição:")
st.write(updated_sales_summary)

Sales.delete_sale(1)

updated_sales_summary = Sales.show_sales_summary()
st.write("Resumo das vendas após exclusão:")
st.write(updated_sales_summary)
