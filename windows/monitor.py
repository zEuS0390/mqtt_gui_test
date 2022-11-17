from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QDesktopWidget, QHBoxLayout,
    QLabel, QPushButton
)
from PyQt5.QtGui import QFont, QPixmap, QColor
from PyQt5.QtCore import Qt, pyqtSignal
from constants import *

class MonitorWindow(QWidget):

    pressedBackspace = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MonitorWindow, self).__init__(*args, **kwargs)
        self.setupUI()
        self.center()
    
    def setupUI(self):
        self.setWindowTitle(WINDOW_TITLE)

        self.font = QFont()
        self.font.setPointSize(18)
        self.font.setFamily("Roboto Mono")
        
        self.mainlayout  = QVBoxLayout()
        self.headerlayout = QHBoxLayout()
        self.viewslayout = QHBoxLayout()

        # Create widgets
        self.back_btn = QPushButton("Back")
        self.stop_btn = QPushButton("Stop Camera")
        self.start_btn = QPushButton("Start Camera")

        self.back_btn.setFont(self.font)
        self.stop_btn.setFont(self.font)
        self.start_btn.setFont(self.font)

        self.image1 = QLabel()
        self.image2 = QLabel()
        self.view1 = QPixmap(640, 480)
        self.view2 = QPixmap(640, 480)
        self.view1.fill(QColor('darkGray'))
        self.view2.fill(QColor('darkGray'))
        self.image1.setPixmap(self.view1)
        self.image2.setPixmap(self.view2)

        self.image1.setFont(self.font)
        self.image2.setFont(self.font)

        self.headerlayout.addWidget(self.back_btn)
        self.headerlayout.addStretch()
        self.headerlayout.addWidget(self.start_btn)
        self.headerlayout.addWidget(self.stop_btn)

        self.viewslayout.addWidget(self.image1)
        self.viewslayout.addWidget(self.image2)
        self.viewslayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainlayout.addLayout(self.headerlayout)
        self.mainlayout.addLayout(self.viewslayout)

        self.setLayout(self.mainlayout)
    
    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2)

    def keyPressEvent(self,event):
        if event.key() == Qt.Key.Key_Backspace:
            self.pressedBackspace.emit()