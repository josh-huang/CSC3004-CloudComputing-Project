from msilib.schema import tables
import paho.mqtt.client as mqtt
import pandas as pd
import psutil
import os
import json
import speedtest

temp_array= []
counter = 0

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return bytes/MB

   
#mqtt subscribe topic 
def on_connect(client, userdata, flags, rc):
    client.subscribe("CSC3004/Temperature")

#mqtt client receive message 
def on_message(client, userdata, msg):
    speed_test = speedtest.Speedtest()
    download_speed = bytes_to_mb(speed_test.download())
    upload_speed = bytes_to_mb(speed_test.upload())
    
    payload = json.loads(msg.payload)
    temperature = payload['temperature']
    humidity = payload['humidity']
    # if path.exists('dataset_real_time.csv'):
    tableA = pd.read_csv('dataset_real_time.csv')
    print(tableA)
    
    cpu_percent = psutil.cpu_percent()
    disk_percent = psutil.disk_usage(os.sep).percent
    ram_usage = psutil.virtual_memory().percent
    
    global counter
    if temperature > 30.5 and ram_usage > 80:
        tableA.loc[str(counter)] = [0, cpu_percent, ram_usage, download_speed, upload_speed, temperature, humidity, 1]
    else:
        tableA.loc[str(counter)] = [0, cpu_percent, ram_usage, download_speed, upload_speed, temperature, humidity, 0]
    counter += 1
    tableA.drop(tableA.filter(regex="Unname"),axis=1, inplace=True)
    tableA.to_csv('dataset_real_time.csv')
    

#mqtt client connection 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()