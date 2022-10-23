from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from pydantic import BaseModel

class Product(BaseModel):
  name: str
  value: float

class CPI(BaseModel):
  products: list[Product]
  total: float
  date: DateCpi

def saveCpiDB (CPIs: CPI, indicator: Indicator):
  db_name = indicator['db_name']
  try:
    database = economist_db()
    collection = database[db_name]

    products = CPIs['products']
    total = CPIs['total']
    date = CPIs['date']

    collection.update_one(
      { 'type': 'by-region' },
      { '$push': { 'values':  { 'date': date, 'value': total } }}
    )

    for product in products:
      product_name = product['name']
      value = product['value']

      collection.update_one(
        { 'type': 'by-product', 'name': product_name },
        { '$push': { 'values':  { 'date': date, 'value': value } }}
      )
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'