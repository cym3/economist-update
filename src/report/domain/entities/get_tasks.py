from src.core.db.connect_db import jobs_db
from src.currentCurrencyTrades.domain.errors.create_error import createError

def getTasksDB():
  tasks = []

  try:
    database = jobs_db()
    collection = database['jobs']

    tasks = collection.find()
    
  except Exception as err:
    print(err)
    errorMessage = 'Was not able to get all Task.'
    createError(errorMessage)

  return tasks