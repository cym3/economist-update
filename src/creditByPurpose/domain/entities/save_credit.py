from src.creditByPurpose.domain.requiredFields.credit import DateCredit
from src.creditByPurpose.domain.entities.create_tasks import createTaskDB
from src.creditByPurpose.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Value(BaseModel):
  date: DateCredit
  circul: float
  investment: float
  total: float

class CreditByPurpose(BaseModel):
  id: str
  values: Value

def saveCreditByPurposeDB(creditByPurpose: list[CreditByPurpose], indicator: str):
  db_name = indicator['db_name']
  
  try:
    database = economist_db()
    collection = database[db_name]

    for b_indicator in creditByPurpose:
      id = b_indicator['id']
      values = b_indicator['values']

      date = values['date']
      circul = values['circul']
      investment = values['investment']
      total = values['total']

      collection.update_one(
        { '_id': id },
        { '$push': { 
          'values':  {
            'date': date,
            'circul': circul,
            'investment': investment,
            'total': total
          }
        }}
      )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return 'Done'