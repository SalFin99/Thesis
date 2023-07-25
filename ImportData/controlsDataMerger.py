from ImportData import getImport
import pandas as pd

def importDataMerger():

    dfBra = getImport.loadImports('data/imports/Brazil/BRA_280530.csv')

    dfCan = getImport.loadImports('data/imports/canada/CAN_280530.csv')

    dfJap = getImport.loadImports('data/imports/japan/JAP_280530.csv')

    dfKor = getImport.loadImports('data/imports/SouthKorea/KOR_280530.csv')

    dfUs = getImport.loadImports('data/imports/USA/US_280530.csv')

    dfControl = pd.concat([dfUs,dfKor,dfJap,dfBra,dfCan], join="inner")
    dfControl.to_csv("data/imports/concat.csv", index=True)

    ControlImportPanel=dfControl.pivot_table(index='Year', values='Value', aggfunc='sum')

    ControlImportPanel.to_csv("data/imports/Panel.csv", index=True)
    print(ControlImportPanel)

""""
For tomorrow: 
- generate all dfControls for all the materials
- create pivot

"""

