from distutils.errors import UnknownFileError
import re

unknownNomes = ['Emiratos A.Unid', 'Kowait', 'Nova Zelandia']

def findCurrencyTrades(currenciesTrades: list[list[str]], countryName: str):
    for currencyTrades in currenciesTrades:
      match = re.search(countryName, currencyTrades[0])

      if match is not None:
        return currencyTrades

      if match is None:
        for unknownname in unknownNomes:
          match = re.search(unknownname, currencyTrades[0])

          if match is not None:
            return currencyTrades
          