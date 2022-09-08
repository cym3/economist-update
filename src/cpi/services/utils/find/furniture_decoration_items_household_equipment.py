from typing import Union
import re

def find_furniture_decoration_items_household_equipment(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('mobiliário', el)
      match2 = re.search('artigos', el)
      match3 = re.search('decoração', el)
      match4 = re.search('equipamento', el)
      match5 = re.search('doméstico', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None) and (match4 is not None) and (match5 is not None):
        values = []
        year = 2018
        month = 1

        index = 0
        for col in row:

          if index >= 138:
            if type(col) == type('str'):
              col = 0
            values.append({
              "date": {
                "year": year,
                "month": month
              },
              "value": float(col)
            })

            if month == 12:
              month = 1
              year += 1
            else:
              month += 1

          index += 1

        return values
  
  values = find()

  return {
    "name": "Mobiliário, Artigos de Decoração, Equipamento Doméstico e Manutenção da Habitação",
    "by": "by-product",
    "values": values
  }