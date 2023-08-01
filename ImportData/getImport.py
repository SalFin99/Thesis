import pandas as pd



"""
    - FOR EU: 
        df=pd.read_csv("data/imports/EU/DATA.csv",delimiter=";",thousands=".")
        
    - FOR CANADA:
        df=pd.read_csv('data/imports/canada/FILE.csv', delimiter=';', thousands=".", decimal=',')
        
    - FOR JAPAN:
        df = pd.read_csv('data/imports/japan/FILE.csv', delimiter=';', thousands=".", decimal=',')

    - FOR US:
        df = pd.read_csv('data/imports/USA/FILE.csv', delimiter=';', thousands=".", decimal=',')
    
    - FOR BRAZIL:
        df = pd.read_csv('data/imports/Brazil/FILE.csv', delimiter=';', thousands=".", decimal=',')

"""
def loadSingleImports(dataImportCountry_HScsv):
    df = pd.read_csv(dataImportCountry_HScsv, delimiter=';', thousands=".", decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    df=df.pivot_table(index=["Year"], values=["Value"]) #values=["Value", "Weight"]

    return df

def loadImportRatio(RatioCountrycsv):
    df = pd.read_csv(RatioCountrycsv, delimiter=';', decimal=',')
    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    df = df.pivot_table(index=["Year"], values=["import_ratio"])  # values=["Value", "Weight"]

    return df

def loadAllImports():
    df = pd.read_csv('data/imports/EU/EU_UN.csv', delimiter=';', thousands=".", decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    df=df.pivot_table(index=["HScode","Year"], values=["Value"]) #values=["Value", "Weight"]

    grouped = df.groupby('HScode') #this is a tuple

    df_dictionary = {}

    for hs, group in grouped: #iterate through the tuple. hs gets the key, group gets the values
        df_dictionary[hs] = group.copy()

    df850231 = df_dictionary[850231]
    df850231.to_csv('data/imports/EU/EU_850231UN.csv')

    df280530 = df_dictionary[280530]
    df280530.to_csv('data/imports/EU/EU_280530UN.csv')

    df850511 = df_dictionary[850511]
    df850511.to_csv('data/imports/EU/EU_850511UN.csv')

    df854140 = df_dictionary[854140]
    df854140.to_csv('data/imports/EU/EU_854140UN.csv')
