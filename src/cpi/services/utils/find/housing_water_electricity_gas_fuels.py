from typing import Union
import re

def find_housing_water_electricity_gas_fuels(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('habitação', el)
      match2 = re.search('água', el)
      match3 = re.search('electricidade', el)
      match4 = re.search('gás', el)

      if (match1 is not None) and (match2 is not None) and (match3 is not None) and (match4 is not None):
        return float(row[-1])

  value = find()

  return {
    "id": 0,
    "name": "Habitação, Água, Electricidade, Gás e Outros Combustíveis",
    "value": value
  }