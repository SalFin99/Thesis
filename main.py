import loadData
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


epsControl=loadData.load_and_cleanEPScontrol() #esi: load Environmental Policy Stringency index (EPS)
epsEU=loadData.load_and_cleanEPStreatment() #esi: load Environmental Policy Stringency index (EPS)
"""
epsControl['EPSvalue'].mean(axis=1).plot(label='Control: US, Canada, South Korea, Japan')
epsEU['EPSvalue'].mean(axis=1).plot(label='EU')

plt.title('Average Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()
"""

epsControl['logEPS'].mean(axis=1).plot(label='Control: US, Canada, South Korea, Japan')
epsEU['logEPS'].mean(axis=1).plot(label='EU')

plt.title('Average log Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()





"""
epsEU.mean(axis=1).plot()
plt.title('Average Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.show()
"""



""""
imp = loadData.loadImports()



imp.mean(axis=1).plot()
plt.title('Average import of rare earths')
plt.ylabel('Import value')
plt.xlabel('Year')
plt.show()



qty=loadData.loadQty()

qty.mean(axis=1).plot()
plt.title('Average import weight of rare earths')
plt.ylabel('Weight in Kg')
plt.xlabel('Year')
plt.show()
"""
