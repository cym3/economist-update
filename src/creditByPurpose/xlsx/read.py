from pathlib import Path
import pandas as pd
from src.creditByPurpose.domain.requiredFields.credit import Indicator
from src.creditByPurpose.domain.entities.create_tasks import createTaskDB
from src.creditByPurpose.domain.errors.create_error import createError

def readXlsx(path: Path, indicator: Indicator):
  documentPath = str(path)
  table = []

  try:
    lx = pd.ExcelFile(documentPath)
    sheet_name = lx.sheet_names[0]

    df = pd.read_excel(documentPath, sheet_name=sheet_name)
    sheet = df.values.tolist()

    return sheet

  except Exception as err:
    print(err)
    errorMessage = f'Was not possible to read {documentPath} file'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return table