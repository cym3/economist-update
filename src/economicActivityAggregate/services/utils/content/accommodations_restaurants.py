from datetime import datetime
from typing import Union
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError
from src.economicActivityAggregate.services.utils.find.filter_row import filter_row
from rapidfuzz.process import extractOne

name = 'aloj.rest. similares'

def accommodationsRestaurantsFormatter(
  table: list[list[Union[float, str]]],
  dates_row: list[datetime],
  last_date_on_db: datetime
):
  values = []

  try:
    row_is_found = False

    names = [row[0] for row in table]

    match = extractOne(name, names)
    match_score  = match[-2]
    matched_index  = match[-1]

    if (match_score > 85):
      row_is_found = True

      row = table[matched_index]

      # Get only the first 12 list elements
      # row must have the same length with date_row
      row = filter_row(row)

      index = 0
      for el in dates_row:
        if el > last_date_on_db:
          year = el.year
          month = el.month
          value = row[index]

          values.append({
            'date': {
              'year': year,
              'month': month
            },
            'value': value
          })

        index += 1

    if row_is_found == False:
      raise Exception(f"'{name}' index is not found on the excel file.")

  except Exception as err:
    print(err)
    errorMessage = f'aggregate Economic Activities Index: has a format error on {name}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return {
    'id': '6306c1b54145e6a1fc2b9ed6',
    'values': values
  }
