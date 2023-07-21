from getPolicies import loadCAPMF, loadEPS
import numpy as np
import pandas as pd

def buildPanel_EU():
    df = loadCAPMF.getEU()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_EU = df.pivot(index=['Country', 'year'], columns='Policy', values='Stringency')

    #df.to_csv("data/CAPMF/panels/EU_panel.csv", index=False)


    return panel_EU

def buildPanel_EU26():
    df = loadCAPMF.getEU26()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_EU26 = df.pivot(index=['Country', 'year'], columns='Policy', values='Stringency')

    df.to_csv("data/CAPMF/panels/EU26_panel.csv", index=False)

    return panel_EU26

def buildPanel_NonEU():
    df = loadCAPMF.getNonEU()

    df.year=pd.to_datetime(df['year'], format='%Y').dt.year

    panel_NonEU26 = df.pivot(index=['Country', 'year'], columns='Policy', values='Stringency')

    df.to_csv("data/CAPMF/panels/NonEU26_panel.csv", index=False)

    return panel_NonEU26

