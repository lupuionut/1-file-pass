from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from window import Window
import os, sys

app = QApplication([])
app.setWindowIcon(QIcon(os.path.dirname(os.path.abspath(sys.argv[0])) + '/icon.svg'))
window = Window()
window.addIndexPage()
window.addNewPasswordPage()
window.addlistPasswordsPage()
window.show()
app.exec()