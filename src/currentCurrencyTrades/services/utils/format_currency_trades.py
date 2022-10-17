import re
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

def formatCurrencyTrades(tableRow: list[str], date: str, divider: int, countryName: str, isoCode: str):
  regex = r'\d+'
  formatted = {}
  
  try:
    buy = re.findall(regex, tableRow[2])
    buy = '.'.join(buy)

    sale =  re.findall(regex, tableRow[3])
    sale = '.'.join(sale)

    formatted = {
      'isoCode': isoCode,
      'trade': {
        'buy': float(buy) / divider,
        'sale': float(sale) / divider,
        'date': date
      }
    }

  except Exception as err:
    print(err)
    errorMessage = f'The {countryName} currency has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return formatted