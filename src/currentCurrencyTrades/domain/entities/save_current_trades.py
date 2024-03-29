from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class CurrencyRate(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

def saveCurrentTradesDB (currenciesRates: list[CurrencyRate], indicator: Indicator):
  db_name = indicator['db_name']
  try:
    database = economist_db()
    collection = database[db_name]

    for currency in currenciesRates:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save exchange rates, { currenciesRates[0].date }'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'