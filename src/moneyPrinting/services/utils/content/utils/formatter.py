from typing import Union
from src.moneyPrinting.domain.requiredFields.main import DateMoneyPrinting

def rowFormatter(
  row: list[Union[float, str]],
  new_date: DateMoneyPrinting,
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