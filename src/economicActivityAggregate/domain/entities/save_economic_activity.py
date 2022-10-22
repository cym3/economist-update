from mimetypes import init
from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Value(BaseModel):
  date: DateEconomicActivity
  value: float

class EconomicActivity(BaseModel):
  id: str
  values: list[Value]

def saveEconomicActivityDB(economicActivities: list[EconomicActivity], indicator: Indicator):
  db_name = indicator['db_name']
  
  try:
    database = economist_db()
    collection = database[db_name]

    for economicActivity in economicActivities:
      id = economicActivity['id']
      values = economicActivity['values']

      for el in values:
        date = el['date']
        value = el['value']

        collection.update_one(
          { '_id': id },
          { '$push': { 'values':  { 'date': date, 'value': value } }}
        )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name} Economic Activity'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return 'Done'