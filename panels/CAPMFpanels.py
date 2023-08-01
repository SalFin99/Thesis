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


def buildPanel_EU():
    df = loadCAPMF.getEU()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_EU = df.pivot_table(index=['Country', 'year'], columns='Policy', values='Stringency')

    #df.to_csv("data/CAPMF/panels/EU_panel.csv", index=False)


    return panel_EU

def buildPanel_EU26():
    df = loadCAPMF.getEU26()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_EU26 = df.pivot_table(index=['Country', 'year'], columns='Policy', values='Stringency', aggfunc=np.mean)


    #df.to_csv("data/CAPMF/panels/EU26_panel.csv", index=False)

    return panel_EU26

def buildPanel_NonEU():
    df = loadCAPMF.getNonEU()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_NonEU26 = df.pivot_table(index=['Country', 'year'], columns='Policy', values='Stringency')

    #df.to_csv("data/CAPMF/panels/NonEU26_panel.csv", index=False)

    return panel_NonEU26

def buildPanel_Control():
    df = loadCAPMF.getControl()

    panel_NonEU26 = df.pivot_table(index=['Country', 'year'], columns='Policy', values='Stringency')

    #df.to_csv("data/CAPMF/panels/NonEU26_panel.csv", index=False)

    return panel_NonEU26

