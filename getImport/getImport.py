import pandas as pd


def loadImports():
    df=pd.read_csv("data/imports/EU/EU26_280530.csv",delimiter=";",decimal=".")

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    df=df.pivot_table(index=["Year", "Product"], values="Euro_value")

    return df


"""
def loadQty():
    df=pd.read_excel("data/imports/test1990to2021.xlsx", decimal=".")

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df=df.pivot_table(values="Qty", index="Year", columns=["Country"])

    print(df)

    return df
""" #load quantity
