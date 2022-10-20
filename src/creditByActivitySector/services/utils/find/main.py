from typing import Union
from src.businessConfidenceBySector.services.utils.find.find_quarter_row import getNewQuarter
from src.businessConfidenceBySector.services.utils.find.index import findFirstRow, findLastRow
from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceBySector.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceBySector.domain.errors.create_error import createError

def findNewQuarter(table: list, indicator: Indicator):
  db_name = indicator['db_name']
  new_table = []
  new_quarter: Union[dict, None] = None

  try:
    first_row_index = findFirstRow(table)
    last_row_index = findLastRow(table)

    new_quarter = getNewQuarter(table, first_row_index, indicator)

    index = 0
    for row in table:
      if (index >= first_row_index) and (index <= last_row_index):
        new_table.append(row)
      
      index += 1

  except Exception as err:
    print(err)
    errorMessage = f'The {db_name} table could not be filtered. Error occurred'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return { 'table': new_table, 'new_quarter': new_quarter }