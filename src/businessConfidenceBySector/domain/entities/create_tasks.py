from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.businessConfidenceBySector.domain.errors.create_error import createError
from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Indicator

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
    errorMessage = 'Was not able to save the task of By Sector Business Confidence indicator.'
    createError(errorMessage, indicator)

  return 'Done'