from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, 
)
from PyQt5.QtGui import QFont
from constants import *

class OptionsWindow(QWidget):


    def __init__(self, *args, **kwargs):
        super(OptionsWindow, self).__init__(*args, **kwargs)
        self.setupUI()
    
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
        self.disconnect_btn = QPushButton("Disconnect")

        self.publish_plain_txt_btn.setFont(self.font)
        self.set_preferences_btn.setFont(self.font)
        self.disconnect_btn.setFont(self.font)

        self.btns_layout.addWidget(self.publish_plain_txt_btn)
        self.btns_layout.addWidget(self.set_preferences_btn)
        self.btns_layout.addWidget(self.disconnect_btn)

        self.mainlayout.addLayout(self.btns_layout)

        self.setLayout(self.mainlayout)