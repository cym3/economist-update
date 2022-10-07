from src.businessConfidenceBySector.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceBySector.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(db_name: str):
  quarter = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    eai = collection.find_one()
    last = eai['values'][-1]

    quarter = last['quarter']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get By Sector Business Confidence indicator update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return quarter