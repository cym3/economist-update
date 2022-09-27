from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(db_name: str):
  quarter = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    business_confidence = collection.find_one({'type': 'Agregado' })
    last = business_confidence['values'][-1]

    quarter = last['quarter']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get {db_name} update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return quarter