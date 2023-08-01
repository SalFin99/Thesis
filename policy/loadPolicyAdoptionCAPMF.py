import pandas as pd
import numpy as np


def getAdoption() :
    df = pd.read_csv('data/policyAdoption/EU27_policyAdoption.csv', delimiter=';')

    df['Year']=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    return df