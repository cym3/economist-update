from typing import Union
from datetime import datetime
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.services.utils.find.filter_row import filter_row

def findTotal(
  table: list[list[Union[float, int]]],
  dates_row: list[datetime],
  date: DateCpi
):
  old_date = datetime(date['year'], date['month'], 1)

  def find():
    for row in table:
      el = str(row[1]).lower()

      if (el == 'total'):
        return row
  
  row = find()
  row = filter_row(row)

  values = []

  index = 0
  for el in dates_row:
    if el > old_date:
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

  return {
    "name": "Total",
    "values": values
  }

