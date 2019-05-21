from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from window import Window

app = QApplication([])
app.setWindowIcon(QIcon('./icon.svg'))
window = Window()
window.addIndexPage()
window.addNewPasswordPage()
window.addlistPasswordsPage()
window.show()
app.exec()