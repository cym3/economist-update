from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError
from src.core.db.connect_db import db

async def getLastUpdateDateDB():
  date = ''

  try:
    database = db()
    collection = database['interest-rates']

    interestRates = collection.find()

    dates = [rate['values'][-1]['date'] for rate in interestRates]

    date = max(dates)

  except Exception:
    errorMessage = f'Was not able to save Interest Rates, {date}'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return date