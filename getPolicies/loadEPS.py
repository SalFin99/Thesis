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




