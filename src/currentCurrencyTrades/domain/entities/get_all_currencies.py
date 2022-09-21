from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getAllCurrenciesDB ():
  currencies = []

  try: 
    database = economist_db()
    collection = database['exchange-rates']

    currencies = collection.find()

  except Exception as err:
    print(err)
    errorMessage = 'Database failed to get currencies'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return currencies