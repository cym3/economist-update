from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.economicActivityAggregate.domain.errors.create_error import createError

def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()

  task = {
    'jobCode': '04-job',
    'name': 'Economic Activity',
    'description': 'Economic Activity update',
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