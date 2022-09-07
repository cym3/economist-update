from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError

async def formatInterestRates(table: list[list[str]], date: str):
  formatted = []

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
    errorMessage = f'The interest Rates has a format error'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return formatted