import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


import openpyxl


def getRE_Magnets_Canada():
    df=pd.read_csv('../imports/canada/850511_2000-2020MAGNETS.csv', delimiter=';')

    df = df.transpose()

    df.reset_index(inplace=True)
    df.columns = ['Year', 'HS850511']
    df=df.set_index('Year')

    # Convert the value columns to numeric


    return df

getRE_Magnets_Canada()



def showTrend_RE_Magnets_Canada():

    imports=getRE_Magnets_Canada()
    print(imports.dtypes)
    plt.figure(figsize=(14, 10))  # Adjust the values as per your requirement

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports['HS850511'], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import of permanent magnets (HS850511)')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    plt.show()

showTrend_RE_Magnets_Canada()







