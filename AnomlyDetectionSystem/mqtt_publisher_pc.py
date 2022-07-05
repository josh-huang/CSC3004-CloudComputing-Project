from msilib.schema import tables
import paho.mqtt.client as mqtt
import pandas as pd
import psutil
import json
import speedtest
import paho.mqtt.publish as publish
from time import sleep

temp_array = []
counter = 0

MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "CSC3004/Temperature"


def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return bytes / MB


# mqtt publisher send message
while True:
    speed_test = speedtest.Speedtest()
    download_speed = bytes_to_mb(speed_test.download())
    upload_speed = bytes_to_mb(speed_test.upload())
    cpu_percent = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    message = {
        "downloadSpeed": download_speed,
        "uploadSpeed": upload_speed,
        "cpuUsage": cpu_percent,
        "ramUsage": ram_usage,
    }
    publish.single(MQTT_PATH, payload=json.dumps(message), hostname=MQTT_SERVER)
    sleep(5)
