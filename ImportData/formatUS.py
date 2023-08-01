import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


import openpyxl


def cleanValues_USA():
    df=pd.read_csv('data/imports/canada/china/CAN_china.csv', delimiter=';')

    #df = df.transpose()

    #df.reset_index(inplace=True)

    #df.columns = ['Year', 'HS280530', 'HS850231', 'HS850511', 'HS854140']

    #df = df.drop(index=0) #drop first row because it was just: 0   HTS Number      2805.3      8505.11

    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)



    # Convert the value columns to numeric
    #df['HS280530'] = df['HS280530'].str.replace('.', '').astype(int)
    #df['HS850511'] = df['HS850511'].str.replace('.', '').astype(int)

    dfHS850231 = df[['HS850231']].copy()
    dfHS850511 = df[['HS850511']].copy()
    dfHS854140 = df[['HS854140']].copy()


    df=df.drop(['HS850511', 'HS850231', 'HS854140'], axis=1)

    df=df.rename({'HS280530':'Value'}, axis=1)
    dfHS850231=dfHS850231.rename({'HS850231':'Value'}, axis=1)
    dfHS850511=dfHS850511.rename({'HS850511':'Value'}, axis=1)
    dfHS854140=dfHS854140.rename({'HS854140':'Value'}, axis=1)


    df.to_csv('data/imports/USA/china/CAN_280530ch.csv', index=True)

    dfHS850231.to_csv('data/imports/canada/china/CAN_850231ch.csv', index=True)

    dfHS850511.to_csv('data/imports/USA/china/CAN_850511ch.csv', index=True)

    dfHS854140.to_csv('data/imports/USA/china/CAN_854140ch.csv', index=True)






