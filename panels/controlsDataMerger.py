import numpy as np

from ImportData import getImport
import pandas as pd

def ControlImportMerger():
    dfBra = getImport.loadSingleImports('data/imports/Brazil/china/BRA_850650ch.csv')

    dfCan = getImport.loadSingleImports('data/imports/canada/china/CAN_850650ch.csv')

    dfJap = getImport.loadSingleImports('data/imports/japan/China/JAP_850650ch.csv')

    dfKor = getImport.loadSingleImports('data/imports/SouthKorea/china/KOR_850650ch.csv')

    dfUs = getImport.loadSingleImports('data/imports/USA/china/USA_850650ch.csv')

    dfAus = getImport.loadSingleImports('data/imports/Australia/china/AUS_850650ch.csv')

    dfZaf = getImport.loadSingleImports('data/imports/SouthAfrica/china/ZAF_850650ch.csv')

    dfControl = pd.concat([dfKor, dfZaf, dfAus, dfBra, dfJap, dfUs, dfCan], join="inner")

    # dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlImportPanel = dfControl.pivot_table(index='Year', values='Value', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return ControlImportPanel


def ControlRatioMerger():
    #dfBra = getImport.loadImportRatio('data/imports/Brazil/china/BRA_850650ch.csv')

    dfCan = getImport.loadImportRatio('data/imports/canada/ratio/CANratio850650.csv')

    #dfJap = getImport.loadImportRatio('data/imports/japan/China/JAP_850650ch.csv')

    dfKor = getImport.loadImportRatio('data/imports/SouthKorea/ratio/KORratio850650.csv')

    dfUs = getImport.loadImportRatio('data/imports/USA/ratio/USAratio850650.csv')

    #dfAus = getImport.loadImportRatio('data/imports/Australia/china/AUS_850650ch.csv')

    #dfZaf = getImport.loadImportRatio('data/imports/SouthAfrica/china/ZAF_850650ch.csv')

    dfControl = pd.concat([dfKor, dfUs,dfCan], join="inner")

    # dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlRatioPanel = dfControl.pivot_table(index='Year', values='import_ratio', aggfunc=np.mean)

    # ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)

    return ControlRatioPanel


