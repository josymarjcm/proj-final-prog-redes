import sqlite3
import datetime

class BancoDeDados():
    """
    Faz a conexão com o banco de dados.
    """
    def __init__(self):
        self.conn = sqlite3.connect("banco.db", check_same_thread = False)

    """
    Adiciona os dados de humidade na tabela Humidade juntamente com o horário.
    """
    def inserir_humidade(self, valor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Humidade (horario, valor) VALUES (?, ?)",
                (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), valor))

        self.conn.commit()
        return 200

    """
    Adiciona os dados de temperatura na tabela Temperatura juntamente com o horário.
    """
    def inserir_temperatura(self, valor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Temperatura (horario, valor) VALUES (?, ?)",
                (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), valor))

        self.conn.commit()
        return 200

    """
    Adiciona os dados de gás na tabela Gas juntamente com o horário.
    """
    def inserir_gas(self, valor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Gas (horario, valor) VALUES (?, ?)",
                (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), valor))

        self.conn.commit()
        return 200

    """
    Seleciona os dados baseado nos critérios definidos pelo usuário.
    Opções: apenas a humidade, apenas a temperatura, apenas o gás ou todas as anteriores.
    """
    def selecionar_dados(self, humidade, temperatura, gas, de, ate):
        cursor = self.conn.cursor()

        if humidade and not temperatura and not gas:
            cursor.execute("SELECT * FROM Humidade WHERE horario BETWEEN ? AND ?", (de, ate))
        elif not humidade and temperatura and not gas:
            cursor.execute("SELECT * FROM Temperatura WHERE horario BETWEEN ? AND ?", (de, ate))
        elif not humidade and not temperatura and gas:
            cursor.execute("SELECT * FROM Gas WHERE horario BETWEEN ? AND ?", (de, ate))
        elif humidade and temperatura and gas:
            dados = []
            c = cursor.execute("SELECT * FROM Humidade WHERE horario BETWEEN ? AND ?", (de, ate)).fetchall()
            if c:
                dados.append(c)
            c = cursor.execute("SELECT * FROM Temperatura WHERE horario BETWEEN ? AND ?", (de, ate)).fetchall()
            if c:
                dados.append(c)
            c = cursor.execute("SELECT * FROM Gas WHERE horario BETWEEN ? AND ?", (de, ate)).fetchall()
            if c:
                dados.append(c)

            return dados, True

        return cursor.fetchall(), False
