from interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(indicator: Indicator):
  db_name = indicator['db_name']
  date = ''

  try:
    database = economist_db()
    collection = database[db_name]

    interestRates = collection.find()

    dates = [rate['values'][-1]['date'] for rate in interestRates]

    date = max(dates)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save Interest Rates, {date}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return date