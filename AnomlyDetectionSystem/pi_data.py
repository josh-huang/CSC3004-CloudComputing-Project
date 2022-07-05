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
import speedtest
import psutil

sense = SenseHat()
sense.clear()


def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return bytes / MB


def database_connection(cpu, ram, download, upload, temp, humid):
    mydb = connection.connect(  # connection to database
        host="54.179.115.76",
        database="sensor",
        user="staff",
        passwd="password",
        use_pure=True,
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO SensorData (CPUUsage, RAMUsage, DownloadSpeed, UploadSpeed, Temperature, Humidity) VALUES (%s, %s, %s, %s, %s, %s)"

    val = (cpu, ram, download, upload, temp, humid)
    mycursor.execute(sql, val)
    mydb.commit()


def getMeasurement():
    temp = sense.get_temperature()
    print(temp)
    humidity = sense.get_humidity()
    print(humidity)

    speed_test = speedtest.Speedtest()
    download = bytes_to_mb(speed_test.download())
    upload = bytes_to_mb(speed_test.upload())
    print(upload)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    database_connection(cpu_usage, ram_usage, download, upload, temp, humidity)

    print("Data has been recorded in database.")


getMeasurement()
