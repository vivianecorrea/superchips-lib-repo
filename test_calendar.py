import unittest
from unittest.mock import MagicMock
from calendar_class import Calendar

class TestCalendar(unittest.TestCase):
    def setUp(self):
        self.mock_db_connection = MagicMock()
        self.calendar = Calendar(self.mock_db_connection)

    def test_criar_tabela_eventos(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Eventos (
            Id_Evento INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo VARCHAR(100) NOT NULL,
            Descricao TEXT,
            Data DATE NOT NULL,
            Hora TIME NOT NULL
            )
        '''
        self.calendar.criar_tabela_eventos()
        self.mock_db_connection.executar_operacao.assert_called_once_with(query)

    def test_inserir_evento(self):
        titulo = "Aniversário"
        descricao = "Festa de aniversário"
        data = "2023-12-31"
        hora = "18:00"

        query = 'INSERT INTO Eventos (Titulo, Descricao, Data, Hora) VALUES (?, ?, ?, ?)'
        params = (titulo, descricao, data, hora)

        self.calendar.inserir_evento(titulo, descricao, data, hora)
        self.mock_db_connection.executar_operacao.assert_called_once_with(query, params)

    def test_obter_eventos(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Aniversário", "Festa de aniversário", "2023-12-31", "18:00")]

        self.mock_db_connection.cursor.return_value = mock_cursor

        result = self.calendar.obter_eventos()
        query = 'SELECT * FROM Eventos'
        self.mock_db_connection.executar_operacao.assert_called_once_with(query)
        self.assertEqual(result, [("Aniversário", "Festa de aniversário", "2023-12-31", "18:00")])

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock
from calendar import Calendar 

class TestCalendar(unittest.TestCase):
    def setUp(self):
        self.mock_db_connection = MagicMock()
        self.calendar = Calendar(self.mock_db_connection)

    def test_criar_tabela_eventos(self):
        expected_query = '''
        CREATE TABLE IF NOT EXISTS Eventos (
            Id_Evento INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo VARCHAR(100) NOT NULL,
            Descricao TEXT,
            Data DATE NOT NULL,
            Hora TIME NOT NULL
            )
        '''
        self.calendar.criar_tabela_eventos()
        self.mock_db_connection.executar_operacao.assert_called_once_with(expected_query)

    def test_inserir_evento(self):
        titulo = "Aniversário"
        descricao = "Festa de aniversário"
        data = "2023-12-31"
        hora = "18:00"

        expected_query = 'INSERT INTO Eventos (Titulo, Descricao, Data, Hora) VALUES (?, ?, ?, ?)'
        expected_params = (titulo, descricao, data, hora)

        self.calendar.inserir_evento(titulo, descricao, data, hora)
        self.mock_db_connection.executar_operacao.assert_called_once_with(expected_query, expected_params)

    def test_obter_eventos(self):
        expected_query = 'SELECT * FROM Eventos'

        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Aniversário", "Festa de aniversário", "2023-12-31", "18:00")]

        self.mock_db_connection.cursor.return_value = mock_cursor

        result = self.calendar.obter_eventos()
        self.mock_db_connection.executar_operacao.assert_called_once_with(expected_query)
        self.assertEqual(result, [("Aniversário", "Festa de aniversário", "2023-12-31", "18:00")])

if __name__ == '__main__':
    unittest.main()
