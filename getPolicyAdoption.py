import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def getAdoption() :
    df = pd.read_csv('data/policyAdoption/EU27_policyAdoption.csv', delimiter=';')

    df['Year']=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    return df