from typing import Union
import re

def find_restaurants_hotels_cafes(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('restaurante', el)
      match2 = re.search('hotéis', el)
      match3 = re.search('café', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
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
    "name": "Restaurantes, Hotéis, Cafés e Similares",
    "by": "by-product",
    "values": values
  }