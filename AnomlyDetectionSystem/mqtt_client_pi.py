# import pandas as pd

# df = pd.read_csv('AnomlyDetectionSystem/dataset.csv')
# #drop cpu cores, CPU capacity provisioned [MHZ] column
# print(df)

# Importing the library
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
from time import sleep
import json
import mysql.connector as connection

sense = SenseHat()
sense.clear()

# mqtt subscribe topic
def on_connect(client, userdata, flags, rc):
    client.subscribe("CSC3004/Temperature")


# mqtt client receive message
def on_message(client, userdata, msg):
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    payload = json.loads(msg.payload)
    download = payload["downloadSpeed"]
    upload = payload["uploadSpeed"]
    cpu_usage = payload["cpuUsage"]
    ram_usage = payload["ramUsage"]

    database_connection(cpu_usage, ram_usage, download, upload, temp, humidity)


def database_connection(cpu, ram, download, upload, temp, humid):
    mydb = connection.connect(  # connection to database
        host="18.143.63.224",
        database="sensor",
        user="staff",
        passwd="password",
        use_pure=True,
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO SensorData (CPUUsage, RAMUsage, DownloadSpeed, UploadSpeed, Temperature, Humidity) VALUES (%s, %s, %s, %s, %s, %s)"

    val = (0.5, 1, 0, 0.5, 1, 0)
    mycursor.execute(sql, val)
    mydb.commit()


# mqtt client connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
