import matplotlib.pyplot as plt
from getPolicies import getPolicyAdoption


def adoptionVisualization():

    df = getPolicyAdoption.getAdoption()

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['EUadopted'])
    plt.title("Number of EU adopted policies 2000-2019")
    plt.xticks(df.index, rotation=45)  # Rotate x-axis tick labels for better readability
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.ylabel('Number of policies')
    plt.xlabel('Years')



    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()


def showTrend_Magnets_Japan():
    imports = getRE_Japan()

    plt.figure(figsize=(20, 20))
    #plt.plot(imports.index, imports['NetWgt'], label='NetWgt')
    plt.plot(imports.index, imports['PrimaryValue'], label='PrimaryValue')

    plt.xlabel('Period')
    plt.ylabel('Values')
    plt.title('NetWgt and PrimaryValue')

    plt.legend()
    plt.show()


def showTrend_RE_Japan():
    imports = getRE_Japan()

    plt.figure(figsize=(14, 10))
    plt.plot(imports.index, imports['NetWgt'], label='NetWgt')
    plt.plot(imports.index, imports['PrimaryValue'], label='PrimaryValue')

    plt.xlabel('Period')
    plt.ylabel('Values')
    plt.title('NetWgt and PrimaryValue')
    plt.legend()
    plt.show()


"""

    # Use seaborn style defaults and set the default figure size
    sns.lineplot(data=imports[['PrimaryValue']], dashes=False)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Import rare earths (HS280530)')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)
        plt.show()
"""

"""
#no need for all these functions, just rewrite one and pass paths
epsControl=loadData.load_and_cleanEPScontrol() #esi: load Environmental Policy Stringency index (EPS)
epsEU=loadData.load_and_cleanEPStreatment() #esi: load Environmental Policy Stringency index (EPS)

epsControl['EPSvalue'].mean(axis=1).plot(label='Control: US, Canada, South Korea, Japan')
epsEU['EPSvalue'].mean(axis=1).plot(label='EU')

plt.title('Average Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()


epsControl['logEPS'].mean(axis=1).plot(label='Control: US, Canada, South Korea, Japan')
epsEU['logEPS'].mean(axis=1).plot(label='EU')

plt.title('Average log Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()






epsEU.mean(axis=1).plot()
plt.title('Average Environmental Policy Stringency index 1990 - 2020')
plt.ylabel('EPS index')
plt.xlabel('Year')
plt.show()


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


