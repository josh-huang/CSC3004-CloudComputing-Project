import pandas as pd

df = pd.read_csv('AnomlyDetectionSystem/dataset.csv')
#drop cpu cores, CPU capacity provisioned [MHZ] column
print(df)