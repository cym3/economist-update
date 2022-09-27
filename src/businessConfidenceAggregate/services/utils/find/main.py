import pandas as pd
from src.economicActivityAggregate.services.utils.find.filter_row import filter_row
from src.economicActivityAggregate.services.utils.find.find_date_row import findDatesRow
from src.economicActivityAggregate.services.utils.find.index import findFirstRow, findLastRow
from src.economicActivityAggregate.services.utils.find.page import validatePage
from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError

def findTable(path: str, indicator: Indicator):
  sheet_name = indicator['sheet_name']
  table = []
  dates_row = []

  try:
    df = pd.read_excel(path, sheet_name=sheet_name)
    validatePage(df, indicator)

    sheet = df.values.tolist()

    first_row_index = findFirstRow(sheet, indicator)
    last_row_index = findLastRow(sheet)

    dates_row = findDatesRow(sheet, first_row_index)
     
    table = []

    index = 0
    for row in sheet:
      if (index >= first_row_index) and (index <= last_row_index):
        table.append(row)
      
      index += 1

  except Exception as err:
    print(err)
    errorMessage = f'The economicActivityAggregate has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return { 'table': table, 'dates_row': dates_row }