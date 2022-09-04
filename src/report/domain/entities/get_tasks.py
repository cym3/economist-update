from src.core.db.connect_db import db
from src.currentCurrencyTrades.domain.errors.create_error import createError

async def getTasksDB():
  tasks = []

  try:
    database = db()
    collection = database['tasks']

    tasks = collection.find()
    
  except Exception:
    errorMessage = 'Was not able to get all Task.'
    await createError(errorMessage)

  return tasks