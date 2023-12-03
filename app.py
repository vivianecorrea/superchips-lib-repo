import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from faker import *
import random 

# Configuração do Faker
fake = Faker()

# Função para gerar dados mockados de produtos
def gerar_dados_produtos(qtd_produtos=10):
    produtos = []
    for _ in range(qtd_produtos):
        produto = {
            'ID_Produto': random.randint(1, 100),
            'Produto': fake.word(),
            'Peso': f"{random.choice([300, 500, 700])} g",
            'Preco': round(random.uniform(1, 10), 2),
            'Sabor': fake.word(),
            'Quantidade': random.randint(1, 100)
        }
        produtos.append(produto)
    return produtos

# Gerar dados mockados
dados_produtos = gerar_dados_produtos()

# Converter dados para DataFrames
df_produtos = pd.DataFrame(dados_produtos)

# Streamlit UI
st.title('Dashboard Superchips')

col1, col2 = st.columns(2)

# Exibir gráfico de quantidade de estoque por produto (Gráfico de Barras)
st.subheader('Quantidade Atual de Estoque por Produto (Gráfico de Barras)')
fig_estoque_bar = px.bar(df_produtos, x='Produto', y='Quantidade', title='Quantidade Atual de Estoque por Produto')
st.plotly_chart(fig_estoque_bar)
# Seção de Controle de Estoque

st.header('Controle de Estoque')
# Card com número (Quantidade total de produtos)
st.header('KPI: Quantidade Total de Produtos')
kpi_quantidade_total = df_produtos['Quantidade'].sum()
st.metric(label='Quantidade Total de Produtos', value=kpi_quantidade_total, delta="Total")


# Exibir gráfico de distribuição de sabores (Gráfico de Pizza)
st.subheader('Distribuição de Sabores (Gráfico de Pizza)')
fig_sabores_pizza = px.pie(df_produtos, names='Sabor', title='Distribuição de Sabores')
st.plotly_chart(fig_sabores_pizza)



# Exibir gráfico de dispersão entre preço e quantidade (Gráfico de Dispersão)
st.subheader('Relação entre Preço e Quantidade (Gráfico de Dispersão)')
fig_dispersao = px.scatter(df_produtos, x='Preco', y='Quantidade', title='Relação entre Preço e Quantidade')
st.plotly_chart(fig_dispersao)

# Exibir gráfico de linha para visualizar a variação do preço (Gráfico de Linha)
st.subheader('Variação do Preço ao Longo do Tempo (Gráfico de Linha)')
df_variacao_preco = pd.DataFrame({
    'Data': [fake.date_between('-30d', 'today') for _ in range(50)],
    'Preco': np.random.uniform(1, 10, 50)
})
fig_variacao_preco = px.line(df_variacao_preco, x='Data', y='Preco', title='Variação do Preço ao Longo do Tempo')
st.plotly_chart(fig_variacao_preco)



# Placeholder para funcionalidades adicionais
