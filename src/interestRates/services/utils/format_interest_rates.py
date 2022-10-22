from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError

def formatInterestRates(table: list[list[str]], date: str, indicator: Indicator):
  formatted = []
  db_name = indicator['db_name']


  try:
    for rate in table:
      name = rate[0]

      if name == 'Prime rate':
        name = 'Prime Rate'

      ints = [x for x in str(rate[1])]
      int1 = f'{ ints[0] }{ ints[1] }'
      int2 = f'{ ints[2] }{ ints[3] }'
    
      value = float('.'.join([int1,int2]))

      formatted.append({
        'name': name,
        'value': value,
        'date': date
      })
    
  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error on {name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return formatted