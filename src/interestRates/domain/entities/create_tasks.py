from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.interestRates.domain.errors.create_error import createError

def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')

  task = {
    'jobCode': '02-job',
    'name': 'InterestRates',
    'description': 'Daily Interest Rates update',
    'isDone': isDone,
    'error': error,
    'date': date
  }

  try:
    database = jobs_db()
    collection = database['jobs']

    collection.insert_one(task)
    
  except Exception as err:
    print(err)
    errorMessage = 'Was not able to save the task of interest rates.'
    createError(errorMessage)

  return 'Done'