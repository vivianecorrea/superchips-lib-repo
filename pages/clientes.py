import streamlit as st
import sqlite3
import pandas as pd
import os

def conectar_banco():
    db_path = os.path.join(os.getcwd(), 'db', 'superchips.db')
    conn = sqlite3.connect(db_path)
    return conn

def obter_clientes():
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'SELECT * FROM Clientes'
    cursor.execute(query)
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def atualizar_cliente(id_cliente, nome, email, telefone, cidade):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'UPDATE Clientes SET Nome=?, Email=?, Telefone=?, Cidade=? WHERE Id_Cliente=?'
    cursor.execute(query, (nome, email, telefone, cidade, id_cliente))
    conn.commit()
    conn.close()

def deletar_cliente(id_cliente):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'DELETE FROM Clientes WHERE Id_Cliente=?'
    cursor.execute(query, (id_cliente,))
    conn.commit()
    conn.close()

st.title('Clientes')

clientes = obter_clientes()
df_clientes = pd.DataFrame(clientes, columns=['Id_Cliente', 'Nome', 'Email', 'Telefone', 'Cidade'])

if not df_clientes.empty:
    st.subheader('Registros de Clientes')
    st.table(df_clientes)

    opcao = st.selectbox('Escolha uma opção:', ['Selecione', 'Editar', 'Deletar'])

    if opcao == 'Editar':
        st.subheader('Editar Cliente')
        id_cliente_edicao = st.number_input('ID do Cliente que deseja editar:', min_value=df_clientes['Id_Cliente'].min(), max_value=df_clientes['Id_Cliente'].max())

        cliente_selecionado = df_clientes[df_clientes['Id_Cliente'] == id_cliente_edicao].iloc[0]

        novo_nome = st.text_input('Novo Nome:', value=cliente_selecionado['Nome'])
        novo_email = st.text_input('Novo Email:', value=cliente_selecionado['Email'])
        novo_telefone = st.text_input('Novo Telefone:', value=cliente_selecionado['Telefone'])
        nova_cidade = st.text_input('Nova Cidade:', value=cliente_selecionado['Cidade'])

        if st.button('Confirmar Edição'):
            atualizar_cliente(id_cliente_edicao, novo_nome, novo_email, novo_telefone, nova_cidade)
            st.success('Cliente editado com sucesso.')

    elif opcao == 'Deletar':
        st.subheader('Deletar Cliente')
        id_cliente_delecao = st.number_input('ID do Cliente que deseja deletar:', min_value=df_clientes['Id_Cliente'].min(), max_value=df_clientes['Id_Cliente'].max())

        if st.button('Confirmar Deleção'):
            deletar_cliente(id_cliente_delecao)
            st.success('Cliente deletado com sucesso.')

else:
    st.warning('Não há registros na tabela de Clientes.')
