from itertools import product
import re
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

async def formatCpi(trades: list[str], date: str, divider: int, countryName: str, isoCode: str):
  regex = r'\d+'

  formatted = {
    'products': [{
        'name': 'Alimentos e Bebidas não Alcoólicas',
        'value': 43
    }],
    'total': 43
  }
  
  try:
    print('Work')

  except Exception as err:
    print(err)
    errorMessage = f'The {countryName} currency has a format error'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return formatted