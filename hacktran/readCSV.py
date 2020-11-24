# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dfPrimary1 = pd.read_csv ('datatran2017.csv', sep=";")
dfPrimary2 = pd.read_csv ('datatran2018.csv', sep=";")
dfPrimary3 = pd.read_csv ('datatran2019.csv', sep=";")
dfPrimary4 = pd.read_csv ('datatran2020.csv', sep=";")
# print(dfPrimary.columns)

def label_race(row):
    if row['mortos'] >= 1:
        return 3
    elif row['feridos'] >= 1:
        return 2
    else:
        return 1

data = { 'data':  np.concatenate((dfPrimary1["data_inversa"], dfPrimary2["data_inversa"], dfPrimary3["data_inversa"], dfPrimary4["data_inversa"])),
        'br':  np.concatenate((dfPrimary1["br"], dfPrimary2["br"], dfPrimary3["br"], dfPrimary4["br"])),
        'km': np.concatenate((dfPrimary1["km"], dfPrimary2["km"], dfPrimary3["km"], dfPrimary4["km"])),
        'lat': np.concatenate((dfPrimary1["latitude"], dfPrimary2["latitude"], dfPrimary3["latitude"], dfPrimary4["latitude"])),
        'long': np.concatenate((dfPrimary1["longitude"], dfPrimary2["longitude"], dfPrimary3["longitude"], dfPrimary4["longitude"])),
        'mortos': np.concatenate((dfPrimary1["mortos"], dfPrimary2["mortos"], dfPrimary3["mortos"], dfPrimary4["mortos"])),
        'feridos': np.concatenate((dfPrimary1["feridos"], dfPrimary2["feridos"], dfPrimary3["feridos"], dfPrimary4["feridos"]))
        }

df = pd.DataFrame (data, columns = ['data', 'br','km', 'lat', 'long', 'mortos', 'feridos'])
df["class"] = df.apply(lambda row: label_race(row), axis=1)
df.to_csv ('acidenteTransito.csv', index = False, header=True)
print (df.head())