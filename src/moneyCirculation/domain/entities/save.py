from src.moneyCirculation.domain.requiredFields.main import MoneyCirculation, Indicator
from src.moneyCirculation.domain.entities.create_tasks import createTaskDB
from src.moneyCirculation.domain.errors.create_error import createError
from src.core.db.connect_db import economist_db
from bson.objectid import ObjectId

def saveMoneyCirculationDB(moneyCirculation: list[MoneyCirculation], indicator: Indicator):
  db_name = indicator['db_name']
  
  try:
    database = economist_db()
    collection = database[db_name]

    for b_indicator in moneyCirculation:
      id = ObjectId(b_indicator['id'])
      values = b_indicator['values']
      volumes = b_indicator['volumes']

      index = 0
      for el in values:
        date = el['date']
        value = el['value']

        volume = volumes[index]['value']

        collection.update_one(
          { '_id': id },
          { '$push': { 
            'values':  {
              'date': date,
              'value': value
            },
            'volumes':  {
              'date': date,
              'value': volume
            }
          }}
        )

        index += 1
    
    createTaskDB(isDone=True, indicator=indicator)

  except Exception as err:
    print(err)
    errorMessage = f'Was not able to save {db_name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return 'Done'