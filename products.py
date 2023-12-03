import pandas as pd
from DBConn import DBConn

class Product: 
    def __init__(self, db_connection: DBConn):
        self.db_connection = db_connection

    def inserir_registro(self, produto, peso, sabor):
        self.db_connection.executar_operacao('INSERT INTO Produtos (Produto, Peso, Sabor) VALUES (?, ?, ?)', (produto, peso, sabor))

    def obter_registros(self):
        query = 'SELECT ID_Produto, Produto, Peso, Sabor FROM Produtos'
        self.db_connection.executar_operacao(query)
        df = pd.read_sql_query(query, self.db_connection.connection)
        df = df.reset_index(drop=True)
        return df

    def atualizar_registro(self, id_produto, novo_produto, novo_peso, novo_sabor):
        query = 'UPDATE Produtos SET Produto=?, Peso=?, Sabor=? WHERE ID_Produto=?'
        self.db_connection.executar_operacao(query, (novo_produto, novo_peso, novo_sabor, id_produto))

    def deletar_registro(self, id_produto):
        query = 'DELETE FROM Produtos WHERE ID_Produto=?'
        self.db_connection.executar_operacao(query, (id_produto))
