from PyQt5.QtWidgets import \
    QLabel, QWidget, QStackedWidget,\
    QPushButton, QInputDialog, QMessageBox,\
    QGridLayout, QLineEdit
import os
import bcrypt
import storage
from controller import WindowController

class Window(QStackedWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(1200,600)
        self.setWindowTitle('1 file pass')
        self.setGeometry(130, 130, 1200, 600)
        self.storage = storage.Storage()
        self.controller = WindowController(self)

    def addIndexPage(self):
        page = QWidget()
        page.setObjectName('page0')
        bNew = QPushButton(page)
        bNew.setObjectName('new_password')
        bNew.setText('Add new password')
        bNew.setGeometry(350,100,200,50)
        bNew.clicked.connect(self.controller.accessNewPasswordPage)
        bList = QPushButton(page)
        bList.setObjectName('list_passwords')
        bList.setText('List Passwords')
        bList.setGeometry(650,100,200,50)
        bList.clicked.connect(self.listPage)
        self.addWidget(page)

    def addNewPasswordPage(self):

        gridLayoutWidget = QWidget()
        gridLayoutWidget.setGeometry(200, 100, 800, 50)
        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(300, 40, 300, 40)

        fields = {'website':'', 'username':'', 'password':''}
        idx = 1
        for (field, _) in fields.items():
            label = QLabel(gridLayoutWidget)
            label.setText(field.capitalize() + ': ')
            gridLayout.addWidget(label,idx,0,1,1)
            in_field = QLineEdit(gridLayoutWidget)
            in_field.setObjectName(field)
            gridLayout.addWidget(in_field,idx,1,1,1)
            idx += 1

        backButton = QPushButton(gridLayoutWidget)
        backButton.setText('Cancel')
        backButton.clicked.connect(self.controller.accessIndexPage)
        gridLayout.addWidget(backButton, idx, 0, 1, 1)

        saveButton = QPushButton(gridLayoutWidget)
        saveButton.setText('Save')
        saveButton.clicked.connect(self.controller.saveNewPassword)
        gridLayout.addWidget(saveButton, idx, 1, 1, 1)
        self.addWidget(gridLayoutWidget)

    def addlistPasswordsPage(self):
        page = QWidget()
        page.setObjectName('page2')
        label = QLabel(page)
        label.setText('List passwords page')
        label.setGeometry(500,100,100,100)
        self.addWidget(page)

    def listPage(self):
        try:
            self.isPasswordOk()
            self.setCurrentIndex(2)
        except Exception as e:
            alert = QMessageBox()
            alert.setText(str(e))
            alert.show()
            alert.exec()
            self.setCurrentIndex(0)

    def isPasswordOk(self):
        if self.password is None:
            raise Exception('You did not provide a password')

        stored_password = self.storage.getPassword()
        if stored_password is not None:
            if bcrypt.checkpw(password, stored_password) is False:
                raise Exception('Your master password is not ok')
        else:
            raise Exception('Your database does not contain a master password')

        return True