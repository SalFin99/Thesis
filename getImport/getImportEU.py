def loadImports():
    df=pd.read_excel("data/imports/eudata.xlsx", decimal=".")

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df=df.pivot_table(values="REPORTER", index="Year", columns=["REPORTER"])

    print(df)

    return df

def loadQty():
    df=pd.read_excel("data/imports/test1990to2021.xlsx", decimal=".")

    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year

    df=df.pivot_table(values="Qty", index="Year", columns=["Country"])

    print(df)

    return df