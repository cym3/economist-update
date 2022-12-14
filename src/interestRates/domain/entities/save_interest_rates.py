from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class InterestRates(BaseModel):
  name: str
  value: float
  date: str

def saveInterestRatesDB (data: list[InterestRates], indicator: Indicator):
  db_name = indicator['db_name']

  try:
    database = economist_db()
    collection = database[db_name]

    for d in data:
      name = d['name']
      value = d['value']
      date = d['date']

      collection.update_one(
        { 'name': name },
        { '$push': { 'values':  { 'date': date, 'value': value } }}
      )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save Interest Rates, {date}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'