import pandas as pd
import numpy as np
import csv

def loadCAPFMdb():
    #load the whole CAPFM database and rename columns
    df=pd.read_csv("data/CAPMF/CAPMF_Comp_10022023.csv", delimiter=";",decimal=".")
    df = df.rename(columns={"ISO":"Country", "Component":"Policy", "Comp":"Stringency"})

    return df

def loadExcludedPolicies():

    #load file with the policies that I won't consider

    with open("data/CAPMF/excludedPolicies.csv", "r", encoding='utf-8-sig') as file:
        ExcludedPolicies = [item for sublist in csv.reader(file) for item in sublist]

    return ExcludedPolicies



def cleanCAPFMpolicies():

    # clean the CAPFM database deleting rows for not relevant policies

    df = loadCAPFMdb()
    ExcludedPolicies = loadExcludedPolicies()

    print(ExcludedPolicies)

    df = df[~df.Policy.isin(ExcludedPolicies)]

    #save the new cleaned database to a CSV.
    #df.to_csv("data/CAPMF/cleanedCAPMF.csv", index=False)

    return df








