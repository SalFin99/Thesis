from forex_python.converter import CurrencyRates
import pandas as pd
from Import import getImport


def get_exchange_rates():
    start_year = 2000
    end_year = 2019

    exchange_rates = {}
    c = CurrencyRates()

    for year in range(start_year, end_year + 1):
        date_obj = pd.to_datetime(f'{year}-12-31')
        rate = c.get_rate('EUR', 'USD', date_obj=date_obj)
        exchange_rates[year] = rate

    return exchange_rates #this returns a dictionary


def toUSD():
    df = getImport.loadSingleImports('data/imports/EU/china/EU26_850511ch.csv')

    df['rates'] = get_exchange_rates()

    df['UsdValue'] = df['Value'] * df['rates']

    # print(df)

    df = df.drop(['rates', 'Value'], axis=1)

    df = df.rename(columns={'UsdValue':'Value'})

    df.to_csv('data/imports/EU/newUSD/EU26_850511chUSDnew.csv')
