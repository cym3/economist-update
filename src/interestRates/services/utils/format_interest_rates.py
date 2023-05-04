from src.interestRates.services.utils.find_rate_id import findRateId
from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.requiredFields.page_validator import Rate
from src.interestRates.domain.errors.create_error import createError

def formatInterestRates(rates: list[Rate], date: str, indicator: Indicator):
  formatted = []
  db_name = indicator['db_name']

  try:
    for rate in rates:
      rateId = findRateId(rate['name'])

      formatted.append({
        'id': rateId,
        'value': float(rate['value']),
        'date': date
      })
    
  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return formatted