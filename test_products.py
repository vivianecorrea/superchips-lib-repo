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

def test_obter_registros(mock_db_connection):
    product = Product(mock_db_connection)
    
    query = 'SELECT ID_Produto, Produto, Peso, Sabor FROM Produtos'
    
    mock_db_connection.executar_operacao.return_value = pd.DataFrame({
        'ID_Produto': [1, 2],
        'Produto': ['Apple', 'Orange'],
        'Peso': [100, 120],
        'Sabor': ['Sweet', 'Citrus']
    })
    
    result = product.obter_registros()
    
    # Assert that the method fetched the data and returned a DataFrame
    mock_db_connection.executar_operacao.assert_called_once_with(query)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2  # Check the length of the returned DataFrame
