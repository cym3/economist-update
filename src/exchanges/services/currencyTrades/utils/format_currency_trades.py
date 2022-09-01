import re
from src.core.domain.errors.domain_error import DataFetchError

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
    raise DataFetchError(
      f'Exchange Rates could not be updated {date}: The {countryName} currency has a format error'
    )

  return formatted