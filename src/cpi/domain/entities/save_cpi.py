from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import db
from pydantic import BaseModel

class CurrencyTrade(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

async def saveCpiDB (currencyTrades: list[CurrencyTrade], region: str):
  try:
    database = db()
    collection = database['cpi-beira-test']

    for currency in currencyTrades:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )
    
    await createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to  {region} CPI'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return 'Done'