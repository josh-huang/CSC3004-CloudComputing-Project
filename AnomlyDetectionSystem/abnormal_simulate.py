import mysql.connector as connection


def connect_database(cpu, ram, download, upload, temp, humid):
    mydb = connection.connect(
        host="18.143.63.224",
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


def main():
    cpu = input("Enter the cpu usage: \n")
    ram = input("Enter the cpu usage: \n")
    download = input("Enter the cpu usage: \n")
    upload = input("Enter the cpu usage: \n")
    temp = input("Enter the cpu usage: \n")
    humid = input("Enter the cpu usage: \n")

    connect_database(cpu, ram, download, upload, temp, humid)
    print("Data has been recorded in database.")
