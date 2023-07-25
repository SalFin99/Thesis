import matplotlib.pyplot as plt
import numpy as np
from ImportData import getImport
import getPolicies.loadPolicyAdoptionCAPMF
from getPolicies import loadPolicyAdoptionCAPMF
import seaborn as sns

def importVisualization():
    df = getImport.loadImports('data/imports/Brazil/BRA_850231.csv')

    Logdf = np.log(df)

    plt.figure(figsize=(14, 8))

    sns.set_style("darkgrid")

    """
        sns.lineplot(data=df, x='Year', y="Weight")
        sns.lineplot(data=df, x='Year', y="Value")
    """

    sns.lineplot(data=df, x='Year', y="Value")

    plt.xticks(df.index.get_level_values(0), rotation=45)  #access only first level of the MultiIndex pivot table, i.e. the Years

    """
        plt.title("EU import value for HS-XXXXXX")
        plt.title("EU import weight (in KG) for HS-XXXXXX")

        plt.title("Canada import value HS-XXXXXX")
        plt.title("Canada import weight (in KG) for HS-XXXXXX")
        
        plt.title("Japan import value for HS-XXXXXX")
        plt.title("Japan import weight for HS-XXXXXX")
        
        plt.title("South Korea import value for HS-XXXXXX")
        plt.title("South Korea import weight for HS-XXXXXX")
        
        plt.title("US import value for HS-XXXXXX")
        plt.title("US import weight for HS-XXXXXX")
        
        plt.title("Brazil import value for HS-XXXXXX")
        plt.title("Brazil import weight for HS-XXXXXX")
    """

    plt.title("Brazil import value for HS-850231")

    plt.show()


    plt.figure(figsize=(14, 8))

    sns.set_style("darkgrid")

    """
        sns.lineplot(data=df, x='Year', y="Weight")
        sns.lineplot(data=df, x='Year', y="Value")

    """

    sns.lineplot(data=Logdf, x='Year', y="Value")

    """
        plt.title("EU log of import value HS-XXXXXX")
        plt.title("EU log of import weight (in KG) for HS-XXXXXX")
        
        plt.title("CANADA log of import value HS-XXXXXX")
        plt.title("Canada log of import weight (in Kg) for HS-XXXXXX")
        
        plt.title("Japan log of import value HS-XXXXXX")
        plt.title("Japan log of import weight (in Kg) for HS-XXXXXX")
        
        plt.title("South Korea log of import value for HS-XXXXXX")
        plt.title("South Korea log of weight (in Kg) for HS-XXXXXX")
        
        plt.title("US log of import value for HS-XXXXXX")
        plt.title("US log of weight (in Kg) for HS-XXXXXX")


    """
    plt.title("Brazil log of import value for HS-850231")

    plt.xticks(df.index.get_level_values(0), rotation=45)  #access only first level of the MultiIndex pivot table, i.e. the Years

    plt.show()





def adoptionVisualization():

    df = loadPolicyAdoptionCAPMF.getAdoption()

    plt.figure(figsize=(14, 8))
    plt.plot(df.index, df['EUadopted'])
    plt.title("Number of EU adopted policies 2000-2019")
    plt.xticks(df.index, rotation=45)  # Rotate x-axis tick labels for better readability
    plt.axvline(x=2009,color='g') #set vertical line on 2009 for policy introduction (the treatment)
    plt.ylabel('Number of policies')
    plt.xlabel('Years')



    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()  # To avoid label cutoff
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


