from src.cpi.domain.requiredFields.cpi import Indicator
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getAllDB (indicator: Indicator):
  db_name = indicator['db_name']
  CPIs = []

  try: 
    database = economist_db()
    collection = database[db_name]

    CPIs = collection.find()

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get {db_name} last update date'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return CPIs