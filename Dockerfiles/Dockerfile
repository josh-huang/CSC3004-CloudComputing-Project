#Dockerfile, Image, Container
#Adding Abnormal.py
FROM python:3

ADD abnormal.py .

RUN pip install mysql.connector

CMD ["python", "./abnormal.py"]

#Adding pi_data.py
FROM python:3

ADD pi_data.py .

RUN pip install mysql.connector speedtest psutil

CMD ["python", "./pi_data.py"]

#Adding abnormal_simulate.py
FROM python:3

ADD abnormal_simulate.py .

RUN pip install mysql.connector

CMD ["python", "./abnormal_simulate.py"]
 