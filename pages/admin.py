import streamlit as st
import sqlalchemy

#débito técnico : padronizar o gerenciamento de regra e exibição 
class AdminUI:
    def __init__(self):
        self.conn = st.connection('mysql', type='sql')

    def get_usuarios_df(self):
        return self.conn.query('SELECT username, role from usuarios;', ttl=600)

    def show_user_info(self, user, col1, col2, col3, col4):
        # Lógica de apresentação para mostrar informações de um usuário
        col1.write(f"{user.username}")
        col2.write(f"{user.role}")
        col3.button("Excluir", type="secondary", key=f"delete_{user}")
        col4.button("Alterar", type="secondary", key=f"alter_{user}")

    def main(self):
        st.title('Olá Admin Superchips !')
        st.write(' Gerencie aqui os seus usuários')

        # Lógica de negócios para obter os dados dos usuários
        df = self.get_usuarios_df()

        col1, col2, col3, col4 = st.columns(4)

        col1.subheader('Usuário', divider='gray')
        col2.subheader('Role', divider='gray')
        col3.subheader('But', divider='gray')
        col4.subheader('But', divider='gray')

        # Lógica de apresentação para mostrar informações de cada usuário
        for user in df.itertuples(): 
            self.show_user_info(user, col1, col2, col3, col4)

        st.subheader(' ', divider='gray')

        st.button('Criar novo usuário', type="primary")

# Crie uma instância da classe e chame o método main
app = AdminUI()
app.main()
