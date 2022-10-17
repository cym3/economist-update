from rapidfuzz.process import extractOne

def find(countryName: str, table: list[list[str]]):
  names = [row[0] for row in table]

  match = extractOne(countryName, names)
  match_score  = match[-2]
  matched_index  = match[-1]

  if (match_score > 85):
    return table[matched_index]

def findCurrencyTrades(countryName: str, currenciesTrades: list[list[str]]):
  if (countryName == 'Emirados Árabes Unidos'):
    return find(countryName='Emiratos A.Unid', table=currenciesTrades)

  if (countryName == 'Kuwait'):
    return find(countryName='Kowait', table=currenciesTrades)
  
  return find(countryName=countryName, table=currenciesTrades)    