from typing import Union
from datetime import datetime
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.services.utils.find.filter_row import filter_row
import re

def find_furniture_decoration_items_household_equipment(
  table: list[list[Union[float, int]]],
  dates_row: list[datetime],
  date: DateCpi
):
  old_date = datetime(date['year'], date['month'], 1)
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('mobiliário', el)
      match2 = re.search('artigos', el)
      match3 = re.search('decoração', el)
      match4 = re.search('equipamento', el)
      match5 = re.search('doméstico', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None) and (match4 is not None) and (match5 is not None):
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
    "name": "Mobiliário, Artigos de Decoração, Equipamento Doméstico e Manutenção da Habitação",
    "values": values
  }