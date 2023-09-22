from policy import loadCAPMF, loadEPS
import numpy as np
import pandas as pd

"""
These functions create the pivot tables for climate policy stringency data. 
Every table is indexed by country and year.
The columns represent the different policies.
The pivot table syntax says that for every ‘index’, return the ‘aggfunc’ of the ‘values’ column(s), 
segregated (further grouped) by ‘columns’.

Tables are built for EU (aggregated EU level), EU26 countries, Non-EU countries, sample of Non-EU countries. 
The sample must be specified in the loadCAPMF.getControl() function, in the nonEU[] list. 
This sample will be then used to test the common trend assumption of DID and select countries for the control group.
"""


def buildPanel_PolicyStringency():
    df = loadCAPMF.getEU26()
    #df = loadCAPMF.getControl()


    panel_stringency = df.pivot_table(index=['Year', 'Country'], values='Stringency') #Just for control countries
   # panel_stringency = df.pivot_table(index=['Year'], values='Stringency', aggfunc=np.mean) #Just for EU because we aggregate the data


    #panel_stringency.insert(0,'Country', 'EU')

    print(panel_stringency)

    panel_stringency.to_csv("data/CAPMF/stringency/policyStringency/EUstatesPolicyStringency.csv", index=True)



#used to get the panel data for climate policy stringency for nonEU countries and for EU as a single unit.

def buildPanel_Control():
    df = loadCAPMF.getControl()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_Control = df.pivot_table(index=['Country', 'year'], columns='Policy', values='Stringency', aggfunc=np.mean)

    return panel_Control


