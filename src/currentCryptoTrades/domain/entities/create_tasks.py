from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.currentCryptoTrades.domain.errors.create_error import createError
from src.currentCryptoTrades.domain.requiredFields.currencies import Indicator

def createTaskDB (isDone: bool, indicator: Indicator, error: Union[str, None] = '',):
  db_name = indicator['db_name']
  now = datetime.now()

  task = {
    'jobCode': indicator['jobCode'],
    'name': indicator['name'],
    'description': indicator['description'],
    'isDone': isDone,
    'error': error,
    'created_at': now
  }

  try:
    database = jobs_db()
    collection = database['jobs']

    collection.insert_one(task)
    
  except Exception as err:
    errorMessage = f'Was not able to save the task of {db_name}'
    createError(errorMessage, indicator)
    print(err)

  return 'Done'