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
        self.setStyleSheet("background-color: #242424;color:#eee;")
        self.setContentsMargins(50,0,50,0)

    def addIndexPage(self):
        page = QWidget()
        grid = QGridLayout(page)
        page.setWindowTitle('1 File Password')
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
        grid.addWidget(bNew, 0, 0)
        grid.addWidget(bList, 0, 1)

        self.addWidget(page)

    def addNewPasswordPage(self):

        gridLayoutWidget = QWidget()
        gridLayoutWidget.setGeometry(200, 100, 800, 50)
        gridLayout = QGridLayout(gridLayoutWidget)

        fields = ['website', 'username', 'password', 'extra']
        idx = 1
        for field in fields:
            label = QLabel(gridLayoutWidget)
            label.setText(field.capitalize() + ': ')
            gridLayout.addWidget(label,idx,0,1,1)
            in_field = QLineEdit(gridLayoutWidget)
            in_field.setObjectName(field)
            in_field.setStyleSheet("border:1px solid #ccc;padding:3px;")
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
        gridLayout.setObjectName('password_grid')

        backButton = QPushButton(gridLayoutWidget)
        backButton.setText('Cancel')
        backButton.clicked.connect(self.controller.accessIndexPage)
        gridLayout.addWidget(backButton, 0, 0, 1, 1)

        search = QLineEdit(gridLayoutWidget)
        search.setObjectName('search_input')
        search.setPlaceholderText('Filter term')
        search.setStyleSheet("border:1px solid #ccc;padding:3px;")
        gridLayout.addWidget(search, 0, 2, 1, 1)

        searchButton = QPushButton(gridLayoutWidget)
        searchButton.setText('Filter')
        searchButton.setDefault(True)
        searchButton.clicked.connect(self.controller.filterPasswordList)
        gridLayout.addWidget(searchButton, 0, 3, 1, 1)

        resetButton = QPushButton(gridLayoutWidget)
        resetButton.setText('Reset list')
        resetButton.clicked.connect(self.controller.resetPasswordList)
        gridLayout.addWidget(resetButton, 0, 4, 1, 1)

        self.passList = QTableWidget()
        self.passList.setObjectName('password_list_widget')
        self.passList.setColumnCount(5)
        self.passList.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.passList.setContextMenuPolicy(3)
        self.passList.customContextMenuRequested.connect(self.openCellMenu)
        gridLayout.addWidget(self.passList, 1, 0, 1, 5)

        self.addWidget(gridLayoutWidget)

    def appendPasswords(self, items):
        self.passList.setRowCount(len(items))
        self.passList.setColumnCount(5)
        headers = ['id', 'url', 'username', 'password', 'extra']
        self.passList.setHorizontalHeaderLabels(headers)
        idx = 0
        for item in items:
            self.passList.setItem(idx, 0, QTableWidgetItem(str(item["id"])))
            self.passList.setItem(idx, 1, QTableWidgetItem(str(item["url"])))
            self.passList.setItem(idx, 2, QTableWidgetItem(str(item["username"])))
            self.passList.setItem(idx, 3, QTableWidgetItem(str(item["password"])))
            self.passList.setItem(idx, 4, QTableWidgetItem(str(item["extra"])))
            idx += 1

    def removePasswords(self):
        rows = self.passList.rowCount()
        columns = self.passList.columnCount()

        for row in range(rows):
            self.passList.removeRow(0)
        for column in range(columns):
            self.passList.removeColumn(0)

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
        if item is not None:
            menu = QMenu()
            copy = QAction('copy')
            copy.setData(QVariant(item))
            copy.setObjectName('cell_copy')
            menu.addAction(copy)
            delete = QAction('delete entry')
            entry = tableWidget.item(item.row(), 0)
            delete.setData(QVariant(entry))
            delete.setObjectName('delete_entry')
            menu.addAction(delete)
            menu.triggered.connect(self.controller.cellItemClicked)
            menu.exec_(tableWidget.mapToGlobal(pos))

    def confirmChange(self):
        box = QMessageBox()
        box.setText('Are you sure you want to do this?')
        box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        box.setModal(True)
        box.show()
        box.exec()
        return box.result()

    def toggleTray(self):
        if self.isVisible() == True:
            self.hide()
        else:
            self.show()
