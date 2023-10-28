import os
import pandas as pd

for file in os.listdir('/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/csvs'):
    df = pd.read_csv(f'/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/csvs/{file}')
    df = df.dropna()
    dropped = df.drop(columns='date')
    grouped = df.groupby(['state','city','ibgeID','dose','vaccine','sex','age','pop2021']).sum().reset_index()
    grouped.to_csv(f'/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/processed/{file}', index= False)
