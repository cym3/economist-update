import re
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

def formatCurrencyTrades(
  tableRow: list[str],
  date: str,
  divider: int,
  isoCode: str,
  indicator: Indicator
):
  regex = r'\d+'
  formatted = {}
  db_name = indicator['db_name']
  
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
    errorMessage = f'{db_name}: has a format error on {isoCode}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return formatted