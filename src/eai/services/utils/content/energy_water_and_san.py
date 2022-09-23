import re
from datetime import datetime
from typing import Union
from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError
from src.eai.services.utils.find.filter_row import filter_row

name = 'energia,água e san'

def energyWaterAndSanFormatter(
  table: list[list[Union[float, str]]],
  dates_row: list[datetime],
  last_date_on_db: datetime
):
  values = []

  try:
    for row in table:
      names = str(row[0]).split('\n')
      row_name = ' '.join(names).lower()
      match = re.search(name, row_name)

      if match is not None:

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

    if not values:
      raise Exception(f"'{name}' index is not found on the excel file.")

  except Exception as err:
    print(err)
    errorMessage = f'aggregate Economic Activities Index: has a format error on {name}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return {
    'id': '6306c46810f38589a0d189ab',
    'name': 'Energia,Água e San',
    'values': values
  }
