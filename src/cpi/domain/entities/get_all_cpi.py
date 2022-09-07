from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.core.db.connect_db import db

async def getAllCpiDB ():
  currencies = []

  try: 
    database = db()
    collection = database['exchange-rates']

    currencies = collection.find()

  except Exception as err:
    print(err)
    errorMessage = 'Database failed to get currencies'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return currencies