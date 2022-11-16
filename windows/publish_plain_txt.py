from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, 
    QPlainTextEdit, QPushButton,
    QDesktopWidget
)
from PyQt5.QtGui import QFont
from constants import *

class PublishPlainTXTWindow(QWidget):


    def __init__(self, *args, **kwargs):
        super(PublishPlainTXTWindow, self).__init__(*args, **kwargs)
        self.setupUI()
        self.center()
    
    def setupUI(self):
        self.setWindowTitle(WINDOW_TITLE)
        # self.resize(*WINDOW_SIZE)

        self.font = QFont()
        self.font.setPointSize(18)
        self.font.setFamily("Roboto Mono")

        self.font = QFont()
        self.font.setPointSize(18)
        self.font.setFamily("Roboto Mono")
        
        self.mainlayout  = QVBoxLayout()
        self.inputs_layout = QVBoxLayout()

        # Create widgets
        self.plaintext_input = QPlainTextEdit()
        self.publish_btn = QPushButton("Publish")
        self.back_btn = QPushButton("Back")

        self.plaintext_input.setFont(self.font)
        self.publish_btn.setFont(self.font)
        self.back_btn.setFont(self.font)

        self.inputs_layout.addWidget(self.plaintext_input)
        self.inputs_layout.addWidget(self.publish_btn)
        self.inputs_layout.addWidget(self.back_btn)

        self.mainlayout.addLayout(self.inputs_layout)

        self.setLayout(self.mainlayout)

    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2)