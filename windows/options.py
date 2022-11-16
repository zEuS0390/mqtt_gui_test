from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, 
    QDesktopWidget
)
from PyQt5.QtGui import QFont
from constants import *

class OptionsWindow(QWidget):


    def __init__(self, *args, **kwargs):
        super(OptionsWindow, self).__init__(*args, **kwargs)
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
        self.btns_layout = QVBoxLayout()

        # Create widgets
        self.publish_plain_txt_btn = QPushButton("Publish Plain Text")
        self.set_preferences_btn = QPushButton("Set Preferences")
        self.changee_interval_btn = QPushButton("Change Interval")
        self.disconnect_btn = QPushButton("Disconnect")

        self.publish_plain_txt_btn.setFont(self.font)
        self.set_preferences_btn.setFont(self.font)
        self.changee_interval_btn.setFont(self.font)
        self.disconnect_btn.setFont(self.font)

        self.btns_layout.addWidget(self.publish_plain_txt_btn)
        self.btns_layout.addWidget(self.set_preferences_btn)
        self.btns_layout.addWidget(self.changee_interval_btn)
        self.btns_layout.addWidget(self.disconnect_btn)

        self.mainlayout.addLayout(self.btns_layout)

        self.setLayout(self.mainlayout)

    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2)