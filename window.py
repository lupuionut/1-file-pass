from PyQt5.QtWidgets import QLabel, QWidget, QStackedWidget, QPushButton

class Window(QStackedWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(1200,600)
        self.setWindowTitle('1 file pass')
        self.setGeometry(130, 130, 1200, 600)

    def addIndexPage(self):
        page = QWidget()
        page.setObjectName('page0')
        bNew = QPushButton(page)
        bNew.setObjectName('new_password')
        bNew.setText('Add new password')
        bNew.setGeometry(350,100,200,50)
        bNew.clicked.connect(self.addPage)
        bList = QPushButton(page)
        bList.setObjectName('list_passwords')
        bList.setText('List Passwords')
        bList.setGeometry(650,100,200,50)
        bList.clicked.connect(self.listPage)
        self.addWidget(page)

    def addNewPasswordPage(self):
        page = QWidget()
        page.setObjectName('page1')
        label = QLabel(page)
        label.setText('Add new password page')
        label.setGeometry(500,100,100,100)
        self.addWidget(page)

    def addlistPasswordsPage(self):
        page = QWidget()
        page.setObjectName('page2')
        label = QLabel(page)
        label.setText('List passwords page')
        label.setGeometry(500,100,100,100)
        self.addWidget(page)

    def indexPage(self):
        self.setCurrentIndex(0)

    def addPage(self):
        self.setCurrentIndex(1)

    def listPage(self):
        self.setCurrentIndex(2)