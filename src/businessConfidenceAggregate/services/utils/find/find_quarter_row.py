import re
from typing import Union
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from src.businessConfidenceAggregate.services.utils.months import quarters
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator

def findSignQuarter(quarter_sign: str):
  for quarter in quarters:
    sign = quarter['sign']['pt']

    if quarter_sign == sign:
      return quarter


def getNewQuarter(table: list, first_row_index: int, indicator: Indicator):
  db_name = indicator['db_name']
  column_index = indicator['column_index']
  quarter_row = table[first_row_index -2]

  new_quarter: Union[dict, None] = None
  try:

    match = re.search(r'\(([^)]+)\)', quarter_row[column_index])

    if match:
      founds: str = match.group(1).split('-')
      
      new_quarter_sign = founds[0]
      new_quarter_year = founds[1]

      new_quarter = findSignQuarter(new_quarter_sign)
      new_quarter['year'] = int(new_quarter_year)
    
      new_quarter = new_quarter



  except Exception as err:
    print(err)
    errorMessage = f'Quarter in the {db_name} table could not be processed. It could be a problem format from header table row or column.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return new_quarter
