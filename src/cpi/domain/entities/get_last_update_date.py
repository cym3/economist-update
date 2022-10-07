from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB (region: str):
  date = {}

  try: 
    database = economist_db()
    collection = database[f'cpi-{region}']

    cpi = collection.find_one({ 'type': 'by-region' })
    last = cpi['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get {region} CPI last update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return date