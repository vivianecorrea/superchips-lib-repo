import sqlite3
from DBConnSingleton import DBConnSingleton
import os

class DBConn(metaclass=DBConnSingleton):
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(os.getcwd(), 'db', 'superchips.db'), check_same_thread=False)

    def executar_operacao(self, query, parameters=()):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        self.connection.commit()
    
    def executar_operacao_em_lista(self, query_objects):
        for query_object in query_objects:
            cursor = self.connection.cursor()
            cursor.execute(query_object['query'], query_object['parameters'])            
        self.connection.commit()
