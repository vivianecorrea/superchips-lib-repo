import unittest
import sqlite3
import os
from datetime import datetime


from classe_order import Order  

class TestOrderMethods(unittest.TestCase):
    def setUp(self):
        self.db_connection = sqlite3.connect(':memory:')  
        self.order = Order(self.db_connection)
        
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produtos (
                ID_Produto INTEGER PRIMARY KEY,
                Produto TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pedidos (
                ID_Pedido INTEGER PRIMARY KEY,
                ID_Produto INTEGER,
                Quantidade INTEGER,
                Data_Pedido TEXT,
                Status TEXT,
                Data_Entrega_Prevista TEXT,
                Operador_Responsavel TEXT
            )
        ''')

    def test_obter_produtos(self):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Produtos (ID_Produto, Produto) VALUES (1, 'Produto Teste 1')")
        cursor.execute("INSERT INTO Produtos (ID_Produto, Produto) VALUES (2, 'Produto Teste 2')")

        produtos = self.order.obter_produtos()

        self.assertEqual(len(produtos), 2)
        self.assertEqual(produtos[0][0], 1)
        self.assertEqual(produtos[1][1], 'Produto Teste 2')

    def test_inserir_pedido_e_obter_pedidos(self):
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.order.inserir_pedido(1, 10, data_atual, 'Em andamento', '2023-12-31', 'Operador Teste')

        pedidos = self.order.obter_pedidos()

        self.assertEqual(len(pedidos), 1)
        self.assertEqual(pedidos['Quantidade'][0], 10)
        self.assertEqual(pedidos['Status'][0], 'Em andamento')

if __name__ == '__main__':
    unittest.main()
