from itertools import product
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import db
from pydantic import BaseModel

class CPI(BaseModel):
  products: list
  total: float
  date: DateCpi

async def saveCpiDB (CPIs: CPI, region: str):
  try:
    database = db()
    collection = database['cpi-beira']

    products = CPIs['products']
    total = CPIs['total']
    date = CPIs['date']

    collection.update_one(
      { 'by': 'by-region' },
      { '$push': { 'values':  { 'date': date, 'value': total } }}
    )

    db_by = collection.update_one({ 'by': 'by-product'})

    db_products = db_by['products']
    
    await createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to  {region} CPI'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return 'Done'