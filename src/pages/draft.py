import streamlit as st
import pandas as pd
from PIL import Image



   
def main():
    # Definindo o estado da aplicação
    state = {"page": "home"}  # Inicialmente, estamos na página inicial

    
    with st.sidebar:
    # Criando duas colunas para posicionar os botões lado a lado
        image = Image.open('img\superchips-logo.png')
        st.image(image)


        # Botão para cadastrar novo produto
        if st.button("Cadastrar Novo Produto"):
            state["page"] = "produtos"

        # Botão para gerenciar estoque
        if st.button("Gerenciar Estoque"):
            state["page"] = "estoque"

        # Botão para novo pedido
        if st.button("Novo Novo Pedido"):
            state["page"] = "pedido"

        # Botão para finalizar vendas
        if st.button("Finalizar Vendas"):
            state["page"] = "vendas"

    # Verifica o estado atual e exibe a página correspondente
    
    if state["page"] == "produtos":
        show_produtos()
    elif state["page"] == "estoque":
        show_estoque()
    elif state["page"] == "pedido":
        show_pedido()
    elif state["page"] == "vendas":
        show_vendas()

def show_produtos():
    st.header("Página de Produtos")
    st.write("Aqui você pode cadastrar novos produtos.")
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


def show_estoque():
    st.header("Página de Estoque")
    st.write("Aqui você pode gerenciar o estoque.")
    

    # Dados de exemplo - substitua isso pelos dados do seu estoque
    dados_estoque = {
        'Produto': ['Produto A', 'Produto B', 'Produto C'],
        'Quantidade': [100, 50, 75]
    }

    # Criando um DataFrame com os dados do estoque
    estoque_df = pd.DataFrame(dados_estoque)

    def atualizar_estoque():
        st.title('Formulário de Atualização de Estoque')

        # Exibindo a tabela com os produtos e quantidades atuais
        st.subheader('Estoque Atual:')
        st.table(estoque_df)

        # Criando o formulário para atualização de estoque
        st.subheader('Atualizar Estoque:')
        produto_selecionado = st.selectbox('Selecione o Produto:', estoque_df['Produto'])
        nova_quantidade = st.number_input('Digite a Nova Quantidade:', min_value=0)

        # Botão para atualizar o estoque
        if st.button('Atualizar Estoque'):
            # Atualizando o DataFrame com a nova quantidade
            estoque_df.loc[estoque_df['Produto'] == produto_selecionado, 'Quantidade'] = nova_quantidade

            # Exibindo mensagem de sucesso
            st.success(f'O estoque de {produto_selecionado} foi atualizado para {nova_quantidade} unidades.')

            # Atualizando a tabela na página
            st.table(estoque_df)

    # Chamando a função para exibir a página
    atualizar_estoque()

def show_pedido():
    st.header("Página de Pedidos")
    st.write("Aqui você pode criar novos pedidos.")

def show_vendas():
    st.header("Página de Vendas")
    st.write("Aqui você pode finalizar vendas.")

if __name__ == "__main__":
    main()
