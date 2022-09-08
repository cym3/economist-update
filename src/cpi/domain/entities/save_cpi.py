from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import db
from pydantic import BaseModel

class Product(BaseModel):
  name: str
  value: float

class CPI(BaseModel):
  products: list[Product]
  total: float
  date: DateCpi

async def saveCpiDB (CPIs: CPI, region: str):
  try:
    database = db()
    collection = database[f'cpi-{region}']

    products = CPIs['products']
    total = CPIs['total']
    date = CPIs['date']

    collection.update_one(
      { 'by': 'by-region' },
      { '$push': { 'values':  { 'date': date, 'value': total } }}
    )

    for product in products:
      product_name = product['name']
      value = product['value']

      collection.update_one(
        { 'by': 'by-product', 'name': product_name },
        { '$push': { 'values':  { 'date': date, 'value': value } }}
      )
    
    await createTaskDB(isDone=True)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to  {region} CPI'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return 'Done'