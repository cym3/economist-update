from src.currentCurrencyTrades.domain.requiredFields.page_validator import Rate
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

def findDivider(isoCode: str): 
  if isoCode == 'INR' or isoCode == 'IQD' or isoCode == 'JPY' or isoCode == 'MWK' or isoCode == 'TZS' or isoCode == 'ZWL':
    return 1000
  return 1

def formatCurrencyRate(
  rate: Rate,
  date: str,
  isoCode: str,
  indicator: Indicator
):
  formatted = {}
  db_name = indicator['db_name']
  
  try:
    buy = float(rate['buy'])
    sale = float(rate['sell'])
    divider = findDivider(isoCode)

    formatted = {
      'isoCode': isoCode,
      'trade': {
        'buy': buy / divider,
        'sale': sale / divider,
        'date': date
      }
    }

  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error on {isoCode}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return formatted