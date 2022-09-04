from src.core.db.connect_db import db
from datetime import datetime
from src.currentCurrencyTrades.domain.errors.create_error import createError

async def createTaskDB (isDone: bool):
  now = datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')

  task = {
    'taskCode': 'T1',
    'name': 'CurrentCurrencyTrades',
    'description': 'Update of current exchange rates',
    'isDone': isDone,
    'error': '',
    'date': date
  }

  try:
    database = db()
    collection = database['tasks']

    collection.insert_one(task)
    
  except Exception:
    errorMessage = 'Was not able to save exchange rates Task.'
    await createError(errorMessage)

  return 'Done'