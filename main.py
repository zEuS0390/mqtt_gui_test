
from PyQt5.QtWidgets import (
    QApplication
)
from windows.app import MainApplication
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainapp = MainApplication()
    sys.exit(app.exec())