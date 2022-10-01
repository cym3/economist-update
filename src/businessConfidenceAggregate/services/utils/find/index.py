import re
from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator

import re

def findFirstRow(table: list, indicator: Indicator):
  name: str = indicator['name'].lower()

  index = 0
  for row in table:
    el = str(row[0]).split('\n')
    row_name = ' '.join(el).lower()

    match = re.search(name, row_name)

    if match is not None:
      return index
    index += 1


def findLastRow(table: list):
  index = 0

  for row in table:
    row_name = str(row[0]).lower()
    match = re.search('outros serviços', row_name)

    if match is not None:
      return index
    index += 1