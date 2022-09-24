import re
from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator

def findFirstRow(sheet: list, indicator: Indicator):
  name: str = indicator['name'].lower()

  index = 0
  for row in sheet:
    el = str(row[0]).split('\n')
    row_name = ' '.join(el).lower()

    if name == row_name:
      return index
    index += 1


def findLastRow(sheet: list):
  index = 0

  for row in sheet:
    row_name = str(row[0]).lower()
    match = re.search('outros serviços', row_name)

    if match is not None:
      return index
    index += 1