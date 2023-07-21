import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import openpyxl


def getRE_Korea():
    df=pd.read_csv('../data/imports/SouthKorea/280530_2000-2020.csv', delimiter=';', decimal='.')

    df = df.drop(['Items', 'H.S Code', 'Export Weight', 'Export Value', 'Trade Balance'], axis=1)
    df.columns = ['Year', 'Import_Weight', 'Import_Value']


    df.reset_index(drop=True)
    df = df.drop(index=0)
    df=df.set_index('Year')

    # Convert the value columns to numeric
    df['Import_Weight'] = df['Import_Weight'].str.replace(',', '').str.replace('.', '').astype(int)
    df['Import_Value'] = df['Import_Value'].str.replace(',', '').str.replace('.', '').astype(int)

    df['Import_Weight'] = df['Import_Weight']
    df['Import_Value'] = df['Import_Value']



    print(df.head(5))

    return df


    print(df.head())


def getMagnets_Korea():
    df=pd.read_csv('../data/imports/SouthKorea/850511_2000-2020.csv', delimiter=';', decimal='.')

    df = df.drop(['Items', 'H.S Code', 'Export Weight', 'Export Value', 'Trade Balance'], axis=1)
    df.columns = ['Year', 'Import_Weight', 'Import_Value']


    df.reset_index(drop=True)
    df = df.drop(index=0)
    df=df.set_index('Year')

    # Convert the value columns to numeric
    df['Import_Weight'] = df['Import_Weight'].str.replace(',', '').str.replace('.', '').astype(int)
    df['Import_Value'] = df['Import_Value'].str.replace(',', '').str.replace('.', '').astype(int)

    df['Import_Weight'] = df['Import_Weight']
    df['Import_Value'] = df['Import_Value']

    print(df.dtypes)




    print(df.head(5))

    return df

getMagnets_Korea()




def showTrend_RE_Korea():

    imports=getRE_Korea()

    plt.figure(figsize=(14, 10))  # Adjust the values as per your requirement

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports[['Import_Weight', 'Import_Value']], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import of rare earths(HS280530) - UNIT:USD 1,000 / Ton')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    plt.show()


#showTrend_RE_Korea()

def showTrend_Magnets_Korea():

    imports=getMagnets_Korea()

    plt.figure(figsize=(14, 10))  # Adjust the values as per your requirement

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports[['Import_Weight', 'Import_Value']], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import of permanent magnets (HS850511) - UNIT:USD 1,000 / Ton')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    plt.show()

showTrend_Magnets_Korea()


