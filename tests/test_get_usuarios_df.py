import pytest
import streamlit as st


@pytest.mark.skip(reason="Débito técnico problemas de conexão com o banco ")
def test_get_usuarios_df(app_instance, monkeypatch):
    # Simula a lógica de negócios para a função self.conn.query
    class MockConnection:
        def query(self, query, ttl):
            # Simula um retorno de DataFrame para a query
            return {'username': ['user1', 'user2'],
                    'role': ['role1', 'role2']}

    # Substitui a conexão real pelo objeto de conexão simulado
    monkeypatch.setattr(app_instance, 'conn', MockConnection())

    # Chama o método e verifica o resultado
    df = app_instance.get_usuarios_df()
    
    # Verifica se os dados retornados correspondem ao esperado
    assert df['username'][0] == 'user1'
    assert df['role'][0] == 'role1'

    assert df['username'][1] == 'user2'
    assert df['role'][1] == 'role2'
