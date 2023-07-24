import pandas as pd
import numpy as np
import csv

def loadCAPFMdb():    #load the whole CAPFM database and rename columns

    df=pd.read_csv("data/CAPMF/CAPMF_Comp_10022023.csv", delimiter=";",decimal=".")
    df = df.rename(columns={"ISO":"Country", "Component":"Policy", "Comp":"Stringency"})

    return df

def loadExcludedPolicies():     #load file with the policies that I won't consider



    with open("data/CAPMF/excludedPolicies.csv", "r", encoding='utf-8-sig') as file:
        ExcludedPolicies = [item for sublist in csv.reader(file) for item in sublist]

    return ExcludedPolicies

def cleanCAPFMpolicies():    # clean the CAPFM database deleting rows of not relevant policies



    df = loadCAPFMdb()
    ExcludedPolicies = loadExcludedPolicies()

    df = df[~df.Policy.isin(ExcludedPolicies)]

    #save the new cleaned database to a CSV.
    #df.to_csv("data/CAPMF/cleanedCAPMF.csv", index=False)

    return df

def getEU():
    df = cleanCAPFMpolicies()

    df = df.loc[df['Country'] == 'EUR']

    #df.to_csv("data/CAPMF/EU_cleanedCAPMF.csv", index=False)

    return df


def getEU26():
    EU26 = ['AUT', 'BEL', 'BGR', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'HUN', 'HRV', 'IRL', 'ITA', 'LTU', 'LUX', 'LVA', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVN','SVK', 'SWE']

    df = cleanCAPFMpolicies()

    df = df[df.Country.isin(EU26)]

    #df.to_csv("data/CAPMF/EU26_cleanedCAPMF.csv", index=False)

    return df

def getNonEU():

    nonEU = ['JPN', 'USA', 'BRA', 'KOR', 'CAN']

    if nonEU:
        df = cleanCAPFMpolicies()

        df = df[~df.Country.isin(nonEU)]

    else:
        EU26 = ['AUT', 'BEL', 'BGR', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'HUN', 'HRV', 'IRL', 'ITA',
                'LTU', 'LUX', 'LVA', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVN', 'SVK', 'SWE']

        df = cleanCAPFMpolicies()

        df = df[~df.Country.isin(EU26)]

        df.to_csv("data/CAPMF/NonEU_cleanedCAPMF.csv", index=False)

    return df









