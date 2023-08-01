import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ImportData import getImport
import policy.loadPolicyAdoptionCAPMF
from policy import loadPolicyAdoptionCAPMF
from panels import controlsDataMerger
import seaborn as sns

def importVisualization(country):
    dfCountry = getImport.loadSingleImports(country).astype(float)
    dfEU26 = getImport.loadSingleImports('data/imports/EU/china/EU26_850650chUSD.csv').astype(float)

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, dfEU26['Value'], marker='o', linestyle='-', color='b',
             label="Import of HS850650 EU countries")
    plt.plot(dfCountry.index, dfCountry['Value'], marker='o', linestyle='-', color='r',
             label=" Import of HS850650 control country")

    plt.title("Import of HS850650 from china EU VS control country")
    plt.ylabel('HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

    ##########

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, np.log(dfEU26['Value']), marker='o', linestyle='-', color='b',
             label=" LOG Import of HS850650 EU countries")
    plt.plot(dfCountry.index, np.log(dfCountry['Value']), marker='o', linestyle='-', color='r',
             label=" LOG Import of HS850650 control countries")

    plt.title(
        "LOG Import of HS850650 EU VS control country (US, South-Korea, Canada)")
    plt.ylabel('HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

def ImportCommonTrendVisualization():
    dfControl = controlsDataMerger.ControlImportMerger()
    dfEU26= getImport.loadSingleImports('data/imports/EU/china/EU26_850650chUSD.csv')

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, dfEU26['Value'], marker='o', linestyle='-', color='b',
             label=" Import of HS850650 - EU countries")
    plt.plot(dfControl.index, dfControl['Value'], marker='o', linestyle='-', color='r',
             label=" Import of HS850650 - control OECD")

    plt.title(
        "Import of Lithium cells and batteries HS850650 from China - EU VS control OECD (US, South-Korea, Canada, Japan, South Africa, Brazil, Australia)")
    plt.ylabel('HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

####
    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, np.log(dfEU26['Value']), marker='o', linestyle='-', color='b', label=" Log of import of Lithium cells and batteries - EU countries")
    plt.plot(dfControl.index, np.log(dfControl['Value']), marker='o', linestyle='-', color='r', label=" Log of Import of  Lithium cells and batteries - control countries")

    plt.title("Log of import of Lithium cells and batteries HS850650 from China - EU VS control OECD (US, South-Korea, Canada, Japan, South Africa, Brazil, Australia)")
    plt.ylabel('Log of HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()


####
    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, (np.log(dfEU26['Value'])- np.log(dfControl['Value'])), marker='o', linestyle='-', color='b', label=" Difference in Log of import of Lithium cells and batteries EU - Control")

    plt.title("Difference in Log of import of Lithium cells and batteries HS850650 from China - EU VS control OECD (US, South-Korea, Canada, Japan, South Africa, Brazil, Australia)")
    plt.ylabel('Difference in Log of HS850650 imports: Log EU - Log OECD')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

   # plt.xticks(df.index.get_level_values(0), rotation=45)  # access only first level of the MultiIndex pivot table, i.e. the Years

def RatioControlCommonTrendVisualization():
    dfControl = controlsDataMerger.ControlRatioMerger().astype(float)
    dfEU26= getImport.loadImportRatio('data/imports/EU/ratio/EUratio850650.csv').astype(float)

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, dfEU26['import_ratio'], marker='o', linestyle='-', color='b',
             label="Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - EU ")
    plt.plot(dfControl.index, dfControl['import_ratio'], marker='o', linestyle='-', color='r',
             label="Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - Control countries  ")

    plt.title("Chinese imports over total imports for Lithium cells and batteries - EU VS Control (US, South-Korea, Canada)")
    plt.ylabel('Ratio China/Total imports for Lithium cells and batteries')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

    ##########

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, np.log(dfEU26['import_ratio']), marker='o', linestyle='-', color='b', label="Log of the ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - EU")
    plt.plot(dfControl.index, np.log(dfControl['import_ratio']), marker='o', linestyle='-', color='r', label="Log og the ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - Control countries")

    plt.title("Log of chinese imports over total imports for Lithium cells and batteries - EU VS Control: US, South-Korea, Canada")
    plt.ylabel('Log of ratio China/Total imports for Lithium cells and batteries')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

    #####

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, (np.log(dfEU26['import_ratio'])-np.log(dfControl['import_ratio'])), marker='o', linestyle='-', color='b', label="Difference in Log of the ratios")

    plt.title("Difference in Log of the ratios of chinese imports over total imports for Lithium cells and batteries: Log EU - Log Control")
    plt.ylabel('Difference in Log of ratio China/Total imports for Lithium cells and batteries: LogEU - LogControl')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()


def RatioCommonTrendVisualization(country):
    dfCountry= getImport.loadImportRatio(country).astype(float)
    dfEU26= getImport.loadImportRatio('data/imports/EU/ratio/EUratio850650.csv').astype(float)

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, dfEU26['import_ratio'], marker='o', linestyle='-', color='b',
             label=" Import of HS850650 EU countries")
    plt.plot(dfCountry.index, dfCountry['import_ratio'], marker='o', linestyle='-', color='r',
             label=" Import of HS850650 control country")

    plt.title(
        "Import of HS850650 EU VS control country")
    plt.ylabel('HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()

    ##########

    plt.figure(figsize=(14, 8))

    plt.plot(dfEU26.index, np.log(dfEU26['import_ratio']), marker='o', linestyle='-', color='b', label=" LOG Import of HS850650 EU countries")
    plt.plot(dfCountry.index, np.log(dfCountry['import_ratio']), marker='o', linestyle='-', color='r', label=" LOG Import of HS850650 control countries")

    plt.title("LOG Import of HS850650 EU VS control country (US, South-Korea, Canada)")
    plt.ylabel('HS850650 import')
    plt.xlabel('Year')
    plt.xticks(dfEU26.index, rotation=45)
    plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.show()




