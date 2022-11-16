from windows.connection import ConnectionWindow
from windows.options import OptionsWindow
from windows.publish_plain_txt import PublishPlainTXTWindow
from windows.set_preferences import SetPreferencesWindow
from windows.change_interval import ChangeIntervalWindow
from constants import *
from client import MQTTClient
from secrets import token_hex
import json, time

from PyQt5.QtCore import QThread, pyqtSignal
class MainApplication:

    def __init__(self):
        self.mqtt_client = None
        self.setupWindows()
        self.connectionWindow.show()

    def setupWindows(self):
        self.connectionWindow = ConnectionWindow()
        self.optionsWindow = OptionsWindow()
        self.publishPlainTXTWindow = PublishPlainTXTWindow()
        self.setPreferencesWindow = SetPreferencesWindow()
        self.changeIntervalWindow = ChangeIntervalWindow()

        self.connectionWindow.connect_btn.clicked.connect(self.mqttClientConnect)
        self.optionsWindow.publish_plain_txt_btn.clicked.connect(self.showPublishPlainTXTWindow)
        self.optionsWindow.set_preferences_btn.clicked.connect(self.showPreferencesWindow)
        self.optionsWindow.changee_interval_btn.clicked.connect(self.showChangeIntervalWindow)
        self.optionsWindow.disconnect_btn.clicked.connect(self.disconnectMQTTConnection)
        self.publishPlainTXTWindow.publish_btn.clicked.connect(self.publishPlainTXT)
        self.publishPlainTXTWindow.back_btn.clicked.connect(self.goBackFromPublishPlainTXTWindowToOptionsWindow)
        self.setPreferencesWindow.publish_preference_btn.clicked.connect(self.publishPPEPreferences)
        self.setPreferencesWindow.back_btn.clicked.connect(self.goBackFromSetPreferencesWindowToOptionsWindow)
        self.changeIntervalWindow.publish_interval_btn.clicked.connect(self.publishInterval)
        self.changeIntervalWindow.back_btn.clicked.connect(self.goBackFromChangeIntervalWindowToOptionsWindow)

        self.connectionWindow.pressedEnter.connect(self.mqttClientConnect)
        self.connectionWindow.pressedEscape.connect(lambda: self.connectionWindow.close())
        self.optionsWindow.pressedBackspace.connect(self.disconnectMQTTConnection)
        self.changeIntervalWindow.pressedBackspace.connect(self.goBackFromChangeIntervalWindowToOptionsWindow)
        self.publishPlainTXTWindow.pressedBackspace.connect(self.goBackFromPublishPlainTXTWindowToOptionsWindow)
        self.setPreferencesWindow.pressedBackspace.connect(self.goBackFromSetPreferencesWindowToOptionsWindow)

    def mqttClientConnect(self):
        ip_address = self.connectionWindow.ip_address_input.text()
        topic = self.connectionWindow.topic_input.text()
        username = self.connectionWindow.username_input.text()
        password = self.connectionWindow.password_input.text()

        if len(ip_address) > 0 and len(topic) > 0 and len(username) > 0 and len(password) > 0:
            self.mqtt_client = MQTTClient(ip_address,f"{token_hex(16)}",topic,username,password)
            self.connectingThread = ConnectingThread(self, self.mqtt_client)
            self.connectingThread.isconnected.connect(self.showOptionsWindow)
            self.connectingThread.clearinputs.connect(self.clearConnectionInputs)
            self.connectingThread.start()
        else:
            print("Missing inputs")

    def clearConnectionInputs(self):
        self.connectionWindow.ip_address_input.clear()
        self.connectionWindow.topic_input.clear()
        self.connectionWindow.username_input.clear()
        self.connectionWindow.password_input.clear()

    def showOptionsWindow(self):
        self.connectionWindow.close()
        self.optionsWindow.show()

    def disconnectMQTTConnection(self):
        self.optionsWindow.close()
        self.connectionWindow.show()
        self.mqtt_client.stop()
        self.mqtt_client = None

    def goBackFromPublishPlainTXTWindowToOptionsWindow(self):
        self.publishPlainTXTWindow.close()
        self.optionsWindow.show()

    def showPublishPlainTXTWindow(self):
        self.optionsWindow.close()
        self.publishPlainTXTWindow.show()
    
    def publishPlainTXT(self):
        if self.mqtt_client is not None:
            self.mqtt_client.client.publish(topic=self.mqtt_client.topic, payload=self.publishPlainTXTWindow.plaintext_input.toPlainText())
            print(f"Payload published to {self.mqtt_client.topic}.")

    def showPreferencesWindow(self):
        self.optionsWindow.close()
        self.setPreferencesWindow.show()

    def publishPPEPreferences(self):
        if self.mqtt_client is not None:
            payload = json.dumps(self.setPreferencesWindow.ppe_preferences)
            self.mqtt_client.client.publish(topic=self.mqtt_client.topic, payload=payload)
            print(f"Payload published to {self.mqtt_client.topic}.")

    def goBackFromSetPreferencesWindowToOptionsWindow(self):
        self.setPreferencesWindow.close()
        self.optionsWindow.show()

    def showChangeIntervalWindow(self):
        self.optionsWindow.close()
        self.changeIntervalWindow.show()

    def publishInterval(self):
        interval = self.changeIntervalWindow.detection_interval_input.text()
        if interval.isdigit():
            interval = int(interval)
            payload = json.dumps({"detection_interval": interval})
            self.mqtt_client.client.publish(topic=self.mqtt_client.topic, payload=payload)
            print(f"Payload published to {self.mqtt_client.topic}.")
        else:
            print("Invalid input!")

    def goBackFromChangeIntervalWindowToOptionsWindow(self):
        self.changeIntervalWindow.close()
        self.optionsWindow.show()
class ConnectingThread(QThread):

    isconnected = pyqtSignal()
    clearinputs = pyqtSignal()

    def __init__(self, mainapp: MainApplication, mqtt_client: MQTTClient, parent=None):
        super(ConnectingThread, self).__init__()
        self.mqtt_client = mqtt_client
        self.mainapp = mainapp

    def run(self):
        try:
            self.mqtt_client.start()
            n = 0
            while not self.mqtt_client.isauthorized:
                n += 1
                if n >= 5:
                    break
                time.sleep(1)
            if self.mqtt_client.isauthorized:
                self.clearinputs.emit()
                self.isconnected.emit()
            else:
                print(f"Not authorized.")
        except Exception as e:
            print(f"{e}")