from PySide2.QtWidgets import QApplication
from GUI.mainWindow import MainWindow
from Controllers.MainWindowController import MainWindowController
import sys


def main():
    app = QApplication(sys.argv)
    m = MainWindow()
    MainWindowController(m)
    m.show()
    sys.exit(app.exec_())

main()
