import pandas as pd
from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError

async def findInterestRates(html: str):
  table = []

  try:
    tables = pd.read_html(html)
    table = tables[12].values.tolist()

  except Exception:
    errorMessage = f'The interest Rates has a format error'

    await createTaskDB(isDone=False, error=errorMessage)
    await createError(errorMessage)

  return table