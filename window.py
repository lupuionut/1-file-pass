from PyQt5.QtWidgets import \
    QLabel, QWidget, QStackedWidget,\
    QPushButton, QInputDialog, QMessageBox,\
    QGridLayout, QLineEdit, QListWidget
from controller import WindowController

class Window(QStackedWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(1200,600)
        self.setWindowTitle('1 file pass')
        self.setGeometry(130, 130, 1200, 600)
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
        bList.clicked.connect(self.controller.accessListPasswordsPage)
        self.addWidget(page)

    def addNewPasswordPage(self):

        gridLayoutWidget = QWidget()
        gridLayoutWidget.setGeometry(200, 100, 800, 50)
        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(300, 40, 300, 40)

        fields = ['website', 'username', 'password', 'extra']
        idx = 1
        for field in fields:
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
        gridLayoutWidget = QWidget()
        gridLayoutWidget.setGeometry(200, 100, 800, 50)

        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(300, 40, 300, 40)
        gridLayout.setObjectName('password_grid')

        backButton = QPushButton(gridLayoutWidget)
        backButton.setText('Cancel')
        backButton.clicked.connect(self.controller.accessIndexPage)
        gridLayout.addWidget(backButton, 0, 0, 1, 1)

        deleteButton = QPushButton(gridLayoutWidget)
        deleteButton.setText('Delete selected')
        deleteButton.clicked.connect(self.controller.accessIndexPage)
        gridLayout.addWidget(deleteButton, 0, 1, 1, 1)

        search = QLineEdit(gridLayoutWidget)
        search.setObjectName('search_input')
        search.setPlaceholderText('Filter term')
        gridLayout.addWidget(search, 0, 2, 1, 1)

        searchButton = QPushButton(gridLayoutWidget)
        searchButton.setText('Filter')
        searchButton.clicked.connect(self.controller.accessIndexPage)
        gridLayout.addWidget(searchButton, 0, 3, 1, 1)
        
        self.addWidget(gridLayoutWidget)

    def appendPasswords(self):
        gridLayoutWidget = self.findChild(QGridLayout, 'password_grid')
        items = self.controller.listPasswords()
        passList = QListWidget()
        passList.setGeometry(200, 100, 800, 50)
        idx = 0
        for item in items:
            passList.insertItem(idx, str(item["id"]))
            idx += 1
        gridLayoutWidget.addWidget(passList, 1, 0, 1, 4)

    def promptPassword(self):
        alert = QInputDialog()
        alert.setModal(True)
        password, _ = alert.getText(self,
            'Please insert database password',
            'Your database password')
        alert.show()
        return password

    def displayError(self, err):
        box = QMessageBox()
        box.setText(err)
        box.setModal(True)
        box.show()
        box.exec()