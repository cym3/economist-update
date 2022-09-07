from typing import Union
from src.core.db.connect_db import db
from datetime import datetime
from src.currentCurrencyTrades.domain.errors.create_error import createError

async def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')

  task = {
    'taskCode': 'T3',
    'name': 'CPI',
    'description': 'Update of consumer price Index (CPI)',
    'isDone': isDone,
    'error': error,
    'date': date
  }

  try:
    database = db()
    collection = database['tasks']

    collection.insert_one(task)
    
  except Exception as err:
    print(err)
    errorMessage = 'Was not able to save the task of CPI.'
    await createError(errorMessage)

  return 'Done'