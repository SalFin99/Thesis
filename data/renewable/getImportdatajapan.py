import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import openpyxl


def getRE_Japan():
    df = pd.read_csv('../imports/japan/280530_2000-2020.csv', delimiter=';', decimal=',', thousands='.')

    df['Period'] = pd.to_datetime(df['Period'], format='%Y')
    df.set_index('Period', inplace=True)

    print(df)

    return df



def getMagnets_Japan():
    df = pd.read_csv('../imports/japan/850511_2000-2020.csv', delimiter=';', decimal=',', thousands='.')

    df['Period'] = pd.to_datetime(df['Period'], format='%Y')
    df.set_index('Period', inplace=True)

    print(df)

    return df

