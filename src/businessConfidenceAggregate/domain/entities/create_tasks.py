from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.businessConfidenceAggregate.domain.errors.create_error import createError

def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()

  task = {
    'jobCode': '04-job',
    'name': 'Aggregate Business Confidence indicator',
    'description': 'Aggregate Business Confidence indicator update',
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
    errorMessage = 'Was not able to save the task of Aggregate Business Confidence indicator.'
    createError(errorMessage)

  return 'Done'