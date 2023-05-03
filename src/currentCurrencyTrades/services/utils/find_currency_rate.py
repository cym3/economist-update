from src.currentCurrencyTrades.domain.requiredFields.page_validator import Rate
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

def findCurrencyRate(isoCode: str, rates: list[Rate], indicator: Indicator):
  db_name = indicator['db_name']

  try:
    isFound = False
    
    for rate in rates:
      if rate['currency'] == isoCode:
        isFound = True
        return rate
      
    if isFound == False: 
      Exception('Rate not found')
    
  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has not found the {isoCode} rate in the BM object'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)