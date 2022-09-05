from typing import Union
from src.core.db.connect_db import db
from datetime import datetime
from src.interestRates.domain.errors.create_error import createError

async def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')

  task = {
    'taskCode': 'T1',
    'name': 'InterestRates',
    'description': 'Daily Interest Rates update',
    'isDone': isDone,
    'error': error,
    'date': date
  }

  try:
    database = db()
    collection = database['tasks']

    collection.insert_one(task)
    
  except Exception:
    errorMessage = 'Was not able to save interest rates Task.'
    await createError(errorMessage)

  return 'Done'