import mysql.connector as connection


def connect_database(cpu, ram, download, upload, temp, humid):
    mydb = connection.connect(
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


def main():
    cpu = input("Enter the cpu usage: \n")
    ram = input("Enter the ram usage: \n")
    download = input("Enter the download speed: \n")
    upload = input("Enter the upload speed: \n")
    temp = input("Enter the temperature: \n")
    humid = input("Enter the humidity: \n")

    connect_database(cpu, ram, download, upload, temp, humid)
    print("Data has been recorded in database.")


main()
