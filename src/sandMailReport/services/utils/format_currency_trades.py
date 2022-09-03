import re
from src.core.errors.domain_error import DataFetchError
from src.core.mail.sand_mail import sandMail

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
    errorTitle = f'Exchange Rates could not be updated {date}'
    errorMessage = f'The {countryName} currency has a format error'

    await sandMail(title=errorTitle, message=errorMessage)

    raise DataFetchError(f'{errorTitle} f{errorMessage}')

  return formatted