from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError
from src.core.db.connect_db import db
from pydantic import BaseModel

class InterestRates(BaseModel):
  name: str
  value: float
  date: str

async def saveInterestRatesDB (data: list[InterestRates]):

  try:
    database = db()
    collection = database['interest-rates']

    for d in data:
      name = d['name']
      value = d['value']
      date = d['date']

      collection.update_one(
        { 'name': name },
        { '$push': { 'values':  { 'date': date, 'value': value } }}
      )
    
    await createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save Interest Rates, {date}'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return 'Done'