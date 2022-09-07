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
        return float(row[-1])
  
  value = find()

  return {
    "id": 10,
    "name": "Restaurantes, Hotéis, Cafés e Similares",
    "value": value
  }