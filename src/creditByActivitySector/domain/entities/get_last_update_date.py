from src.creditByActivitySector.domain.entities.create_tasks import createTaskDB
from src.creditByActivitySector.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(db_name: str):
  date = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    credit = collection.find_one()
    last = credit['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get By Sector Business Confidence indicator update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return date