import pandas as pd
import numpy as np
import openpyxl


def load_and_cleanEPScontrol():
    df=pd.read_csv("data/eps/epsControl/controlEPS.csv", decimal=".")

    df=df.rename(columns={'Value':'EPSvalue'})

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df=df.drop(["Variable","YEA","Unit Code","Unit","PowerCode Code","PowerCode","Reference Period Code","Reference Period","Flag Codes","Flags"], axis=1)

    df['logEPS']=np.log(df['EPSvalue'])


    df.to_csv("OG_EPSandLogEPS_Control.csv", index=False)


    #create a pivot table with MultiIndex with COU and Country
    df=df.pivot_table(values=["EPSvalue", "logEPS"], index="Year", columns=["COU","Country"])
    #print(df)
    return df

def load_and_cleanEPStreatment():
    df=pd.read_csv("data/eps/epsEU.csv", decimal=".", delimiter=";")

    df=df.rename(columns={'Value':'EPSvalue'})

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df['logEPS']=np.log(df['EPSvalue'])

   # df.to_csv("EPSandLogEPS_treatment.csv", index=False)


    #create a pivot table with MultiIndex with COU and Country
    df=df.pivot_table(values=["EPSvalue", "logEPS"], index="Year", columns=["COU","Country"])
    print(df)


    #print(df)
    return df

def loadEPSMbyPolicy():

    df=pd.read_csv("data/eps/EPSbyPolicy.csv", delimiter=",")
    df = df.rename(columns={"ISO":"Country", "Component":"Policy", "Comp":"Stringency"})

    return df

def EPSbyPolicyEU():
    EU = ['AUT', 'DEU', 'DNK', 'ESP', 'FIN', 'FRA', 'IRL', 'ITA', 'PRT', 'SWE']

    df = loadEPSMbyPolicy()

    df = df[df.Country.isin(EU)]

    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year

    df['Country'] = 'EU'

    df = df.pivot_table(index=['Country','Year'], columns=['Policy'], values='Value', aggfunc=np.mean)


    return df

def EPSbyPolicyControl():
    EU = ['AUT', 'BEL','CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'IRL', 'ITA', 'LUX', 'NLD', 'POL', 'PRT', 'SVN','SVK', 'SWE']

    df = loadEPSMbyPolicy()

    df = df[~df.Country.isin(EU)]

    df = df[df['Country'] != 'HUN']

    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year

    df = df.pivot_table(index=['Country', 'Year'], columns='Policy', values='Value')

    return df

def EPSbyPolicyAll():
    EU = EPSbyPolicyEU()
    Control = EPSbyPolicyControl()


    all = pd.concat([EU, Control], axis=0, ignore_index=False)

    all.to_csv('data/eps/epsAllByPolicy.csv', index=True)