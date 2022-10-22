import pandas as pd
from interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError

def findInterestRates(html: str, indicator: Indicator):
  table = []
  db_name = indicator['db_name']

  try:
    tables = pd.read_html(html, )

    table = tables[11].values.tolist()

  except Exception as err:
    print(err)
    errorMessage = f'The {db_name} has a format error'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)
    createError(errorMessage)

  return table