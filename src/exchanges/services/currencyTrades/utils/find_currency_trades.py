import re

def findCurrencyTrades(currenciesTrades: list[list[str]], countryName: str):
    for currencyTrades in currenciesTrades:
      match = re.search(countryName, currencyTrades[0])

      if match is not None:
        return currencyTrades