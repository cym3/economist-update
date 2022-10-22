from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.interestRates.domain.errors.create_error import createError
from src.interestRates.domain.requiredFields.interest_rates import Indicator

def createTaskDB (isDone: bool, indicator: Indicator, error: Union[str, None] = '',):
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
    print(err)
    errorMessage = 'Was not able to save the task of interest rates.'
    createError(errorMessage)

  return 'Done'