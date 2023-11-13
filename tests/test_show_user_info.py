import pytest

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



@pytest.mark.skip(reason="Débito técnico problemas de conexão com o banco ")
def test_show_user_info(app_instance, mocker):
    # Mock dos objetos col1, col2, col3, col4 do Streamlit
    mock_col1 = mocker.MagicMock()
    mock_col2 = mocker.MagicMock()
    mock_col3 = mocker.MagicMock()
    mock_col4 = mocker.MagicMock()

    # Dados de exemplo do usuário
    user = mocker.MagicMock(username="John", role="Admin")

    # Chama a função que você deseja testar
    app_instance.show_user_info(user, mock_col1, mock_col2, mock_col3, mock_col4)

    # Verifica se as funções do Streamlit foram chamadas corretamente
    mock_col1.write.assert_called_once_with("John")
    mock_col2.write.assert_called_once_with("Admin")
    mock_col3.button.assert_called_once_with("Excluir", type="secondary", key="delete_John")
    mock_col4.button.assert_called_once_with("Alterar", type="secondary", key="alter_John")

    