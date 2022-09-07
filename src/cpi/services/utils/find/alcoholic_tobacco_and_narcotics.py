from typing import Union
import re

def find_alcoholic_tobacco_and_narcotics(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('bebida', el)
      match2 = re.search('alcoólica', el)
      match3 = re.search('tabaco', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
        return float(row[-1])

  value = find()

  return {
    "id": 0,
    "name": "Bebidas Alcoólicas, Tabaco e Narcóticos",
    "value": value
  }