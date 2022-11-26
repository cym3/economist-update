from typing import Union
from src.creditByPurpose.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByPurpose.domain.entities.create_tasks import createTaskDB
from src.creditByPurpose.domain.errors.create_error import createError
from rapidfuzz.fuzz import partial_ratio

name = 'TRANSPORTES E COMUNICAÇÕES'

def transportAndCommunicationFormatter(
  table: list[list[Union[float, str]]],
  new_date: DateCredit,
  indicator: Indicator
):
  db_name = indicator['db_name']
  value = {}

  try:
    row_is_found = False

    for row in table:
      row_name = f'{row[1]}'
      match_score = partial_ratio(name, row_name)

      if (match_score > 90):
        row_is_found = True

        year = new_date['year']
        month = new_date['month']

        value = {
          'date': {
            'year': year,
            'month': month
          },
          'value': row[-1]
        }

    if row_is_found == False:
      raise Exception(f"'{name}' is not found on the excel file.")

  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error on {name}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return {
    'id': '63503b410fb0a210901b8920',
    'values': value
  }