from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db

def getLastUpdateDateDB(db_name: str):
  date = {}

  try: 
    database = economist_db()
    collection = database[db_name]

    eai = collection.find_one({'type': 'Agregado' })
    last = eai['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get EAI update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return date