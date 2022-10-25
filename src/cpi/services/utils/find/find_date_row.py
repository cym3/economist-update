from typing import Union
from src.cpi.domain.requiredFields.cpi import Indicator
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from rapidfuzz.fuzz import partial_ratio

name = 'Divisão e Grupos'

def findDateRow(table: list[list[Union[float, int]]], indicator: Indicator):
  db_name = indicator['db_name']

  try:
    row_is_found = False

    for row in table:
      row_name = f'{row[0]}'
      match_score = partial_ratio(name, row_name)

      if (match_score > 90):
        row_is_found = True
        return row

    if row_is_found == False:
      raise Exception(f"'{name}' is not found on the excel file.")

  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error on {name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)