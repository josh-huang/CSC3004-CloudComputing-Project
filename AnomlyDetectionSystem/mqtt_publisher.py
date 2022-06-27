# import pandas as pd

# df = pd.read_csv('AnomlyDetectionSystem/dataset.csv')
# #drop cpu cores, CPU capacity provisioned [MHZ] column
# print(df)

# Importing the library
import paho.mqtt.publish as publish
from sense_hat import SenseHat
from time import sleep
import json

MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "CSC3004/Temperature"

sense = SenseHat()
sense.clear()

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    message = {'temperature': temp, 'humidity':humidity}
    publish.single(MQTT_PATH, payload=json.dumps(message), hostname=MQTT_SERVER)
    sleep(5)

