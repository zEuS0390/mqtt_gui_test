from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, 
    QGridLayout, QLabel,
    QDesktopWidget, QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from constants import *

class SetPreferencesWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(SetPreferencesWindow, self).__init__(*args, **kwargs)
        self.setupUI()
        self.ppe_preferences = {
            "helmet": True,
            "no_helmet": True,
            "glasses": True,
            "no_glasses": True,
            "vest": True,
            "no_vest": True,
            "gloves": True,
            "no_gloves": True,
            "boots": True,
            "no_boots": True,
            "person": True
        }
        self.update()
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
        self.options_layout = QGridLayout()

        self.helmet_btns_layout = QGridLayout()
        self.glasses_btns_layout = QGridLayout()
        self.vest_btns_layout = QGridLayout()
        self.gloves_btns_layout = QGridLayout()
        self.boots_btns_layout = QGridLayout()

        # Create widgets
        # Preference Option Labels
        self.helmet_label = QLabel("Helmet:")
        self.glasses_label = QLabel("Glasses:")
        self.vest_label = QLabel("Vest:")
        self.gloves_label = QLabel("Gloves:")
        self.boots_label = QLabel("Boots:")

        self.helmet_label.setFont(self.font)
        self.glasses_label.setFont(self.font)
        self.vest_label.setFont(self.font)
        self.gloves_label.setFont(self.font)
        self.boots_label.setFont(self.font)

        # Helmet Buttons
        self.enable_helmet_btn = QPushButton("YES")
        self.disable_all_helmet_btn = QPushButton("None")
        self.enable_no_helmet_btn = QPushButton("NO")

        # Glasses Buttons
        self.enable_glasses_btn = QPushButton("YES")
        self.disable_all_glasses_btn = QPushButton("None")
        self.enable_no_glasses_btn = QPushButton("NO")

        # Vest Buttons
        self.enable_vest_btn = QPushButton("YES")
        self.disable_all_vest_btn = QPushButton("None")
        self.enable_no_vest_btn = QPushButton("NO")

        # Gloves Buttons
        self.enable_gloves_btn = QPushButton("YES")
        self.disable_all_gloves_btn = QPushButton("None")
        self.enable_no_gloves_btn = QPushButton("NO")

        # Boots Buttons
        self.enable_boots_btn = QPushButton("YES")
        self.disable_all_boots_btn = QPushButton("None")
        self.enable_no_boots_btn = QPushButton("NO")

        self.enable_helmet_btn.setFont(self.font)
        self.disable_all_helmet_btn.setFont(self.font)
        self.enable_no_helmet_btn.setFont(self.font)

        self.enable_glasses_btn.setFont(self.font)
        self.disable_all_glasses_btn.setFont(self.font)
        self.enable_no_glasses_btn.setFont(self.font)

        self.enable_vest_btn.setFont(self.font)
        self.disable_all_vest_btn.setFont(self.font)
        self.enable_no_vest_btn.setFont(self.font)

        self.enable_gloves_btn.setFont(self.font)
        self.disable_all_gloves_btn.setFont(self.font)
        self.enable_no_gloves_btn.setFont(self.font)

        self.enable_boots_btn.setFont(self.font)
        self.disable_all_boots_btn.setFont(self.font)
        self.enable_no_boots_btn.setFont(self.font)

        self.publish_preference_btn = QPushButton("Publish")
        self.back_btn = QPushButton("Back")
        self.publish_preference_btn.setFont(self.font)
        self.back_btn.setFont(self.font)

        # Helmet Options Layout
        self.helmet_btns_layout.addWidget(self.enable_helmet_btn, 0, 0)
        self.helmet_btns_layout.addWidget(self.disable_all_helmet_btn, 0, 1)
        self.helmet_btns_layout.addWidget(self.enable_no_helmet_btn, 0, 2)

        # Glasses Options Layout
        self.glasses_btns_layout.addWidget(self.enable_glasses_btn, 1, 0)
        self.glasses_btns_layout.addWidget(self.disable_all_glasses_btn, 1, 1)
        self.glasses_btns_layout.addWidget(self.enable_no_glasses_btn, 1, 2)

        # Vest Options Layout
        self.vest_btns_layout.addWidget(self.enable_vest_btn, 2, 0)
        self.vest_btns_layout.addWidget(self.disable_all_vest_btn, 2, 1)
        self.vest_btns_layout.addWidget(self.enable_no_vest_btn, 2, 2)

        # Gloves Options Layout
        self.gloves_btns_layout.addWidget(self.enable_gloves_btn, 3, 0)
        self.gloves_btns_layout.addWidget(self.disable_all_gloves_btn, 3, 1)
        self.gloves_btns_layout.addWidget(self.enable_no_gloves_btn, 3, 2)

        # Boots Options Layout
        self.boots_btns_layout.addWidget(self.enable_boots_btn, 4, 0)
        self.boots_btns_layout.addWidget(self.disable_all_boots_btn, 4, 1)
        self.boots_btns_layout.addWidget(self.enable_no_boots_btn, 4, 2)

        self.options_layout.addWidget(self.helmet_label, 0, 0)
        self.options_layout.addLayout(self.helmet_btns_layout, 0, 1)
        
        self.options_layout.addWidget(self.glasses_label, 1, 0)
        self.options_layout.addLayout(self.glasses_btns_layout, 1, 1)

        self.options_layout.addWidget(self.vest_label, 2, 0)
        self.options_layout.addLayout(self.vest_btns_layout, 2, 1)

        self.options_layout.addWidget(self.gloves_label, 3, 0)
        self.options_layout.addLayout(self.gloves_btns_layout, 3, 1)

        self.options_layout.addWidget(self.boots_label, 4, 0)
        self.options_layout.addLayout(self.boots_btns_layout, 4, 1)

        self.helmet_btns_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.glasses_btns_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vest_btns_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gloves_btns_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boots_btns_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainlayout.addLayout(self.options_layout)
        self.mainlayout.addWidget(self.publish_preference_btn)
        self.mainlayout.addWidget(self.back_btn)

        self.setLayout(self.mainlayout)

        self.enable_helmet_btn.clicked.connect(self.enableHelmet)
        self.disable_all_helmet_btn.clicked.connect(self.disableAllHelmet)
        self.enable_no_helmet_btn.clicked.connect(self.enableNoHelmet)

        self.enable_glasses_btn.clicked.connect(self.enableGlasses)
        self.disable_all_glasses_btn.clicked.connect(self.disableAllGlasses)
        self.enable_no_glasses_btn.clicked.connect(self.enableNoGlasses)

        self.enable_vest_btn.clicked.connect(self.enableVest)
        self.disable_all_vest_btn.clicked.connect(self.disableAllVest)
        self.enable_no_vest_btn.clicked.connect(self.enableNoVest)

        self.enable_gloves_btn.clicked.connect(self.enableGloves)
        self.disable_all_gloves_btn.clicked.connect(self.disableAllGloves)
        self.enable_no_gloves_btn.clicked.connect(self.enableNoGloves)

        self.enable_boots_btn.clicked.connect(self.enableBoots)
        self.disable_all_boots_btn.clicked.connect(self.disableAllBoots)
        self.enable_no_boots_btn.clicked.connect(self.enableNoBoots)



    def enableHelmet(self):
        self.ppe_preferences["helmet"] = True
        self.ppe_preferences["no_helmet"] = False
        self.enable_helmet_btn.setStyleSheet("background-color: green;")
        self.disable_all_helmet_btn.setStyleSheet("background-color: none;")
        self.enable_no_helmet_btn.setStyleSheet("background-color: none;")

    def disableAllHelmet(self):
        self.ppe_preferences["helmet"] = False
        self.ppe_preferences["no_helmet"] = False
        self.enable_helmet_btn.setStyleSheet("background-color: none;")
        self.disable_all_helmet_btn.setStyleSheet("background-color: green;")
        self.enable_no_helmet_btn.setStyleSheet("background-color: none;")

    def enableNoHelmet(self):
        self.ppe_preferences["helmet"] = False
        self.ppe_preferences["no_helmet"] = True
        self.enable_helmet_btn.setStyleSheet("background-color: none;")
        self.disable_all_helmet_btn.setStyleSheet("background-color: none;")
        self.enable_no_helmet_btn.setStyleSheet("background-color: green;")

    def enableGlasses(self):
        self.ppe_preferences["glasses"] = True
        self.ppe_preferences["no_glasses"] = False
        self.enable_glasses_btn.setStyleSheet("background-color: green;")
        self.disable_all_glasses_btn.setStyleSheet("background-color: none;")
        self.enable_no_glasses_btn.setStyleSheet("background-color: none;")

    def disableAllGlasses(self):
        self.ppe_preferences["glasses"] = False
        self.ppe_preferences["no_glasses"] = False
        self.enable_glasses_btn.setStyleSheet("background-color: none;")
        self.disable_all_glasses_btn.setStyleSheet("background-color: green;")
        self.enable_no_glasses_btn.setStyleSheet("background-color: none;")

    def enableNoGlasses(self):
        self.ppe_preferences["glasses"] = False
        self.ppe_preferences["no_glasses"] = True
        self.enable_glasses_btn.setStyleSheet("background-color: none;")
        self.disable_all_glasses_btn.setStyleSheet("background-color: none;")
        self.enable_no_glasses_btn.setStyleSheet("background-color: green;")

    def enableVest(self):
        self.ppe_preferences["vest"] = True
        self.ppe_preferences["no_vest"] = False
        self.enable_vest_btn.setStyleSheet("background-color: green;")
        self.disable_all_vest_btn.setStyleSheet("background-color: none;")
        self.enable_no_vest_btn.setStyleSheet("background-color: none;")

    def disableAllVest(self):
        self.ppe_preferences["vest"] = False
        self.ppe_preferences["no_vest"] = False
        self.enable_vest_btn.setStyleSheet("background-color: none;")
        self.disable_all_vest_btn.setStyleSheet("background-color: green;")
        self.enable_no_vest_btn.setStyleSheet("background-color: none;")

    def enableNoVest(self):
        self.ppe_preferences["vest"] = False
        self.ppe_preferences["no_vest"] = True
        self.enable_vest_btn.setStyleSheet("background-color: none;")
        self.disable_all_vest_btn.setStyleSheet("background-color: none;")
        self.enable_no_vest_btn.setStyleSheet("background-color: green;")
    
    def enableGloves(self):
        self.ppe_preferences["gloves"] = True
        self.ppe_preferences["no_gloves"] = False
        self.enable_gloves_btn.setStyleSheet("background-color: green;")
        self.disable_all_gloves_btn.setStyleSheet("background-color: none;")
        self.enable_no_gloves_btn.setStyleSheet("background-color: none;")

    def disableAllGloves(self):
        self.ppe_preferences["gloves"] = False
        self.ppe_preferences["no_gloves"] = False
        self.enable_gloves_btn.setStyleSheet("background-color: none;")
        self.disable_all_gloves_btn.setStyleSheet("background-color: green;")
        self.enable_no_gloves_btn.setStyleSheet("background-color: none;")

    def enableNoGloves(self):
        self.ppe_preferences["gloves"] = False
        self.ppe_preferences["no_gloves"] = True
        self.enable_gloves_btn.setStyleSheet("background-color: none;")
        self.disable_all_gloves_btn.setStyleSheet("background-color: none;")
        self.enable_no_gloves_btn.setStyleSheet("background-color: green;")

    def enableBoots(self):
        self.ppe_preferences["boots"] = True
        self.ppe_preferences["no_boots"] = False
        self.enable_boots_btn.setStyleSheet("background-color: green;")
        self.disable_all_boots_btn.setStyleSheet("background-color: none;")
        self.enable_no_boots_btn.setStyleSheet("background-color: none;")

    def disableAllBoots(self):
        self.ppe_preferences["boots"] = False
        self.ppe_preferences["no_boots"] = False
        self.enable_boots_btn.setStyleSheet("background-color: none;")
        self.disable_all_boots_btn.setStyleSheet("background-color: green;")
        self.enable_no_boots_btn.setStyleSheet("background-color: none;")

    def enableNoBoots(self):
        self.ppe_preferences["boots"] = False
        self.ppe_preferences["no_boots"] = True
        self.enable_boots_btn.setStyleSheet("background-color: none;")
        self.disable_all_boots_btn.setStyleSheet("background-color: none;")
        self.enable_no_boots_btn.setStyleSheet("background-color: green;")

    def checkState(self, ppe_key_1: str, ppe_key_2: str, btn_1: QPushButton, btn_2: QPushButton, btn_3: QPushButton):
        if self.ppe_preferences[ppe_key_1] == True and self.ppe_preferences[ppe_key_2] == True:
            btn_1.setStyleSheet("background-color: green;")
            btn_2.setStyleSheet("background-color: none;")
            btn_3.setStyleSheet("background-color: none;")
        elif self.ppe_preferences[ppe_key_1] == False and self.ppe_preferences[ppe_key_2] == True:
            btn_1.setStyleSheet("background-color: none;")
            btn_2.setStyleSheet("background-color: none;")
            btn_3.setStyleSheet("background-color: green;")
        elif self.ppe_preferences[ppe_key_1] == False and self.ppe_preferences[ppe_key_2] == False:
            btn_1.setStyleSheet("background-color: none;")
            btn_2.setStyleSheet("background-color: green;")
            btn_3.setStyleSheet("background-color: none;")

    def update(self):
        self.checkState("helmet", "no_helmet", self.enable_helmet_btn, self.disable_all_helmet_btn, self.enable_no_helmet_btn)
        self.checkState("glasses", "no_glasses", self.enable_glasses_btn, self.disable_all_glasses_btn, self.enable_no_glasses_btn)
        self.checkState("vest", "no_vest", self.enable_vest_btn, self.disable_all_vest_btn, self.enable_no_vest_btn)
        self.checkState("gloves", "no_gloves", self.enable_gloves_btn, self.disable_all_gloves_btn, self.enable_no_gloves_btn)
        self.checkState("boots", "no_boots", self.enable_boots_btn, self.disable_all_boots_btn, self.enable_no_boots_btn)

    def center(self):
        width, height = self.sizeHint().width(), self.sizeHint().height()
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.move(centerPoint.x() - width // 2, centerPoint.y() - height // 2)