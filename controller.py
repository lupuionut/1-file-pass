from PyQt5.QtWidgets import QLineEdit, QMessageBox, QInputDialog

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
                box = QMessageBox(self.window)
                box.setText('Error: {} field is empty.'.format(field))
                box.show()
                box.exec()
                return
        self.promptPassword()
        for field in fields:
            self.window.findChild(QLineEdit, field).setText(None)
        self.accessIndexPage()

    def promptPassword(self):
        alert = QInputDialog()
        alert.setModal(True)
        self.password, _ = alert.getText(self.window,
            'Please insert database password',
            'Your database password')
        alert.show()