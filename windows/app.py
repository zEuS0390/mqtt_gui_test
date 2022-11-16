from windows.connection import ConnectionWindow
from windows.options import OptionsWindow
from windows.publish_plain_txt import PublishPlainTXTWindow
from windows.set_preferences import SetPreferencesWindow
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

        self.connectionWindow.connect_btn.clicked.connect(self.mqttClientConnect)
        self.optionsWindow.publish_plain_txt_btn.clicked.connect(self.showPublishPlainTXTWindow)
        self.optionsWindow.set_preferences_btn.clicked.connect(self.showPreferencesWindow)
        self.optionsWindow.disconnect_btn.clicked.connect(self.disconnectMQTTConnection)
        self.publishPlainTXTWindow.publish_btn.clicked.connect(self.publishPlainTXT)
        self.publishPlainTXTWindow.back_btn.clicked.connect(self.goBackFromPublishPlainTXTWindowToOptionsWindow)

        self.setPreferencesWindow.publish_preference_btn.clicked.connect(self.publishPPEPreferences)
        self.setPreferencesWindow.back_btn.clicked.connect(self.goBackFromSetPreferencesWindowToOptionsWindow)

    def mqttClientConnect(self):
        ip_address = self.connectionWindow.ip_address_input.text()
        topic = self.connectionWindow.topic_input.text()
        username = self.connectionWindow.username_input.text()
        password = self.connectionWindow.password_input.text()

        if len(ip_address) > 0 and len(topic) > 0 and len(username) > 0 and len(password) > 0:
            self.mqtt_client = MQTTClient(ip_address,f"{token_hex(16)}",topic,username,password)
            self.connectingWorker = Worker(self, self.mqtt_client)
            self.connectingWorker.isconnected.connect(self.showOptionsWindow)
            self.connectingWorker.start()
            self.connectionWindow.ip_address_input.clear()
            self.connectionWindow.topic_input.clear()
            self.connectionWindow.username_input.clear()
            self.connectionWindow.password_input.clear()
        else:
            print("Missing inputs")

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

class Worker(QThread):

    isconnected = pyqtSignal()

    def __init__(self, mainapp: MainApplication, mqtt_client: MQTTClient, parent=None):
        super(Worker, self).__init__()
        self.mqtt_client = mqtt_client
        self.mainapp = mainapp

    def run(self):
        try:
            self.mqtt_client.start()
            self.isconnected.emit()
        except Exception as e:
            print(f"{e}")