from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.currentCurrencyTrades.domain.errors.create_error import createError

def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()

  task = {
    'jobCode': '03-job-cpi',
    'name': 'CPI',
    'description': 'Consumer Price Index update',
    'isDone': isDone,
    'error': error,
    'created_at': now
  }

  try:
    database = jobs_db()
    collection = database['jobs']

    collection.insert_one(task)
    
  except Exception as err:
    print(err)
    errorMessage = 'Was not able to save the task of CPI.'
    createError(errorMessage)

  return 'Done'