import sqlite3
import os

class Storage():
    def __init__(self):
        self.file = 'pass.db'

    def connect(self):
        if os.path.isfile(self.file):
            self.db = sqlite3.connect(self.file)
        else:
            self.db = None
        return self

    def close(self):
        if self.db is not None:
            self.db.close()

    def getPassword(self):
        query = 'SELECT encrypted, creation_date FROM main_password'
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute(query)
            (password, _) = cursor.fetchone()
        except Exception as e:
            password = None
            print(str(e))
        finally:
            self.close()
        return password