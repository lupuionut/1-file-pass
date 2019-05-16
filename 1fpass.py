from PyQt5.QtWidgets import QApplication
from window import Window

app = QApplication([])
window = Window()
window.addIndexPage()
window.addNewPasswordPage()
window.addlistPasswordsPage()
window.show()
app.exec()





































