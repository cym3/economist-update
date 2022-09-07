from typing import Union
import re

def find_non_alcoholic_food(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('produto', el)
      match2 = re.search('alimentar', el)
      match3 = re.search('bebida', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
        return float(row[-1])
  
  value = find()

  return {
    "id": 0,
    "name": "Alimentos e Bebidas não Alcoólicas",
    "value": value
  }