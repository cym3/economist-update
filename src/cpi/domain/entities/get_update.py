from optparse import Values
from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Value(BaseModel):
  date: DateCpi
  value: float

class CPI(BaseModel):
  _id: str
  name: str
  values: list[Value]

def updateCpiDB (CPIs: list[CPI], indicator: Indicator):
  db_name = indicator['db_name']

  try:
    database = economist_db()
    collection = database[db_name]

    for cpi in CPIs:
      _id = cpi['_id']
      values = cpi['values']

      collection.update_one(
        { '_id': _id },
        { '$set': { 'values':  values }}
      )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'