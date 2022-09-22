import re
import pandas as pd
from src.eai.services.utils.find.table.page import validatePage
from src.eai.domain.requiredFields.eai import Indicator
from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError

def find_first_row(sheet: list, indicator: Indicator):
  name: str = indicator['name'].lower()

  index = 0
  for row in sheet:
    el = str(row[0]).split('\n')
    row_name = ' '.join(el).lower()

    if name == row_name:
      return index
    index += 1

def find_last_row(sheet: list):
  index = 0

  for row in sheet:
    row_name = str(row[0]).lower()
    match = re.search('outros serviços', row_name)

    if match is not None:
      return index
    index += 1


def findTable(path: str, indicator: Indicator):
  table = []
  try:
    sheet_name = indicator['sheet_name']

    df = pd.read_excel(path, sheet_name=sheet_name)
    validatePage(df, indicator)

    sheet = df.values.tolist()

    first_row_index = find_first_row(sheet, indicator)
    last_row_index = find_last_row(sheet)

    months = sheet[first_row_index -2]
    print(months)

    index = 0
    for row in sheet:
      if (index >= first_row_index) and (index <= last_row_index):
        table.append(row)
    
      index += 1

  except Exception as err:
    print(err)
    errorMessage = f'The EAI has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return table