from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError
from src.core.db.connect_db import db

def getLastUpdateDateDB():
  date = {}

  try: 
    database = db()
    collection = database['eai']

    eai = collection.find_one({ 'name': 'Indices do Volume de Negócios', 'type': 'Agregado' })
    last = eai['values'][-1]

    date = last['date']

  except Exception as err:
    print(err)
    errorMessage = f'Database failed to get EAI update date'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return date