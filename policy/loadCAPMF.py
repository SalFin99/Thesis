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

    #df = cleanCAPFMpolicies()

    df = pd.read_csv("data/CAPMF/stringency/stringency.csv", delimiter=";",decimal=".")
    df = df[df.Country.isin(EU26)]

    #print(df)
    return df




def getControl():

    control = ['CHE'] #Turkey not included

    df = pd.read_csv("data/CAPMF/stringency/stringency.csv", delimiter=";", decimal=".")
    df = df[df.Country.isin(control)]

    # print(df)
    return df

    #df.Year = pd.to_datetime(df['year'], format='%Y').dt.year
    #df.set_index('year', inplace=True)


"""
grouped=df.groupby(['Country', 'Policy'])

    result_dataframes = {}

    # basically every iteration select country-policy pair and takes all the values.
    for (country, policy), group_df in grouped:
        if (country, policy) not in result_dataframes:
            result_dataframes[(country, policy)] = group_df.drop(['Policy'], axis=1)
        else:
            result_dataframes[(country, policy)] = pd.concat(
                [result_dataframes[(country, policy)], group_df.drop(['Policy'], axis=1)])

    policy_dict = {}

    for (country, policy), df in result_dataframes.items():

        if policy in policy_dict:
            policy_dict[policy] = pd.concat([policy_dict[policy],df])

        else:
            policy_dict[policy] = df

    merged_df = pd.DataFrame()

    print(policy_dict)

    for policy, df in policy_dict.items():
        df = df.rename(columns={"Stringency": policy})

        if merged_df.empty:
            merged_df = df[['year', 'Country', policy]]
        else:
            merged_df = pd.merge(merged_df, df[['year', 'Country', policy]], on=['year', 'Country'],
                                 how='left')

    merged_df.to_csv("data/CAPMF/stringency/policyStringency/PolicyDatasets.csv", index=True)


"""


"""
    for policy, df in policy_dict.items():
        filename = f"{policy}.csv"
        df = df.rename(columns={"Stringency": policy})
        df.to_csv("data/CAPMF/stringency/policyStringency/" + filename , index=True)
        print(f"Saved {policy} data")
"""



"""
        # Create a filename based on country and hscode

        filename = f"{country}_{policy}.csv"


        # Save the DataFrame to a CSV file
        df.to_csv("data/" + filename, index=True)
        print(f"File {filename} created.")

"""













