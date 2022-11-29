from src.currentCryptoTrades.domain.requiredFields.currencies import Indicator
from src.currentCryptoTrades.domain.entities.create_tasks import createTaskDB
from src.currentCryptoTrades.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getAllCurrenciesDB (indicator: Indicator):
  db_name = indicator['db_name']
  currencies = []
  
  try: 
    database = economist_db()
    collection = database[db_name]

    found = collection.find({})

    for el in found:
      currencies.append(el)

  except Exception as err:
    print(err)
    errorMessage = 'Database failed to get currencies'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return currencies