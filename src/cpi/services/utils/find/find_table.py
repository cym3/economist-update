import re
import pandas as pd
from cpi.domain.requiredFields.cpi import Indicator
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError

def find_first_row(sheet: list):
  index = 0

  for row in sheet:
    el = str(row[1]).lower()

    if el =='total':
      return index
    index += 1

def find_last_row(sheet: list):
  index = 0

  for row in sheet:
    el = str(row[1]).lower()
    match = re.search('bens e serviços diversos', el)

    if match is not None:
      return index
    index += 1


def findTable(path: str, indicator: Indicator):
  name = indicator['db_name']
  table = []

  try:
    lx = pd.ExcelFile(path)
    sheet_name = lx.sheet_names[1]

    df = pd.read_excel(path, sheet_name=sheet_name)
    sheet = df.values.tolist()

    first_row_index = find_first_row(sheet)
    last_row_index = find_last_row(sheet)

    index = 0
    for row in sheet:
      if (index >= first_row_index) and (index <= last_row_index):
        table.append(row)
    
      index += 1

  except Exception as err:
    print(err)
    errorMessage = f'The {name} CPI has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return table