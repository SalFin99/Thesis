import pandas as pd
import numpy as np
import csv

def loadCAPFMdb():
    df=pd.read_csv("data/CAPMF/CAPMF_Comp_10022023.csv", delimiter=";",decimal=".")
    df = df.rename(columns={"ISO":"Country", "Component":"Policy", "Comp":"Stringency"})

    return df

def loadExcludedPolicies():

    with open("data/CAPMF/excludedPolicies.csv", "r", encoding='utf-8-sig') as file:
        ExcludedPolicies = [item for sublist in csv.reader(file) for item in sublist]

    return ExcludedPolicies



def cleanCAPFMpolicies():
    df = loadCAPFMdb()
    ExcludedPolicies = loadExcludedPolicies()

    print(ExcludedPolicies)

    df = df[~df.Policy.isin(ExcludedPolicies)]

    #df.to_csv("data/CAPMF/cleanedCAPMF.csv", index=False)

    return df








