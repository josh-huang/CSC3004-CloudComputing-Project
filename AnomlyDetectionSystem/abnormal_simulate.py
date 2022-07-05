import mysql.connector as connection

mydb = connection.connect(
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
