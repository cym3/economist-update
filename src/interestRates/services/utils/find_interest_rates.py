import pandas as pd
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError

def findInterestRates(html: str):
  table = []

  try:
    tables = pd.read_html(html)

    table = tables[11].values.tolist()

  except Exception as err:
    print(err)
    errorMessage = f'The interest Rates has a format error'

    createTaskDB(isDone=False, error=errorMessage)
    createError(errorMessage)

  return table