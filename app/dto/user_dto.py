from app.connection.conn import conn


class UserDTO:
    """
    Classe responsável pelas operações do banco de dados relacionadas ao usuário
    """
    def __init__(self, nome):
        self.nome = nome

    def insert(self):
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO Usuario(nome) VALUES ({self.nome})
        """)