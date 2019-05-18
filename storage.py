from PyQt5 import QtSql

class Storage():
    def __init__(self, path):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(path)

        if not self.db.open():
            raise Exception('Databasse is not open')

    def getMasterPassword(self):
        query = QtSql.QSqlQuery('SELECT encrypted FROM main_password')
        return query.record().value('encrypted')