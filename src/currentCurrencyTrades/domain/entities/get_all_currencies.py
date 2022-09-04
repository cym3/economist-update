from src.currentCurrencyTrades.domain.errors.create_error import create_error
from src.core.db.connect_db import db

async def getAllCurrenciesDB ():
  currencies = []

  try: 
    database = db()
    collection = database['exchange-rates']

    currencies = collection.find()

  except Exception:
    errorMessage = f'Database failed to get currencies'

    await create_error(errorMessage)

  return currencies