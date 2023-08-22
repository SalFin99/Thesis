from panels import controlsDataMerger, CAPMFpanels
from plots import importPlot, policy_importPlot
from Import import getImport, EURtoUSD, formatUS, importRatio
import os
from sklearn.linear_model import Lasso, Ridge
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from SyntheticControl import getWeights



"""
total = getImport.loadSingleImports('data/imports/EU/newUSD/EU26_850650USDnew.csv')
china = getImport.loadSingleImports('data/imports/EU/newUSD/EU26_850650chUSDnew.csv')

ratio=importRatio.calculate_import_ratio(total,china)

ratio.to_csv('data/imports/EU/newUSD/EUratio850650new.csv', index=True)
"""

#importPlot.RatioControlCommonTrendVisualization()

#importPlot.RatioCommonTrendVisualization('data/imports/Israel/ratio/ISLratio850650.csv')

#importPlot.importVisualization('data/imports/EU/EU_280530UN.csv')


df_import = controlsDataMerger.RatioPanel() #load the whole ratio china/world panel data

df_import = df_import.pivot_table(index='State', columns='Year', values='import_ratio')

df_importT = df_import.transpose() #pivot table with y number of years as rows and n number of countries as column

df_importT = df_importT.iloc[0:10] #just pre-treatment period.

print(df_importT)

y = df_importT['EU26'].values #load import from just EU

x = df_importT.drop(columns='EU26').values #panel without the EU

#weights_lr = LinearRegression(fit_intercept=False).fit(x, y).coef_ #get the weights by minimizing the distance between the control countries and the EU based on their ratio

weights = getWeights.get_w(x,y)

print("Sum:", weights.sum())
print(weights, 4)

"""
The obtained weights show us how to build the synthetic control.

We will multiply the outcome of state 1, 2, 3, 4 etc respectively by -0.153 -0.024 -0.343  0.242 etc...

We can do this with a dot product between the matrix from the states in the pool and the weights.
"""


df_import = controlsDataMerger.RatioPanel() #load all panel again

df_import = df_import.pivot_table(index='Year', columns='State', values='import_ratio') #pivot table with y number of years as column and countries as rows

df_import = df_import.drop(columns='EU26') #remove EU because we are about to construct the syntethic EU now

synthEU = df_import.values.dot(weights) #this will contain the value of the syntethic EU

print(synthEU)

#print(df_import)

dfEU26 = getImport.loadImportRatio('data/imports/EU/newUSD/EUratio850511new.csv') #get just EU data


plt.figure(figsize=(14, 8))

plt.plot(dfEU26.index, dfEU26['import_ratio'].astype(float), marker='o', linestyle='-', color='b', label="Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - EU ")

plt.plot(dfEU26.index, synthEU, marker='o', linestyle='-', color='r', label="Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - Syntenthic Control")


plt.xlabel('Year')
plt.xticks(dfEU26.index, rotation=45)
plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()

##########


plt.figure(figsize=(14, 8))

plt.plot(dfEU26.index, np.log(dfEU26['import_ratio'].astype(float)), marker='v', linestyle='-', color='b', label=" log of Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - EU ")
plt.plot(dfEU26.index, np.log(synthEU.astype(float)), marker='o', linestyle='-', color='r', label="log of Ratio of chinese imports over total imports for Lithium cells and batteries (HS850650) - Syntenthic Control")

plt.title("Log of chinese imports over total imports for Lithium cells and batteries - EU VS Control: US, South-Korea, Canada")
plt.ylabel('Log of ratio china/Total imports for Lithium cells and batteries')
plt.xlabel('Year')
plt.xticks(dfEU26.index, rotation=45)
plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()

plt.figure(figsize=(14, 8))

plt.plot(dfEU26.index, (dfEU26['import_ratio'].astype(float))-synthEU.astype(float), marker='o', linestyle='-', color='b', label="Difference in Log of the ratios")

plt.title("Difference in the ratios of chinese imports over total imports for Lithium cells and batteries: Log EU - Log Control")
plt.ylabel('Difference in ratio china/Total imports for Lithium cells and batteries: LogEU - LogControl')
plt.xlabel('Year')
plt.xticks(dfEU26.index, rotation=45)
plt.axvline(x=2009, color='g')  # set vertical line on 2009 for policy introduction (the treatment)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()



