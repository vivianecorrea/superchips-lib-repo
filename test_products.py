import pytest
from unittest.mock import Mock
import pandas as pd

from products import Product

@pytest.fixture
def mock_db_connection():
    return Mock()

def test_inserir_registro(mock_db_connection):
    product = Product(mock_db_connection)
    
    produto = 'Apple'
    peso = 100
    sabor = 'Sweet'
    product.inserir_registro(produto, peso, sabor)
    
    mock_db_connection.executar_operacao.assert_called_once_with(
        'INSERT INTO Produtos (Produto, Peso, Sabor) VALUES (?, ?, ?)',
        (produto, peso, sabor)
    )

def test_atualizar_registro(mock_db_connection):
    product = Product(mock_db_connection)

    id_produto = 1
    novo_produto = 'Updated Product'
    novo_peso = 150
    novo_sabor = 'New Flavor'

    product.atualizar_registro(id_produto, novo_produto, novo_peso, novo_sabor)

    query = 'UPDATE Produtos SET Produto=?, Peso=?, Sabor=? WHERE ID_Produto=?'

    mock_db_connection.executar_operacao.assert_called_once_with(
        query, (novo_produto, novo_peso, novo_sabor, id_produto)
    )

def test_deletar_registro(mock_db_connection):
    product = Product(mock_db_connection)

    id_produto = 1

    product.deletar_registro(id_produto)

    query = 'DELETE FROM Produtos WHERE ID_Produto=?'

    mock_db_connection.executar_operacao.assert_called_once_with(
        query, (id_produto)
    )
 

