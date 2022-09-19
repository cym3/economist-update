import re
import camelot
from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError

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


def findTable(path: str):
  table = []

  try:
    tables = camelot.read_pdf(path, pages='12', flavor='stream')
    tables.export('foo.csv', f='csv') 
    data = tables.df.values.tolist()

    table = data

  except Exception as err:
    print(err)
    errorMessage = f'The EAI has a format error'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return table