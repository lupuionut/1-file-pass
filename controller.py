from PyQt5.QtWidgets import QLineEdit
import bcrypt
import storage

class WindowController():
    def __init__(self, window):
        self.window = window
        self.password = None
        self.storage = storage.Storage('pass.db')

    def accessIndexPage(self):
        self.window.setCurrentIndex(0)

    def accessNewPasswordPage(self):
        self.window.setCurrentIndex(1)

    def accessListPasswordsPage(self):
        self.window.setCurrentIndex(2)

    def saveNewPassword(self):
        fields = ['website', 'username', 'password']
        for field in fields:
            val = self.window.findChild(QLineEdit, field).text()
            if len(val) == 0:
                self.window.displayError('Error: {} field is empty.'.format(field))
                return
        self.password = self.askPassword()

        try:
            self.isPasswordOk()
        except Exception as e:
            self.window.displayError(str(e))
            return

        for field in fields:
            self.window.findChild(QLineEdit, field).setText(None)
        self.accessIndexPage()

    def askPassword(self):
        password = self.window.promptPassword()

    def isPasswordOk(self):
        if self.password is None or len(self.password) == 0:
            raise Exception('You did not provide a password')

        stored_password = self.storage.getMasterPassword()

        if stored_password is not None:
            if bcrypt.checkpw(self.password, stored_password) is False:
                raise Exception('Your master password is not ok')
        else:
            raise Exception('Your database does not contain a master password')
        return True