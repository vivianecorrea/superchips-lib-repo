from class_DBConn import DBConn

class Calendar: 
    def __init__(self, db_connection: DBConn):
        self.db_connection = db_connection


    def criar_tabela_eventos(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Eventos (
            Id_Evento INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo VARCHAR(100) NOT NULL,
            Descricao TEXT,
            Data DATE NOT NULL,
            Hora TIME NOT NULL
            )
        '''
        return self.db_connection.executar_operacao(query)

    def inserir_evento(titulo, descricao, data, hora):
        query = 'INSERT INTO Eventos (Titulo, Descricao, Data, Hora) VALUES (?, ?, ?, ?)'
        return  self.db_connection.executar_operacao(query, (titulo, descricao, data, hora) )
        
    def obter_eventos(self):
        conn = self.db_connection
        cursor = conn.cursor()
        query = 'SELECT * FROM Eventos'
        self.db_connection.executar_operacao(query)
        eventos = cursor.fetchall()
        conn.close()
        return eventos

