from typing import Union
import re

def find_health(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('saúde', el)

      if match1 is not None:
        return float(row[-1])

  value = find()

  return {
    "id": 0,
    "name": "Saúde",
    "value": value
  }