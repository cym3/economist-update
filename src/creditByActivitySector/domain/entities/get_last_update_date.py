from src.creditByActivitySector.domain.requiredFields.credit import Indicator
from src.creditByActivitySector.domain.entities.create_tasks import createTaskDB
from src.creditByActivitySector.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(indicator: Indicator):
  db_name = indicator['db_name']
  date = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    credit = collection.find_one()
    last = credit['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get {db_name} update date'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return date