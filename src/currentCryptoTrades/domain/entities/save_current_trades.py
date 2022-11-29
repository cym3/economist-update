from src.currentCryptoTrades.domain.requiredFields.currencies import Indicator
from src.currentCryptoTrades.domain.entities.create_tasks import createTaskDB
from src.currentCryptoTrades.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class CurrencyTrade(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

def saveCurrentTradesDB (currencyTrades: list[CurrencyTrade], indicator: Indicator):
  db_name = indicator['db_name']
  try:
    database = economist_db()
    collection = database[db_name]

    for currency in currencyTrades:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save exchange rates, { currencyTrades[0].date }'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'