import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


import openpyxl


def cleanValues_USA():
    df=pd.read_csv('data/imports/USA/allValues.csv', delimiter=';')

    df = df.transpose()

    df.reset_index(inplace=True)

    df.columns = ['Year', 'HS280530', 'HS850231', 'HS850511', 'HS854140']

    df = df.drop(index=0) #drop first row because it was just: 0   HTS Number      2805.3      8505.11

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


    df.to_csv('data/imports/USA/US_280530.csv', index=True)

    dfHS850231.to_csv('data/imports/USA/US_850231.csv', index=True)

    dfHS850511.to_csv('data/imports/USA/US_850511.csv', index=True)

    dfHS854140.to_csv('data/imports/USA/US_854140.csv', index=True)


    """"
    fai la stessa cosa per dati sul peso, poi fondi le coppie di files, poi puoi usare funzione  loadImport
    """










def showTrend_RE_Magnets_USA():

    imports=getRE_Magnets_USA()

    plt.figure(figsize=(14, 10))  # Adjust the values as per your requirement

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports[['HS280530', 'HS850511']], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import of rare earths(HS280530) and permanent magnets (HS850511)')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    plt.show()







