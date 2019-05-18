from PyQt5.QtWidgets import QLineEdit

class WindowController():
    def __init__(self, window):
        self.window = window
        self.password = None

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
        self.askPassword()
        for field in fields:
            self.window.findChild(QLineEdit, field).setText(None)
        self.accessIndexPage()

    def askPassword(self):
        password = self.window.promptPassword()