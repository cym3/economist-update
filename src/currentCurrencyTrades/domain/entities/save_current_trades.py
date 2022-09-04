from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import db
from pydantic import BaseModel

class CurrencyTrade(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

async def saveCurrentTradesDB (currencyTrades: list[CurrencyTrade]):
  try:
    database = db()
    collection = database['exchange-rates']

    for currency in currencyTrades:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )
    
    await createTaskDB(isDone=True)

  except Exception:
    errorMessage = f'Was not able to save exchange rates, { currencyTrades[0].date }'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return 'Done'