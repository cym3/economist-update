from typing import Union
from datetime import datetime
from src.utils.date.index import CreateDateUTC
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.services.utils.find.filter_row import filter_row
import re

def find_restaurants_hotels_cafes(
  table: list[list[Union[float, int]]],
  dates_row: list[datetime],
  date: DateCpi
):
  old_date = CreateDateUTC(date['year'], date['month'], 1).date
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('restaurante', el)
      match2 = re.search('hotéis', el)
      match3 = re.search('café', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
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
    "id": "631a471d5d359b88a2bfb5b4",
    "values": values
  }