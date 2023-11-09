import pytest
from unittest.mock import patch
import streamlit as st

def cadastrar_produto():
    st.title("Cadastro de Produtos")
    nome_produto = st.text_input("Nome do Produto")
    codigo_produto = st.text_input("Código do Produto")
    
    if len(codigo_produto) <= 5:
        st.warning("O código do produto deve ter mais de 5 caracteres.")
        st.stop()

    categoria = st.selectbox("Categoria", ["Snacks", "Chips", "Salgadinhos"])
    marca = st.text_input("Marca")
    fornecedor = st.text_input("Fornecedor")
    descricao = st.text_area("Descrição")
    preco_compra = st.number_input("Preço de Compra", min_value=0.0)
    preco_venda = st.number_input("Preço de Venda", min_value=0.0)
    quantidade_estoque = st.number_input("Quantidade em Estoque", min_value=0)
    unidade_medida = st.text_input("Unidade de Medida")
    data_validade = st.date_input("Data de Validade")
    local_estoque = st.text_input("Localização no Estoque")
    alerta_estoque_minimo = st.number_input("Alerta de Estoque Mínimo", min_value=0)
    imagem_produto = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

    if st.button("Cadastrar Produto"):
        st.success("Produto cadastrado com sucesso!")

# Teste para cadastro bem-sucedido
def test_cadastro_produto_sucesso():
    with patch.object(st, 'text_input', return_value='Super Chips'):
        with patch.object(st, 'text_input', return_value='123456'):
            with patch.object(st, 'selectbox', return_value='Chips'):
                with patch.object(st, 'text_input', return_value='SuperBrand'):
                    with patch.object(st, 'text_input', return_value='FornecedorX'):
                        with patch.object(st, 'text_area', return_value='Deliciosos chips de batata'):
                            with patch.object(st, 'number_input', return_value=2.0):
                                with patch.object(st, 'number_input', return_value=4.0):
                                    with patch.object(st, 'number_input', return_value=100):
                                        with patch.object(st, 'text_input', return_value='Pacotes'):
                                            with patch.object(st, 'date_input', return_value='2023-01-01'):
                                                with patch.object(st, 'text_input', return_value='Prateleira A'):
                                                    with patch.object(st, 'number_input', return_value=10):
                                                        with patch.object(st, 'file_uploader', return_value=None):
                                                            with patch.object(st, 'button', return_value=True):
                                                                with patch.object(st, 'success', return_value=None):
                                                                    cadastrar_produto()

# Teste para código do produto muito curto
def test_cadastro_produto_codigo_curto():
    with patch.object(st, 'text_input', return_value='Super Chips'):
        with patch.object(st, 'text_input', return_value='123'):
            with patch.object(st, 'warning', return_value=None):
                cadastrar_produto()

# Implemente mais testes para outros cenários, como valores inválidos, etc.