from src.economicActivityAggregate.services.utils.find.find_date_row import findDatesRow
from src.economicActivityAggregate.services.utils.find.index import findFirstRow, findLastRow
from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError

def filterDates(table: list, indicator: Indicator):
  db_name = indicator['db_name']
  dates_row = []
  new_table = []

  try:
    first_row_index = findFirstRow(table, indicator)
    last_row_index = findLastRow(table)

    dates_row = findDatesRow(table, first_row_index)

    index = 0
    for row in table:
      if (index >= first_row_index) and (index <= last_row_index):
        new_table.append(row)
      
      index += 1

  except Exception as err:
    print(err)
    errorMessage = f'The {db_name} table could not be filtered. Error occurred'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return { 'table': new_table, 'dates_row': dates_row }