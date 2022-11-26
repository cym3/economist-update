from typing import Union
from src.moneyCirculation.services.utils.content.utils.find_rows import findValuesRows, findVolumesRows
from src.moneyCirculation.services.utils.content.utils.formatter import rowFormatter
from src.moneyCirculation.domain.requiredFields.main import Indicator, DateMoneyCirculation

name: str = 'Notas em circulação'

def banknotesFormatter(
  table: list[list[Union[float, str]]],
  new_date: DateMoneyCirculation,
  indicator: Indicator
):
  volumes = []
  values = []

  try:
    values_row = findValuesRows(table, name, 7)
    volumes_row = findVolumesRows(table, name, 15)

    if (not bool(volumes_row)) or (not bool(values_row)):
      raise Exception(f"'{name}' have not found row of data.")

    volumes = rowFormatter(volumes_row, new_date)
    values = rowFormatter(values_row, new_date)

  except Exception as err:
    print(err)

  return {
    'id': "63778ffe4fe16ee1e9bfeb15",
    'name': name,
    'volumes': volumes,
    'values': values
  }
