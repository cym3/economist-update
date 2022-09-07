from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import db

async def getLastUpdateDateDB (region: str):
  date = {}

  try: 
    database = db()
    collection = database[f'cpi-{region}']

    cpi = collection.find_one({ 'by': 'by-region' })
    last = cpi['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get {region} CPI'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return date