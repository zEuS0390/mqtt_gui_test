from windows.connection import ConnectionWindow
from windows.options import OptionsWindow
from windows.publish_plain_txt import PublishPlainTXTWindow
from windows.set_preferences import SetPreferencesWindow
from windows.change_interval import ChangeIntervalWindow
from windows.monitor import MonitorWindow
from constants import *
from secrets import token_hex
import json, time, cv2
import numpy as np

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QThread, QThreadPool, QRunnable, pyqtSignal, QObject
from paho.mqtt.client import Client
from secrets import token_hex
import base64

class MainApplication:

    def __init__(self):
        self.mqtt_client = Client(f"{token_hex(16)}")
        self.host = None
        self.topic = None
        self.username = None
        self.password = None
        self.isConnected = False
        self.threadpool = QThreadPool()
        self.videoSteamThread = VideoStreamThread()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.setupWindows()
        self.connectionWindow.show()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.isConnected = True
        elif rc == 5:
            self.isConnected = False

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload}")
        payload = msg.payload.decode()
        data = json.loads(payload)

        if "image" in data:
            encodedImage = data["image"]
            buffer = base64.b64decode(encodedImage)
            npimg = np.frombuffer(buffer, dtype=np.uint8)
            img = cv2.imdecode(npimg, 1)
            img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
            self.updateView2(img)

    def setupWindows(self):
        self.connectionWindow = ConnectionWindow()
        self.optionsWindow = OptionsWindow()
        self.monitorWindow = MonitorWindow()
        self.publishPlainTXTWindow = PublishPlainTXTWindow()
        self.setPreferencesWindow = SetPreferencesWindow()
        self.changeIntervalWindow = ChangeIntervalWindow()

        self.connectionWindow.connect_btn.clicked.connect(self.mqttClientConnect)
        self.optionsWindow.monitor_btn.clicked.connect(self.showMonitorWindow)
        self.optionsWindow.publish_plain_txt_btn.clicked.connect(self.showPublishPlainTXTWindow)
        self.optionsWindow.set_preferences_btn.clicked.connect(self.showPreferencesWindow)
        self.optionsWindow.changee_interval_btn.clicked.connect(self.showChangeIntervalWindow)
        self.optionsWindow.disconnect_btn.clicked.connect(self.disconnectMQTTConnection)
        self.monitorWindow.back_btn.clicked.connect(self.goBackFromMonitorWindowToOptionsWindow)
        self.monitorWindow.stop_btn.clicked.connect(self.videoSteamThread.stop_camera)
        self.monitorWindow.start_btn.clicked.connect(self.videoSteamThread.start_camera)
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

        self.videoSteamThread.updateView.connect(self.updateView1)
        self.videoSteamThread.start()
    
    def getConnectionStatus(self):
        return self.isConnected

    def onMessage(self, title, content):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(content)
        msg.setWindowTitle(title)
        msg.exec()

    def mqttClientConnect(self):
        self.host = self.connectionWindow.ip_address_input.text()
        self.topic = self.connectionWindow.topic_input.text()
        username = self.connectionWindow.username_input.text()
        password = self.connectionWindow.password_input.text()

        if len(self.host) > 0 and len(self.topic) > 0 and len(username) > 0 and len(password) > 0:
            self.mqtt_client.username_pw_set(username, password)
            connectWorker = ConnectWorker(self.mqtt_client, self.getConnectionStatus, self.host, self.topic, 1883)
            connectWorker.signals.message.connect(self.onMessage)
            connectWorker.signals.success.connect(self.showOptionsWindow)
            connectWorker.signals.clearInputs.connect(self.clearConnectionInputs)
            connectWorker.signals.enableButton.connect(lambda: self.connectionWindow.connect_btn.setDisabled(False))
            self.threadpool.start(connectWorker)
            self.connectionWindow.connect_btn.setDisabled(True)

    def clearConnectionInputs(self):
        self.connectionWindow.ip_address_input.clear()
        self.connectionWindow.topic_input.clear()
        self.connectionWindow.username_input.clear()
        self.connectionWindow.password_input.clear()

    def showOptionsWindow(self):
        self.connectionWindow.close()
        self.optionsWindow.show()

    def disconnectMQTTConnection(self):
        self.isConnected = False
        self.mqtt_client.unsubscribe(self.topic)
        self.optionsWindow.close()
        self.connectionWindow.show()

    def goBackFromMonitorWindowToOptionsWindow(self):
        self.monitorWindow.close()
        self.optionsWindow.show()

    def showMonitorWindow(self):
        self.optionsWindow.close()
        self.monitorWindow.show()

    def updateView1(self, cv_image):
        qt_image = self.convertFromCVToQT(cv_image)
        self.monitorWindow.image1.setPixmap(qt_image)

    def updateView2(self, cv_image):
        qt_image = self.convertFromCVToQT(cv_image)
        self.monitorWindow.image2.setPixmap(qt_image)

    def convertFromCVToQT(self, cv_image):
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_image.shape
        bytes_per_line = channels * width
        convert_to_QT_format = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_QT_format.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def goBackFromPublishPlainTXTWindowToOptionsWindow(self):
        self.publishPlainTXTWindow.close()
        self.optionsWindow.show()

    def showPublishPlainTXTWindow(self):
        self.optionsWindow.close()
        self.publishPlainTXTWindow.show()
    
    def publishPlainTXT(self):
        self.mqtt_client.publish(topic=self.topic, payload=self.publishPlainTXTWindow.plaintext_input.toPlainText())
        print(f"Payload published to {self.topic}.")

    def showPreferencesWindow(self):
        self.optionsWindow.close()
        self.setPreferencesWindow.show()

    def publishPPEPreferences(self):
        payload = json.dumps({"ppe_preferences":self.setPreferencesWindow.ppe_preferences})
        self.mqtt_client.publish(topic=self.topic, payload=payload)
        print(f"Payload published to {self.topic}.")

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
            self.mqtt_client.publish(topic=self.topic, payload=payload)
            print(f"Payload published to {self.topic}.")
        else:
            print("Invalid input!")

    def goBackFromChangeIntervalWindowToOptionsWindow(self):
        self.changeIntervalWindow.close()
        self.optionsWindow.show()

class ConnectSignals(QObject):
    message = pyqtSignal(str, str)
    clearInputs = pyqtSignal()
    enableButton = pyqtSignal()
    success = pyqtSignal()

class ConnectWorker(QRunnable):

    def __init__(self, mqtt_client: Client, getConnectionStatus, host: str, topic: str, port: int):
        super(ConnectWorker, self).__init__()
        self.mqtt_client = mqtt_client
        self.getConnectionStatus = getConnectionStatus
        self.host = host
        self.topic = topic
        self.port = port
        self.signals = ConnectSignals()

    def __del__(self):
        print("QRunnable deleted.")

    def run(self):
        try:
            self.mqtt_client.connect(self.host, self.port)
            self.mqtt_client.loop_start()
            times = 0
            while not self.getConnectionStatus():
                if times > 5:
                    break
                times += 1
                time.sleep(1)
            if self.getConnectionStatus():
                print("Success.")
                self.mqtt_client.subscribe(self.topic)
                self.signals.enableButton.emit()
                self.signals.success.emit()
                self.signals.clearInputs.emit()
            else:
                print("Try again.")
                self.signals.message.emit("Time Out", "Try again.")
                self.mqtt_client.loop_stop()
                self.signals.enableButton.emit()
        except Exception as e:
            self.signals.message.emit("Error", f"{e}")
            self.signals.enableButton.emit()

class VideoStreamThread(QThread):

    updateView = pyqtSignal(np.ndarray)

    def __init__(self):
        super(VideoStreamThread, self).__init__()
        self.device = 0
        self.run_flag = False

    def run(self):
        while True:
            try:
                cap = cv2.VideoCapture(self.device)
            except:
                time.sleep(5)
                continue
            while self.run_flag:
                ret, frame = cap.read()
                if ret:
                    self.updateView.emit(frame)
                    time.sleep(0.03)
            cap.release()
            time.sleep(5)

    def start_camera(self):
        self.run_flag = True
    
    def stop_camera(self):
        self.run_flag = False