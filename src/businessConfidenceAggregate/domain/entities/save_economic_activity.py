from businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Value(BaseModel):
  quarter: Quarter
  value: float

class BusinessConfidence(BaseModel):
  id: str
  values: list[Value]

def saveBusinessConfidenceDB(businessConfidence: list[BusinessConfidence], indicator: Indicator):
  db_name = indicator['db_name']
  try:
    database = economist_db()
    collection = database[db_name]

    for b_indicator in businessConfidence:
      id = b_indicator['id']
      values = b_indicator['values']

      for el in values:
        quarter = el['quarter']
        value = el['value']

        collection.update_one(
          { '_id': id },
          { '$push': { 'values':  { 'quarter': quarter, 'value': value } }}
        )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return 'Done'