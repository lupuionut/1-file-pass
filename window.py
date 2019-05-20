from PyQt5.QtWidgets import \
    QLabel, QWidget, QStackedWidget,\
    QPushButton, QInputDialog, QMessageBox,\
    QGridLayout, QLineEdit, QTableWidget,\
    QTableWidgetItem, QHeaderView, QMenu, QAction
from PyQt5.QtCore import QVariant
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
        gridLayoutWidget.setGeometry(100, 100, 1000, 50)

        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(100, 40, 100, 40)
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
        items = self.controller.listPasswords()
        columns = len(items)
        gridLayoutWidget = self.findChild(QGridLayout, 'password_grid')
        passList = QTableWidget(columns, 5)
        passList.setObjectName('password_list_widget')
        tHeader = passList.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        headers = ['id', 'url', 'username', 'password', 'extra']
        idx = 0
        for header in headers:
            itemWidget = QTableWidgetItem(header)
            passList.setHorizontalHeaderItem(idx, QTableWidgetItem(header))
            idx += 1
        idx = 0
        for item in items:
            passList.setItem(idx, 0, QTableWidgetItem(str(item["id"])))
            passList.setItem(idx, 1, QTableWidgetItem(str(item["url"])))
            passList.setItem(idx, 2, QTableWidgetItem(str(item["username"])))
            passList.setItem(idx, 3, QTableWidgetItem(str(item["password"])))
            passList.setItem(idx, 4, QTableWidgetItem(str(item["extra"])))
            idx += 1
        passList.setContextMenuPolicy(3)
        passList.customContextMenuRequested.connect(self.openCellMenu)
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

    def openCellMenu(self, pos):
        tableWidget = self.findChild(QTableWidget, 'password_list_widget')
        item = tableWidget.itemAt(pos)
        menu = QMenu()
        copy = QAction('copy')
        copy.setData(QVariant(item))
        copy.setObjectName('cell_copy')
        menu.addAction(copy)
        menu.triggered.connect(self.controller.cellItemClicked)
        menu.exec_(tableWidget.mapToGlobal(pos))