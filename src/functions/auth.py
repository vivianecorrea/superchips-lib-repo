def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='vivi',
        password='12345',
        database='pets'
    )