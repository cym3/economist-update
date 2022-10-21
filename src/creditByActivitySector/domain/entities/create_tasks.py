from typing import Union
from src.core.db.connect_db import jobs_db
from datetime import datetime
from src.creditByActivitySector.domain.errors.create_error import createError

def createTaskDB (isDone: bool, error: Union[str, None] = ''):
  now = datetime.now()

  task = {
    'jobCode': '02-business-confidence',
    'name': 'By Sector Business Confidence indicator',
    'description': 'By Sector Business Confidence indicator update',
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
    createError(errorMessage)

  return 'Done'