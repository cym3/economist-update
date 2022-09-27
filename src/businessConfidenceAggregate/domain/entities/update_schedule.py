from src.economicActivityAggregate.domain.requiredFields.economic_activity import Schedule
from src.core.db.connect_db import jobs_db

from src.economicActivityAggregate.domain.errors.create_error import createError

def updateScheduleDB(schedule: Schedule):
  scheduleCode = schedule['scheduleCode']
  howToUpdate = schedule['howToUpdate']
  date = schedule['date']

  try:
    database = jobs_db()
    collection = database['schedules']

    collection.update_one(
      {'scheduleCode': scheduleCode },
      {'$set': { 'howToUpdate': howToUpdate, 'date': date }}
    )

  except Exception as err:
    print(err)
    errorMessage = 'Was not able to save the task of CPI.'
    createError(errorMessage)

  return 'Done'