import re

def find(countryName: str, currenciesTrades: list[list[str]]):
  for trades in currenciesTrades:
    match = re.search(countryName, trades[0])

    if match is not None:
      return trades

def findCurrencyTrades(countryName: str, currenciesTrades: list[list[str]]):
  if (countryName == 'Emirados Árabes Unidos'):
    return find(countryName='Emiratos A.Unid', currenciesTrades=currenciesTrades)

  if (countryName == 'Kuwait'):
    return find(countryName='Kowait', currenciesTrades=currenciesTrades)
  
  if (countryName == 'Nova Zelândia'):
    return find(countryName='Nova Zelandia', currenciesTrades=currenciesTrades)

  return find(countryName=countryName, currenciesTrades=currenciesTrades)    