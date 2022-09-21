from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class CurrencyTrade(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

def saveCurrentTradesDB (currencyTrades: list[CurrencyTrade]):
  try:
    database = economist_db()
    collection = database['exchange-rates']

    for currency in currencyTrades:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )
    
    createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save exchange rates, { currencyTrades[0].date }'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return 'Done'