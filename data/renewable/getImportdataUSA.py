import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


import openpyxl


def getRE_Magnets_USA():
    df=pd.read_csv('../imports/USA/rareEarths&magnets.csv', delimiter=';')
    df=df.drop('Data Type', axis=1)

    df = df.transpose()
    df.reset_index(inplace=True)
    df.columns = ['Year', 'HS280530', 'HS850511', 'Total']
    df = df.drop(index=0)
    df=df.set_index('Year')

    # Convert the value columns to numeric
    df['HS280530'] = df['HS280530'].str.replace('.', '').astype(int)
    df['HS850511'] = df['HS850511'].str.replace('.', '').astype(int)

    print(df.head(5))

    return df


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


showTrend_RE_Magnets_USA()





