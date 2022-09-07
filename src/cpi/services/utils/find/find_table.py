import re
import pandas as pd
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError

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


async def findTable(path: str):
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
    errorMessage = f'The CPI has a format error'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return table