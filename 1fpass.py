from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from window import Window
import os, sys

icon = QIcon(os.path.dirname(os.path.abspath(sys.argv[0])) + '/icon.svg')
app = QApplication([])
app.setWindowIcon(icon)

#set system tray icon
sysicon = QSystemTrayIcon(icon)
sysicon.setIcon(icon)
sysicon.show()


window = Window()
window.addIndexPage()
window.addNewPasswordPage()
window.addlistPasswordsPage()
window.show()
sysicon.activated.connect(window.toggleTray)

app.exec()