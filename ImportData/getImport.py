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
def loadImports(dataImportCountry_HScsv):
    df = pd.read_csv(dataImportCountry_HScsv, delimiter=';', thousands=".", decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    df=df.pivot_table(index=["Year"], values=["Value"]) #values=["Value", "Weight"]

    return df


"""
def loadQty():
    df=pd.read_excel("data/imports/test1990to2021.xlsx", decimal=".")

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df=df.pivot_table(values="Qty", index="Year", columns=["Country"])

    print(df)

    return df
""" #load quantity
