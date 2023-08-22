import pandas as pd

def loadSingleImports(dataImportCountry_HScsv):
    df = pd.read_csv(dataImportCountry_HScsv, delimiter=';', thousands=".", decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    #df=df.pivot_table(index=["Year"], values=["Value"]) #values=["Value", "Weight"]

    return df

def loadAllImports():
    df = pd.read_csv('data/imports/Israel/china/isch19.csv', delimiter=';', thousands=".", decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    #pivot table with HSCode and all the years, HSCode and all the years etc...
    df=df.pivot_table(index=["HScode","Year"], values=["Value"]) #values=["Value", "Weight"]

    #get a tuple with HScode as key

    grouped = df.groupby('HScode') #this is a tuple

    df_dictionary = {}

    for hs, Importvalue in grouped: #iterate through the tuple. hs gets the key, Importvalue gets the values
        df_dictionary[hs] = Importvalue.copy()

    df850511 = df_dictionary[850511]
    df850511.to_csv('data/imports/Israel/china/ISL_850511ch.csv')

    df854140 = df_dictionary[850650]
    df854140.to_csv('data/imports/Israel/china/ISL_850650ch.csv')

def loadAllCountryAllImports():
    df = pd.read_csv('data/lithium19ch.csv', delimiter=';', decimal=',')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    grouped=df.groupby(['Country', 'HScode'])

    result_dataframes = {}

    # basically every iteration select country-hscode pair and takes all the values.
    for (country, hscode), group_df in grouped:
        if (country, hscode) not in result_dataframes:
            result_dataframes[(country, hscode)] = group_df.drop(['Country', 'HScode'], axis=1)
        else:
            result_dataframes[(country, hscode)] = pd.concat([result_dataframes[(country, hscode)], group_df.drop(['Country', 'HScode'], axis=1)])

    for (country, hscode), df in result_dataframes.items():
        # Create a filename based on country and hscode
        filename = f"{country}_{hscode}ch.csv"

        # Save the DataFrame to a CSV file
        df.to_csv("data/"+filename, index=True)
        print(f"File {filename} created.")

def loadImportRatio(RatioCountrycsv):
    df = pd.read_csv(RatioCountrycsv, delimiter=';', decimal=',')
    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    #df = df.pivot_table(index=["Year"],  columns='State', values=["import_ratio"])  # values=["Value", "Weight"]

    return df

