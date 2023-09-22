import numpy as np

from Import import getImport
import pandas as pd

def ControlImportMerger():
    #dfBra = getImport.loadSingleImports('data/imports/Brazil/china/BRA_850650ch.csv')

    #dfCan = getImport.loadSingleImports('data/imports/Canada/china/CAN_850650ch.csv')

    dfJap = getImport.loadSingleImports('data/imports/HS854140/JPN_854140.csv')

    #dfKor = getImport.loadSingleImports('data/imports/SouthKorea/china/KOR_850650ch.csv')

    dfUs = getImport.loadSingleImports('data/imports/HS854140/USA_854140.csv')

    dfAus = getImport.loadSingleImports('data/imports/HS854140/AUT_854140.csv')

    dfChe = getImport.loadSingleImports('data/imports/HS854140/CHE_854140.csv')

    #dfIsl = getImport.loadSingleImports('data/imports/Israel/china/ISL_850650ch.csv')

    dfNor = getImport.loadSingleImports('data/imports/HS854140/NOR_854140.csv')

    #dfTur = getImport.loadSingleImports('data/imports/Turkey/china/TUR_850650ch.csv')

    dfNzl = getImport.loadSingleImports('data/imports/HS854140/NZL_854140.csv')

    dfIta = getImport.loadSingleImports('data/imports/HS854140/ITA_854140.csv')

    dfPrt = getImport.loadSingleImports('data/imports/HS854140/PRT_854140.csv')

    dfSwe = getImport.loadSingleImports('data/imports/HS854140/SWE_854140.csv')

    dfFra = getImport.loadSingleImports('data/imports/HS854140/FRA_854140.csv')

    dfDeu = getImport.loadSingleImports('data/imports/HS854140/DEU_854140.csv')

    dfDnk = getImport.loadSingleImports('data/imports/HS854140/DNK_854140.csv')

    dfEsp = getImport.loadSingleImports('data/imports/HS854140/ESP_854140.csv')

    dfFin = getImport.loadSingleImports('data/imports/HS854140/FIN_854140.csv')

    #dfMex = getImport.loadSingleImports('data/imports/Mexico/china/MEX_850650ch.csv')

    #dfChl = getImport.loadSingleImports('data/imports/Chile/china/CHL_850650ch.csv')

    #dfZaf = getImport.loadSingleImports('data/imports/SouthAfrica/china/ZAF_850650ch.csv')

    dfControl = pd.concat([dfSwe], join="inner")

    #dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlImportPanel = dfControl.pivot_table(index='Year', values='import_china', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return ControlImportPanel

def ControlRatioMerger():
    dfBra = getImport.loadImportRatio('data/imports/HS854140/BRA_854140.csv')

    dfCan = getImport.loadImportRatio('data/imports/HS854140/CAN_854140.csv')

    dfJap = getImport.loadImportRatio('data/imports/HS854140/JPN_854140.csv')

    dfKor = getImport.loadImportRatio('data/imports/HS854140/KOR_854140.csv')

    dfUs = getImport.loadImportRatio('data/imports/HS854140/USA_854140.csv')

    dfAus = getImport.loadImportRatio('data/imports/HS854140/AUS_854140.csv')

    dfZaf = getImport.loadImportRatio('data/imports/HS854140/ZAF_854140.csv')

    #dfIsl = getImport.loadImportRatio('data/imports/HS854140/ISL_854140.csv')

    dfChe = getImport.loadImportRatio('data/imports/HS854140/CHE_854140.csv')

    dfNzl = getImport.loadImportRatio('data/imports/HS854140/NZL_854140.csv')

    dfChl = getImport.loadImportRatio('data/imports/HS854140/CHL_854140.csv')

    dfMex = getImport.loadImportRatio('data/imports/HS854140/MEX_854140.csv')

    dfNor = getImport.loadImportRatio('data/imports/HS854140/NOR_854140.csv')


 #dfChe, dfCan, dfIsl, dfJap -> che, isl, aus, bra, us
    #dfAus, dfChe, dfCan, dfIsl, dfJap, dfMex, dfTur, dfZaf
    dfControl = pd.concat([dfMex, dfJap, dfZaf, dfZaf], axis=0)

    #dfMex, dfZaf, dfKor, dfJap

   # dfControl['Logimport_ratio'] = np.log(dfControl['import_ratio'])

    #dfControl.to_csv("data/imports/PanelControl.csv", index=True)

    # dfControl.to_csv("data/imports/concat.csv", index=True)

    dfControl = dfControl.pivot_table(index='Year', values='import_ratio', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)


    return dfControl

def RatioMergerEU():
    #dfEur = getImport.loadImportRatio('data/imports/EU/ratio/EUratio850650.csv')

    dfAut = getImport.loadImportRatio('data/imports/HS854140/AUT_854140.csv')

    dfDeu = getImport.loadImportRatio('data/imports/HS854140/DEU_854140.csv')

    dfDnk = getImport.loadImportRatio('data/imports/HS854140/DNk_854140.csv')

    dfEsp = getImport.loadImportRatio('data/imports/HS854140/ESP_854140.csv')

    dfIrl= getImport.loadImportRatio('data/imports/HS854140/IRL_854140.csv')

    dfIta = getImport.loadImportRatio('data/imports/HS854140/ITA_854140.csv')

    dfPrt = getImport.loadImportRatio('data/imports/HS854140/PRT_854140.csv')

    dfSwe = getImport.loadImportRatio('data/imports/HS854140/SWE_854140.csv')

    dfFra = getImport.loadImportRatio('data/imports/HS854140/FRA_854140.csv')

    dfFin = getImport.loadImportRatio('data/imports/HS854140/FIN_854140.csv')

#dfDeu, dfDnk, dfSwe, dfIta, dfEsp

    dfEu = pd.concat([dfSwe], axis=0)

    #dfEu['Logimport_ratio'] = np.log(dfEu['import_ratio'])

    #dfEu.to_csv("data/imports/Panel.csv", index=True)

    dfEu = dfEu.pivot_table(index='Year', values='import_ratio', aggfunc=np.mean)

    #print(EuRatioPanel)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)
    return dfEu

def RatioPanel():

    dfEU26= getImport.loadImportRatio('data/imports/EU/EUratio850650UN.csv')

    dfBra = getImport.loadImportRatio('data/imports/Brazil/ratio/BRAratio850650.csv')

    dfCan = getImport.loadImportRatio('data/imports/Canada/ratio/CANratio850650.csv')

    dfJap = getImport.loadImportRatio('data/imports/Japan/ratio/JAPratio850650.csv')

    dfKor = getImport.loadImportRatio('data/imports/SouthKorea/ratio/KORratio850650.csv')

    dfUs = getImport.loadImportRatio('data/imports/USA/ratio/USAratio850650.csv')

    dfAus = getImport.loadImportRatio('data/imports/Australia/ratio/AUSratio850650.csv')

    dfZaf = getImport.loadImportRatio('data/imports/SouthAfrica/ratio/ZAFratio850650.csv')

    dfChe = getImport.loadImportRatio('data/imports/Switzerland/ratio/CHEratio850650.csv')

    #dfIsl = getImport.loadImportRatio('data/imports/Israel/ratio/ISRratio850650.csv')

    #dfNor = getImport.loadImportRatio('data/imports/Norway/ratio/NORratio850650.csv')

    dfTur = getImport.loadImportRatio('data/imports/Turkey/ratio/TURratio850650.csv')

    dfNzl = getImport.loadImportRatio('data/imports/NewZealand/ratio/NZLratio850650.csv')

    dfMex = getImport.loadImportRatio('data/imports/Mexico/ratio/MEXratio850650.csv')

    dfChl = getImport.loadImportRatio('data/imports/Chile/ratio/CHLratio850650.csv')

    #ALL: dfEU26, dfBra, dfJap, dfIsl, dfAus, dfZaf, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan

    dfControl = pd.concat([dfEU26, dfBra, dfJap, dfAus, dfZaf, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan])

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return dfControl

def ImportPanel():

    dfEU26= getImport.loadImportRatio('data/imports/EU/china/EU26_850650chUSD.csv')

    dfBra = getImport.loadSingleImports('data/imports/Brazil/china/BRA_850650ch.csv')

    dfCan = getImport.loadSingleImports('data/imports/Canada/china/CAN_850650ch.csv')

    dfJap = getImport.loadSingleImports('data/imports/Japan/china/JAP_850650ch.csv')

    dfKor = getImport.loadSingleImports('data/imports/SouthKorea/china/KOR_850650ch.csv')

    dfUs = getImport.loadSingleImports('data/imports/USA/china/USA_850650ch.csv')

    dfAus = getImport.loadSingleImports('data/imports/Australia/china/AUS_850650ch.csv')

    # dfChe = getImport.loadSingleImports('data/imports/Switzerland/china/CHE_850650ch.csv') #da rifare

    #dfIsl = getImport.loadSingleImports('data/imports/Israel/china/ISL_850650ch.csv')

    dfNor = getImport.loadSingleImports('data/imports/Norway/china/NOR_850650ch.csv')

    dfTur = getImport.loadSingleImports('data/imports/Turkey/china/TUR_850650ch.csv')

    dfNzl = getImport.loadSingleImports('data/imports/NewZealand/china/NZL_850650ch.csv')

    dfMex = getImport.loadSingleImports('data/imports/Mexico/china/MEX_850650ch.csv')

    dfChl = getImport.loadSingleImports('data/imports/Chile/china/CHL_850650ch.csv')

    dfZaf = getImport.loadSingleImports('data/imports/SouthAfrica/china/ZAF_850650ch.csv')

    #ALL: dfBra, dfJap, dfAus, dfZaf, dfChe, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan

    dfControl = pd.concat([dfEU26, dfBra, dfJap, dfAus, dfZaf, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan])

    #ControlImportPanel = dfControl.pivot_table(index='State', columns='Year', values='Value')

    return dfControl




