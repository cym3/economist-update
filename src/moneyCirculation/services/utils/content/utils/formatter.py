from typing import Union
from src.moneyCirculation.domain.requiredFields.main import DateMoneyCirculation

def rowFormatter(
  row: list[Union[float, str]],
  new_date: DateMoneyCirculation,
):
  value = row[-1]

  if (type(value) != type(0)) and (type(value) != type(0.2)):
    value = None

  newValue = {
    'date': {
      'year': new_date['year'],
      'month': new_date['month']
    },
    'value': value
  }

  return [newValue]