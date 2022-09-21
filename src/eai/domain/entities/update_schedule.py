from src.eai.domain.requiredFields.eai import Schedule
from src.core.db.connect_db import jobs_db
from bson.objectid import ObjectId
from src.eai.domain.errors.create_error import createError

def updateScheduleDB(schedule: Schedule):
  id = schedule['id']
  howToUpdate = schedule['howToUpdate']
  date = schedule['date']

  try:
    database = jobs_db()
    collection = database['schedule']

    collection.update_one(
      {'_id': ObjectId(id)},
      {'$set': {'howToUpdate': howToUpdate, 'date': date}}
    )
    
  except Exception as err:
    print(err)
    errorMessage = 'Was not able to save the task of CPI.'
    createError(errorMessage)

  return 'Done'