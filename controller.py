from PyQt5.QtWidgets import QLineEdit
from PyQt5.Qt import QClipboard, QApplication
import bcrypt
import storage

class WindowController():
    def __init__(self, window):
        self.window = window
        self.password = None
        self.authorized = False
        self.storage = storage.Storage('pass.db')

    def accessIndexPage(self):
        self.window.setCurrentIndex(0)

    def accessNewPasswordPage(self):
        self.window.setCurrentIndex(1)

    def accessListPasswordsPage(self):
        if self.authorized == False:
            self.password = self.askPassword()
            try:
                self.isPasswordOk()
            except NoPasswordSetException as ex:
                self.storage.setMasterPassword(self.password)
                return
            except Exception as e:
                self.window.displayError(str(e))
                return
        items = self.listPasswords()
        self.window.appendPasswords(items)
        self.window.setCurrentIndex(2)

    def saveNewPassword(self):
        fields = {'website': {'value':'', 'required': True},
                'username': {'value': '', 'required': True},
                'password': {'value': '', 'required': True},
                'extra': {'value': '', 'required': False}}
        values = {}
        for (field, req) in fields.items():
            val = self.window.findChild(QLineEdit, field).text()
            if len(val) == 0 and req["required"]:
                self.window.displayError('Error: {} is empty.'.format(field))
                return
            else:
                values[field] = val
        self.password = self.askPassword()

        try:
            self.isPasswordOk()
            self.storage.insertPassword(values, self.password)
        except NoPasswordSetException as ex:
            self.storage.setMasterPassword(self.password)
            return
        except Exception as e:
            self.window.displayError(str(e))
            return

        for field in fields:
            self.window.findChild(QLineEdit, field).setText(None)
        self.accessIndexPage()

    def askPassword(self):
        return self.window.promptPassword()

    def isPasswordOk(self):
        if self.password is None or len(self.password) == 0:
            raise Exception('You did not provide a password.')

        stored_password = self.storage.getMasterPassword()

        if stored_password is not None and len(stored_password) > 0:
            if bcrypt.checkpw(self.password.encode('utf-8'), stored_password.encode('utf-8')) is False:
                raise Exception('Provided password does not match.')
        else:
            raise NoPasswordSetException('Your database does not contain a master password.')

        self.authorized = True
        return True

    def listPasswords(self):
        return self.storage.listPasswords(self.password)

    def cellItemClicked(self, action):
        item = action.data()
        if action.objectName() == 'cell_copy':
            clipboard = QApplication.clipboard()
            clipboard.setText(item.text(), QClipboard.Clipboard)
        elif action.objectName() == 'delete_entry':
            response = self.window.confirmChange()
            if (response == 1024):
                id = int(item.text())
                self.storage.deletePassword(id)
                item.tableWidget().removeRow(item.row())

class NoPasswordSetException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)