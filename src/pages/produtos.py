import streamlit as st

import streamlit as st

def cadastrar_produto():
    st.title("Cadastro de Produtos")

    # Campos do formulário
    nome_produto = st.text_input("Nome do Produto")
    codigo_produto = st.text_input("Código do Produto")
    
    # Verifica se o código do produto tem mais de 5 caracteres
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

    # Botão para cadastrar o produto
    if st.button("Cadastrar Produto"):
        # Lógica para salvar os dados no banco de dados ou em outro local
        st.success("Produto cadastrado com sucesso!")

# Chama a função para exibir o formulário
cadastrar_produto()
