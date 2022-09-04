import re
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

async def formatCurrencyTrades(trades: list[str], date: str, divider: int, countryName: str, isoCode: str):
  regex = r'\d+'
  formatted = {}
  
  try:
    buy = re.findall(regex, trades[0])
    sale=  re.findall(regex, trades[1])

    formatted = {
      'isoCode': isoCode,
      'trade': {
        'buy': float('.'.join(buy)) / divider,
        'sale': float('.'.join(sale)) / divider,
        'date': date
      }
    }

  except Exception:
    errorMessage = f'The {countryName} currency has a format error'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return formatted