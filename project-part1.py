import sqlite3
from sqlite3 import Error
import logging as log

#mamy listę nowych pacjentów i chcemy dodać ich do bazy

class Database:

    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_name)
        except ConnectionError as e:
            log.error(f"Connection error {e}")
        except Exception as e:
            log.error(f"Unknown error: {e}")
        return self.conn

    def execute_sql(self, sql, params=None):
        if params is None:
            params = []
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                self.conn.commit()
            except Exception as e:
                log.error(f"Database error: {e}")

    def close_conn(self):
        self.conn.close()



if __name__ == '__main__':
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS patients (
        id integer PRIMARY KEY,
        name text NOT NULL,
        surname text NOT NULL,
        pesel integer NOT NULL); """
    db = Database(r"C:\Users\cp24\Desktop\Akademia Kodu\W1_pliki\patients.db")
    db.execute_sql(sql_create_table)
    print("done")
    #na tym etapie powinniśmy mieć stworzoną tabelę w sql

    sql_insert = """
        INSERT INTO patients
        (id, name, surname, pesel)
              VALUES(?,?,?,?)
    """
    with open(r"C:\Users\cp24\Desktop\Akademia Kodu\W1_pliki\project-data.txt", "r", encoding='UTF8') as file:
        for line in file.readlines():
            patient_data = line.strip().split(sep=',')
            #print(patient_data)
            db.execute_sql(sql_insert, patient_data)

    db.close_conn()
    #na tym etapie powinniśmy już wiedzieć
    # 1. jak połączyć się do bazy danych
    # 2. Jak używać wyjątków
    # 3. Jak otworzyć plik z danymi pacjentów