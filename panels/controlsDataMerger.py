import numpy as np

from Import import getImport
import pandas as pd

def ControlImportMerger():
    dfBra = getImport.loadSingleImports('data/imports/Brazil/china/BRA_850511ch.csv')

    dfCan = getImport.loadSingleImports('data/imports/Canada/china/CAN_850511ch.csv')

    dfJap = getImport.loadSingleImports('data/imports/Japan/china/JAP_850511ch.csv')

    dfKor = getImport.loadSingleImports('data/imports/SouthKorea/china/KOR_850511ch.csv')

    dfUs = getImport.loadSingleImports('data/imports/USA/china/USA_850511ch.csv')

    dfAus = getImport.loadSingleImports('data/imports/Australia/china/AUS_850511ch.csv')

    #dfChe = getImport.loadSingleImports('data/imports/Switzerland/china/CHE_850511ch.csv') #da rifare

    dfIsl = getImport.loadSingleImports('data/imports/Israel/china/ISL_850511ch.csv')

    dfNor = getImport.loadSingleImports('data/imports/Norway/china/NOR_850511ch.csv')

    dfTur = getImport.loadSingleImports('data/imports/Turkey/china/TUR_850511ch.csv')

    dfNzl = getImport.loadSingleImports('data/imports/NewZeland/china/NZL_850511ch.csv')

    dfMex = getImport.loadSingleImports('data/imports/Mexico/china/MEX_850511ch.csv')

    dfChl = getImport.loadSingleImports('data/imports/Chile/china/CHL_850511ch.csv')

    dfZaf = getImport.loadSingleImports('data/imports/SouthAfrica/china/ZAF_850511ch.csv')

    dfControl = pd.concat([dfKor, dfUs, dfBra, dfJap,dfZaf,dfIsl], join="inner")

    #dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlImportPanel = dfControl.pivot_table(index='Year', values='Value', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return ControlImportPanel


def ControlRatioMerger():
    #dfBra = getImport.loadImportRatio('data/imports/Brazil/china/BRA_850511ch.csv')

    dfCan = getImport.loadImportRatio('data/imports/canada/ratio/CANratio850511.csv')

    #dfJap = getImport.loadImportRatio('data/imports/japan/China/JAP_850511ch.csv')

    dfKor = getImport.loadImportRatio('data/imports/SouthKorea/ratio/KORratio850511.csv')

    dfUs = getImport.loadImportRatio('data/imports/USA/ratio/USAratio850511.csv')

    #dfAus = getImport.loadImportRatio('data/imports/Australia/china/AUS_850511ch.csv')

    #dfZaf = getImport.loadImportRatio('data/imports/SouthAfrica/china/ZAF_850511ch.csv')

    dfControl = pd.concat([dfKor,dfUs,dfCan], join="inner")

    # dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlRatioPanel = dfControl.pivot_table(index='Year', values='import_ratio', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return ControlRatioPanel

def RatioPanel():

    dfEU26= getImport.loadImportRatio('data/imports/EU/newUSD/EUratio850511new.csv')

    dfBra = getImport.loadImportRatio('data/imports/Brazil/ratio/BRAratio850511.csv')

    dfCan = getImport.loadImportRatio('data/imports/Canada/ratio/CANratio850511.csv')

    dfJap = getImport.loadImportRatio('data/imports/Japan/ratio/JAPratio850511.csv')

    dfKor = getImport.loadImportRatio('data/imports/SouthKorea/ratio/KORratio850511.csv')

    dfUs = getImport.loadImportRatio('data/imports/USA/ratio/USAratio850511.csv')

    dfAus = getImport.loadImportRatio('data/imports/Australia/ratio/AUSratio850511.csv')

    dfZaf = getImport.loadImportRatio('data/imports/SouthAfrica/ratio/ZAFratio850511.csv')

    dfChe = getImport.loadImportRatio('data/imports/Switzerland/ratio/CHEratio850511.csv')

    dfIsl = getImport.loadImportRatio('data/imports/Israel/ratio/ISLratio850511.csv')

    dfNor = getImport.loadImportRatio('data/imports/Norway/ratio/NORratio850511.csv')

    dfTur = getImport.loadImportRatio('data/imports/Turkey/ratio/TURratio850511.csv')

    dfNzl = getImport.loadImportRatio('data/imports/NewZeland/ratio/NZLratio850511.csv')

    dfMex = getImport.loadImportRatio('data/imports/Mexico/ratio/MEXratio850511.csv')

    dfChl = getImport.loadImportRatio('data/imports/Chile/ratio/CHLratio850511.csv')

    #ALL: dfEU26, dfBra, dfJap, dfIsl, dfAus, dfZaf, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan

    dfControl = pd.concat([dfEU26,  dfZaf, dfUs, dfCan])


    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return dfControl

def ImportPanel():

    dfEU26= getImport.loadImportRatio('data/imports/EU/China/.....')

    dfBra = getImport.loadSingleImports('data/imports/Brazil/china/BRA_850511ch.csv')

    dfCan = getImport.loadSingleImports('data/imports/Canada/china/CAN_850511ch.csv')

    dfJap = getImport.loadSingleImports('data/imports/Japan/china/JAP_850511ch.csv')

    dfKor = getImport.loadSingleImports('data/imports/SouthKorea/china/KOR_850511ch.csv')

    dfUs = getImport.loadSingleImports('data/imports/USA/china/USA_850511ch.csv')

    dfAus = getImport.loadSingleImports('data/imports/Australia/china/AUS_850511ch.csv')

    # dfChe = getImport.loadSingleImports('data/imports/Switzerland/china/CHE_850511ch.csv') #da rifare

    dfIsl = getImport.loadSingleImports('data/imports/Israel/china/ISL_850511ch.csv')

    dfNor = getImport.loadSingleImports('data/imports/Norway/china/NOR_850511ch.csv')

    dfTur = getImport.loadSingleImports('data/imports/Turkey/china/TUR_850511ch.csv')

    dfNzl = getImport.loadSingleImports('data/imports/NewZeland/china/NZL_850511ch.csv')

    dfMex = getImport.loadSingleImports('data/imports/Mexico/china/MEX_850511ch.csv')

    dfChl = getImport.loadSingleImports('data/imports/Chile/china/CHL_850511ch.csv')

    dfZaf = getImport.loadSingleImports('data/imports/SouthAfrica/china/ZAF_850511ch.csv')

    #ALL: dfBra, dfJap, dfAus, dfZaf, dfChe, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan

    dfControl = pd.concat([dfEU26, dfBra, dfJap, dfIsl, dfAus, dfZaf, dfNor, dfTur, dfNzl, dfMex, dfChl, dfKor, dfUs, dfCan])

    #ControlImportPanel = dfControl.pivot_table(index='State', columns='Year', values='Value')

    return dfControl




