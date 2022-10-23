from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(indicator: str):
  db_name = indicator['db_name']
  quarter = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    eai = collection.find_one()
    last = eai['values'][-1]

    quarter = last['quarter']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get Aggregate Business Confidence indicator update date'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return quarter