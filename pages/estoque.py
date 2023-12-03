import streamlit as st
import sqlite3
import os
import pandas as pd

# TODO: Criar métodos de conexão com o banco com isso:
db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
conn = sqlite3.connect(db_path)

def obter_produtos_e_estoque():
    cursor = conn.cursor()
    query = '''
        SELECT p.ID_Produto, p.Produto, p.Peso, p.Sabor, e.Quantidade_estoque
        FROM Produtos p
        LEFT JOIN Estoque e ON p.ID_Produto = e.ID_Produto
    '''
    cursor.execute(query)
    df = pd.read_sql_query(query, conn)
    df = df.reset_index(drop=True)
    return df

def atualizar_quantidade_estoque(id_produto, nova_quantidade):
    cursor = conn.cursor()
    # Se não existir entrada no estoque para o produto, insere uma nova
    cursor.execute('INSERT OR IGNORE INTO Estoque (ID_Produto) VALUES (?)', (id_produto,))
    # Atualiza a quantidade em estoque
    cursor.execute('UPDATE Estoque SET Quantidade_estoque=? WHERE ID_Produto=?', (nova_quantidade, id_produto))
    conn.commit()

# Streamlit UI
st.title('Controle de Estoque')

# Obtém produtos e estoque
df_estoque = obter_produtos_e_estoque()
df_estoque['Quantidade_estoque'] = df_estoque['Quantidade_estoque'].fillna(0).astype(int)


# Exibe tabela de produtos e estoque
st.subheader('Produtos e Estoque')
if not df_estoque.empty:
    st.table(df_estoque)
else:
    st.warning('Não há produtos cadastrados ou informações de estoque.')

# Atualiza a quantidade em estoque
st.subheader('Atualizar Quantidade em Estoque')
id_produto_estoque = st.text_input('ID do produto:')
nova_quantidade_estoque = st.number_input('Nova Quantidade em Estoque:',step = 1)
if st.button('Atualizar Estoque'):
    atualizar_quantidade_estoque(id_produto_estoque, nova_quantidade_estoque)
    st.success('Estoque atualizado com sucesso.')
