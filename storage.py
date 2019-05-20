from PyQt5 import QtSql
from datetime import datetime
import bcrypt
import scrypt
from base64 import b64encode, b64decode

class Storage():
    def __init__(self, path):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(path)

        if not self.db.open():
            raise Exception('Databasse is not open')

    def getMasterPassword(self):
        password = None
        query = QtSql.QSqlQuery()
        query.prepare('SELECT encrypted FROM main_password')
        query.exec()
        while query.next():
            password = query.value(0)

        return password

    def setMasterPassword(self, password):
        query = QtSql.QSqlQuery()
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query.prepare('INSERT INTO main_password(encrypted, creation_date) VALUES (:pass, :date)')
        query.bindValue(':pass', password.decode('utf-8'))
        query.bindValue(':date', datetime.now().timestamp())
        query.exec()

    def insertPassword(self, values, master_password):
        if (len(values) == 4):
            password = b64encode(scrypt.encrypt(values['password'], master_password, maxtime=0.05)).decode('utf-8')
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO passwords(id, url, username, password, extra) VALUES (NULL, :url, :username, :password, :extra)')
            query.bindValue(':url', values['website'])
            query.bindValue(':username', values['username'])
            query.bindValue(':password', password)
            query.bindValue(':extra', values['extra'])
            query.exec()
        else:
            raise Exception('Number of fields should be 3')

    def listPasswords(self, master_password):
        passwords = []
        query = QtSql.QSqlQuery()
        query.prepare('SELECT * FROM passwords')
        query.exec()
        while query.next():
            password = {}
            password['id'] = query.value('id')
            password['url'] = query.value('url')
            password['username'] = query.value('username')
            if master_password is not None:
                password['password'] = scrypt.decrypt(b64decode(query.value('password')), master_password)
            password['extra'] = query.value('extra')
            passwords.append(password)

        return passwords