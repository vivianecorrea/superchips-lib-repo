import pytest
from unittest.mock import Mock
import pandas as pd

from class_supply import Supply

@pytest.fixture
def mock_db_connection():
    return Mock()

def test_atualizar_quantidade_estoque(mock_db_connection):
    supply = Supply(mock_db_connection)

    id_produto = 1
    nova_quantidade = 100

    supply.atualizar_quantidade_estoque(id_produto, nova_quantidade)

    expected_query_objects = [
        {
            'query': 'INSERT OR IGNORE INTO Estoque (ID_Produto) VALUES (?)',
            'parameters': (id_produto)
        },
        {
            'query': 'UPDATE Estoque SET Quantidade_estoque=? WHERE ID_Produto=?',
            'parameters': (nova_quantidade, id_produto)
        }
    ]

    mock_db_connection.executar_operacao_em_lista.assert_called_once_with(expected_query_objects)
