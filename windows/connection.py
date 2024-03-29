from PyQt5.QtWidgets import (
    QWidget, QGridLayout, 
    QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QDesktopWidget,
    QCompleter
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt
from constants import *

class ConnectionWindow(QWidget):

    pressedEscape = pyqtSignal()
    pressedEnter = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ConnectionWindow, self).__init__(*args, **kwargs)
        self.setupUI()
        self.center()
    
    def setupUI(self):
        self.setWindowTitle(WINDOW_TITLE)

        self.font = QFont()
        self.font.setPointSize(18)
        self.font.setFamily("Roboto Mono")
        
        self.mainlayout  = QVBoxLayout()
        self.inputs_layout = QGridLayout()

        # Create widgets
        self.ip_address_label = QLabel("IP Address:")
        self.ip_address_input = QLineEdit()
        self.topic_label = QLabel("Topic:")
        self.topic_input = QLineEdit()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.connect_btn = QPushButton("CONNECT")

        self.ip_address_label.setFont(self.font)
        self.topic_label.setFont(self.font)
        self.username_label.setFont(self.font)
        self.password_label.setFont(self.font)
        self.ip_address_input.setFont(self.font)
        self.topic_input.setFont(self.font)
        self.username_input.setFont(self.font)
        self.password_input.setFont(self.font)
        self.connect_btn.setFont(self.font)

        self.inputs_layout.addWidget(self.ip_address_label, 0, 0)
        self.inputs_layout.addWidget(self.ip_address_input, 0, 1)
        self.inputs_layout.addWidget(self.topic_label, 1, 0)
        self.inputs_layout.addWidget(self.topic_input, 1, 1)
        self.inputs_layout.addWidget(self.username_label, 2, 0)
        self.inputs_layout.addWidget(self.username_input, 2, 1)
        self.inputs_layout.addWidget(self.password_label, 3, 0)
        self.inputs_layout.addWidget(self.password_input, 3, 1)

        self.mainlayout.addLayout(self.inputs_layout)
        self.mainlayout.addWidget(self.connect_btn)

        self.setLayout(self.mainlayout)

        ip_address_completer = QCompleter([
            "localhost"
        ])
        ip_address_completer.popup().setFont(self.font)
        self.ip_address_input.setCompleter(ip_address_completer)

    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2) 

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.pressedEnter.emit()
        elif event.key() == Qt.Key.Key_Escape:
            self.pressedEscape.emit()