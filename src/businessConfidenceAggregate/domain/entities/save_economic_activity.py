from mimetypes import init
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

def saveBusinessConfidenceDB(economicActivities: list[BusinessConfidence], db_name: str):
  try:
    database = economist_db()
    collection = database[db_name]

    for BusinessConfidence in economicActivities:
      id = BusinessConfidence['id']
      values = BusinessConfidence['values']

      for el in values:
        quarter = el['quarter']
        value = el['value']

        collection.update_one(
          { '_id': id },
          { '$push': { 'values':  { 'quarter': quarter, 'value': value } }}
        )
    
    createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name} Economic Activity'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return 'Done'