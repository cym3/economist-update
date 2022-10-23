from src.creditByActivitySector.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByActivitySector.domain.entities.create_tasks import createTaskDB
from src.creditByActivitySector.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Value(BaseModel):
  date: DateCredit
  value: float

class CreditByActivitySector(BaseModel):
  id: str
  values: Value

def saveCreditByActivitySectorDB(creditByActivitySector: list[CreditByActivitySector], indicator: Indicator):
  db_name = indicator['db_name']
  
  try:
    database = economist_db()
    collection = database[db_name]

    for b_indicator in creditByActivitySector:
      id = b_indicator['id']
      values = b_indicator['values']

      date = values['date']
      value = values['value']

      collection.update_one(
        { '_id': id },
        { '$push': { 
          'values':  {
            'date': date,
            'value': value
          }
        }}
      )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'