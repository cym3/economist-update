from typing import Union
import re

def find_clothing_and_footwear(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()
      match1 = re.search('vestuário', el)
      match2 = re.search('calçado', el)

      if (match1 is not None) and (match2 is not None):
        return float(row[-1])

  value = find()

  return {
    "id": 0,
    "name": "Vestuários e Calçados",
    "value": value
  }