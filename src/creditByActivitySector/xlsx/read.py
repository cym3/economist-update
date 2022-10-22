import pandas as pd
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError

def readXlsx(documentPath: str):
  table = []

  try:
    lx = pd.ExcelFile(documentPath)
    sheet_name = lx.sheet_names[2]

    df = pd.read_excel(documentPath, sheet_name=sheet_name)
    sheet = df.values.tolist()

    return sheet

  except Exception as err:
    print(err)
    errorMessage = f'Was not possible to read {documentPath} file'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return table