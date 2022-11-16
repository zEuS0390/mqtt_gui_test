from paho.mqtt.client import Client, connack_string
import time

class MQTTClient:

    def __init__(self, broker, client_id, topic, username, password, on_message=None, port=1883):
        self.client_id = client_id
        self.topic = topic
        self.broker = broker
        self.port = port
        self.isauthorized = False
        self.client = Client(client_id=self.client_id)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        if on_message:
            self.client.on_message = self.on_message
        
    def start(self):
        while True:
            try:
                self.client.connect(self.broker, self.port)
                break
            except Exception as e:
                print(f"{e}")
            time.sleep(0.03)
        self.client.loop_start()

    def stop(self):
        self.client.disconnect()
        self.client.loop_stop()

    def __del__(self):
        self.client.disconnect()
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connection result: {connack_string(rc)}")
        if rc == 0:
            self.isauthorized = True
            self.client.subscribe(self.topic)
        elif rc == 5:
            self.isauthorized = False
            # Not authorized (incorrect username or password)
            pass

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload}")