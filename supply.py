from DBConn import DBConn
import pandas as pd 

class Supply: 
    def __init__(self, db_connection: DBConn):
        self.db_connection = db_connection


    def obter_produtos_e_estoque(self):
        query = '''
            SELECT p.ID_Produto, p.Produto, p.Peso, p.Sabor, e.Quantidade_estoque
            FROM Produtos p
            LEFT JOIN Estoque e ON p.ID_Produto = e.ID_Produto
        '''
        self.db_connection.executar_operacao(query)
        df = pd.read_sql_query(query, self.db_connection.connection)
        df = df.reset_index(drop=True)
        return df
    

    def atualizar_quantidade_estoque(self, id_produto, nova_quantidade):
        query_objects = [
        {
            'query': 'INSERT OR IGNORE INTO Estoque (ID_Produto) VALUES (?)',
            'parameters': (id_produto)
        },
        {
            'query': 'UPDATE Estoque SET Quantidade_estoque=? WHERE ID_Produto=?',
            'parameters': (nova_quantidade, id_produto)
        }
        ]
        self.db_connection.executar_operacao_em_lista(query_objects)