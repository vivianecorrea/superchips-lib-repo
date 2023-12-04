import unittest
import sqlite3
import os
from database_functions import conectar_banco, obter_clientes, atualizar_cliente, deletar_cliente

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.getcwd(), 'db', 'test_superchips.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                Id_Cliente INTEGER PRIMARY KEY,
                Nome TEXT,
                Email TEXT,
                Telefone TEXT,
                Cidade TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.cursor.execute('DROP TABLE IF EXISTS Clientes')
        self.conn.commit()
        self.conn.close()
        os.remove(self.db_path)

    def test_conectar_banco(self):
        conn = conectar_banco()
        self.assertIsInstance(conn, sqlite3.Connection)

    def test_obter_clientes(self):
        self.cursor.execute('INSERT INTO Clientes VALUES (1, "Cliente 1", "email1@example.com", "123456789", "Cidade A")')
        self.conn.commit()

        clientes = obter_clientes()
        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0][0], 1)
        self.assertEqual(clientes[0][1], "Cliente 1")

    def test_atualizar_cliente(self):
        self.cursor.execute('INSERT INTO Clientes VALUES (1, "Cliente 1", "email1@example.com", "123456789", "Cidade A")')
        self.conn.commit()

        atualizar_cliente(1, "Novo Nome", "novoemail@example.com", "987654321", "Cidade B")

        self.cursor.execute('SELECT * FROM Clientes WHERE Id_Cliente = 1')
        cliente_atualizado = self.cursor.fetchone()

        self.assertEqual(cliente_atualizado[1], "Novo Nome")
        self.assertEqual(cliente_atualizado[2], "novoemail@example.com")

    def test_deletar_cliente(self):
        self.cursor.execute('INSERT INTO Clientes VALUES (1, "Cliente 1", "email1@example.com", "123456789", "Cidade A")')
        self.conn.commit()

        deletar_cliente(1)

        self.cursor.execute('SELECT * FROM Clientes WHERE Id_Cliente = 1')
        cliente_deletado = self.cursor.fetchone()

        self.assertIsNone(cliente_deletado)

if __name__ == '__main__':
    unittest.main()
