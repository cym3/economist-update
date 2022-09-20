import re
import camelot
from src.eai.services.utils.find.table.page import validatePage
from src.eai.domain.requiredFields.eai import Indicator
from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError

def findTable(path: str, indicator: Indicator):
  table = []

  try:
    indicator = validatePage(path, indicator)
    page_number = indicator['page_number']

    tables = camelot.read_pdf(path, pages=str(page_number))
    list = tables[0].df.values.tolist()

    table = list

  except Exception as err:
    print(err)
    errorMessage = f'The EAI has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return table