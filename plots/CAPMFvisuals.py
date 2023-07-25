import numpy as np

from panels import CAPMFpanels
import matplotlib.pyplot as plt


def preCommonTrendsStringency():
    EU26 = CAPMFpanels.buildPanel_EU26()
    nonEU = CAPMFpanels.buildPanel_NonEU()


    average_stringencyEU26 = EU26.mean(axis=1).groupby('year').mean()
    average_stringencyNonEU26 = nonEU.mean(axis=1).groupby('year').mean()


    yearsEU26 = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesEU26 = average_stringencyEU26.values

    yearsNonEU = average_stringencyEU26.index.get_level_values('year')

    average_stringency_valuesNonEU26 = average_stringencyNonEU26.values

    plt.figure(figsize=(14, 8))

    plt.plot(yearsEU26.astype(int), average_stringency_valuesEU26, marker='o', linestyle='-', color='b', label="Average policy strincency for EU countries (Cyprus not included)")
    plt.plot(yearsNonEU.astype(int), average_stringency_valuesNonEU26, marker='o', linestyle='-', color='r', label="Average policy strincency for Non-EU OECD countries")

    plt.title("Climate policy stringency for EU and non-EU OECD countries")
    plt.ylabel('Climate policy stringency')
    plt.xlabel('Year')
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.xticks(yearsNonEU, rotation=45)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

def preCommonTrendsLogStringency():
    EU26 = CAPMFpanels.buildPanel_EU26()
    nonEU = CAPMFpanels.buildPanel_NonEU()


    average_stringencyEU26 = EU26.mean(axis=1).groupby('year').mean()
    average_stringencyNonEU26 = nonEU.mean(axis=1).groupby('year').mean()

    yearsEU26 = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesEU26 = average_stringencyEU26.values

    yearsNonEU = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesNonEU26 = average_stringencyNonEU26.values

    #take logs
    log_average_stringency_valuesEU26 = np.log(average_stringency_valuesEU26)
    log_average_stringency_valuesNonEU = np.log(average_stringency_valuesNonEU26)

    #print(log_average_stringency_valuesEU26)
    #print(log_average_stringency_valuesNonEU)
    #print(log_average_stringency_valuesEU26-log_average_stringency_valuesNonEU)

    plt.figure(figsize=(14, 8))

    plt.plot(yearsEU26, log_average_stringency_valuesEU26, marker='o', linestyle='-', color='b', label="Average policy strincency for EU countries (Cyprus not included)")
    plt.plot(yearsNonEU, log_average_stringency_valuesNonEU, marker='o', linestyle='-', color='r', label="Average policy strincency for  Non-EU OECD countries")

    plt.title("Log of climate policy stringency for EU and non-EU OECD countries")
    plt.ylabel("Log of climate policy stringency")
    plt.xlabel('Year')
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.xticks(yearsNonEU, rotation=45)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()


def preCommonTrendsStringencyControl():
    EU26 = CAPMFpanels.buildPanel_EU26()
    control = CAPMFpanels.buildPanel_NonEU()


    average_stringencyEU26 = EU26.mean(axis=1).groupby('year').mean()
    average_stringencyControl = control.mean(axis=1).groupby('year').mean()


    yearsEU26 = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesEU26 = average_stringencyEU26.values

    yearsControl = average_stringencyEU26.index.get_level_values('year')

    average_stringency_valuesControl = average_stringencyControl.values

    plt.figure(figsize=(14, 8))

    plt.plot(yearsEU26.astype(int), average_stringency_valuesEU26, marker='o', linestyle='-', color='b', label="Average policy strincency for EU countries (Cyprus not included)")
    plt.plot(yearsControl.astype(int), average_stringency_valuesControl, marker='o', linestyle='-', color='r', label="Average policy strincency for Control OECD countries")

    plt.title("Climate policy stringency for EU and control OECD countries (Japan, USA, Brazil, South-Korea, Canada)")
    plt.ylabel('Climate policy stringency')
    plt.xlabel('Year')
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.xticks(yearsControl, rotation=45)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

def preCommonTrendsLogStringencyControl():
    EU26 = CAPMFpanels.buildPanel_EU26()
    control = CAPMFpanels.buildPanel_NonEU()


    average_stringencyEU26 = EU26.mean(axis=1).groupby('year').mean()
    average_stringencyControl = control.mean(axis=1).groupby('year').mean()

    yearsEU26 = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesEU26 = average_stringencyEU26.values

    yearsControl = average_stringencyEU26.index.get_level_values('year')
    average_stringency_valuesControl = average_stringencyControl.values

    #take logs
    log_average_stringency_valuesEU26 = np.log(average_stringency_valuesEU26)
    log_average_stringency_valuesControl = np.log(average_stringency_valuesControl)

    #print(log_average_stringency_valuesEU26)
    #print(log_average_stringency_valuesNonEU)
    #print(log_average_stringency_valuesEU26-log_average_stringency_valuesNonEU)

    plt.figure(figsize=(14, 8))

    plt.plot(yearsEU26, log_average_stringency_valuesEU26, marker='o', linestyle='-', color='b', label="Average policy strincency for EU countries (Cyprus not included)")
    plt.plot(yearsControl, log_average_stringency_valuesControl, marker='o', linestyle='-', color='r', label="Average policy strincency for  Control OECD countries")

    plt.title("Log of climate policy stringency for EU and control OECD countries (Japan, USA, Brazil, South-Korea, Canada)")
    plt.ylabel("Log of climate policy stringency")
    plt.xlabel('Year')
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.xticks(yearsControl, rotation=45)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()