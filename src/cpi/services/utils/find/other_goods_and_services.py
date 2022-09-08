from typing import Union
import re

def find_other_goods_and_services(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('bens', el)
      match2 = re.search('serviço', el)
      match3 = re.search('diverso', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
        return float(row[-1])

  value = find()

  return {
    "id": 11,
    "name": "Bens e Serviços Diversos",
    "value": value
  }