import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import openpyxl


def getRE_Japan():
    df = pd.read_csv('data/imports/japan/280530_2000-2020.csv', delimiter=';',  decimal=',', thousands='.')

    df['Period'] = pd.to_datetime(df['Period'], format='%Y')
    df.set_index('Period', inplace=True)

    print(df)

    return df

def showTrend_RE_Japan():
    imports = getRE_Japan()

    plt.figure(figsize=(14, 10))
    plt.plot(imports.index, imports['NetWgt'], label='NetWgt')
    plt.plot(imports.index, imports['PrimaryValue'], label='PrimaryValue')

    plt.xlabel('Period')
    plt.ylabel('Values')
    plt.title('NetWgt and PrimaryValue')
    plt.legend()
    plt.show()


"""

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports[['PrimaryValue']], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import rare earths (HS280530)')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)
        plt.show()
"""

def getMagnets_Japan():
    df = pd.read_csv('data/imports/japan/850511_2000-2020.csv', delimiter=';',  decimal=',', thousands='.')

    df['Period'] = pd.to_datetime(df['Period'], format='%Y')
    df.set_index('Period', inplace=True)

    print(df)

    return df

def showTrend_Magnets_Japan():
    imports = getRE_Japan()

    plt.figure(figsize=(20, 20))
    #plt.plot(imports.index, imports['NetWgt'], label='NetWgt')
    plt.plot(imports.index, imports['PrimaryValue'], label='PrimaryValue')

    plt.xlabel('Period')
    plt.ylabel('Values')
    plt.title('NetWgt and PrimaryValue')

    plt.legend()
    plt.show()


showTrend_Magnets_Japan()