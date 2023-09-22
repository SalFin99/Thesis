import pandas as pd

def loadSingleImports(dataImportCountry_HScsv):
    df = pd.read_csv(dataImportCountry_HScsv, delimiter=',', decimal='.')
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

def loadAllCountryRatios():
    df = pd.read_csv('data/imports/HS854140/854140NoTur.csv', delimiter=',', decimal='.')
    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    df = df.pivot_table(index=["country", "Year"], values=['import_china', 'import_total', 'import_ratio',
                                                           'ln_importratio'])  # values=["Value", "Weight"]

    grouped = df.groupby('country')  # this is a tuple

    df_dictionary = {}

    for country, columns in grouped:  # iterate through the tuple. hs gets the key, Importvalue gets the values
        df_dictionary[country] = columns.copy()

    print(df_dictionary)

    for country, df in df_dictionary.items():
        # Create a filename based on country and hscode
        filename = f"{country}_{'854140'}.csv"

        # Save the DataFrame to a CSV file
        df.to_csv("data/imports/HS854140/"+filename, index=True)
        print(f"File {filename} created.")



def loadAllCountryAllImports():
    df = pd.read_csv('data/imports/HS854140/854140NoTur.csv', delimiter=',', decimal='.')
    df.Year=pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)

    df=df.pivot_table(index=["country","Year"], values=['import_china','import_total','import_ratio','ln_importratio']) #values=["Value", "Weight"]

    grouped = df.groupby('HScode') #this is a tuple

    result_dataframes = {}

    # basically every iteration select country-hscode pair and takes all the values.
    for country in grouped:
        if country not in result_dataframes:
            result_dataframes[country]
        else:
            result_dataframes[country] = pd.concat(result_dataframes[country], axis=1)

    for country, df in result_dataframes.items():
        # Create a filename based on country and hscode
        filename = f"{country}_{'854140'}.csv"

        # Save the DataFrame to a CSV file
        df.to_csv("data/imports/HS854140/"+filename, index=True)
        print(f"File {filename} created.")

def loadImportRatio(RatioCountrycsv):
    df = pd.read_csv(RatioCountrycsv, delimiter=',', decimal='.')
    df.Year = pd.to_datetime(df['Year'], format='%Y').dt.year
    df.set_index('Year', inplace=True)
    #df = df.pivot_table(index=["Year"],  columns='State', values=["import_ratio"])  # values=["Value", "Weight"]

    return df

