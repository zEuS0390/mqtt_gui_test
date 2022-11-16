from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QPushButton, QLabel,
    QGridLayout, QLineEdit,
    QDesktopWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
from constants import *

class ChangeIntervalWindow(QWidget):

    pressedBackspace = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ChangeIntervalWindow, self).__init__(*args, **kwargs)
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
        self.detection_interval_label = QLabel("Change Interval (s):")
        self.detection_interval_input = QLineEdit()
        self.detection_interval_input.setPlaceholderText("(in seconds)")
        self.detection_interval_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.publish_interval_btn = QPushButton("Publish")
        self.back_btn = QPushButton("Back")

        self.detection_interval_input.setFont(self.font)
        self.detection_interval_label.setFont(self.font)
        self.publish_interval_btn.setFont(self.font)
        self.back_btn.setFont(self.font)

        self.inputs_layout.addWidget(self.detection_interval_label, 0, 0)
        self.inputs_layout.addWidget(self.detection_interval_input, 0, 1)

        self.mainlayout.addLayout(self.inputs_layout)
        self.mainlayout.addWidget(self.publish_interval_btn)
        self.mainlayout.addWidget(self.back_btn)

        self.setLayout(self.mainlayout)
    
    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2)

    def keyPressEvent(self,event):
        if event.key() == Qt.Key.Key_Backspace:
            self.pressedBackspace.emit()