from typing import Union
import re

def find_leisure_recreation_culture(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('lazer', el)
      match2 = re.search('recreação', el)
      match3 = re.search('cultura', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None):
        return float(row[-1])

  value = find()

  return {
    "id": 0,
    "name": "Lazer, Recreação e Cultura",
    "value": value
  }