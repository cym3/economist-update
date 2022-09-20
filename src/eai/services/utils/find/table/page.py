from pathlib import Path
import requests
import re
import PyPDF2
from src.eai.domain.requiredFields.eai import Indicator
from src.eai.domain.entities.create_tasks import createTaskDB
from src.eai.domain.errors.create_error import createError

def validatePage(path: str, indicator: Indicator):
  page_number = indicator['page_number']
  title = indicator['page_title']

  local_path = str(Path(__file__).parents[4].joinpath('assets/eai.pdf'))
  response = requests.get(path)

  try:
    with open(local_path, 'wb') as f:
      f.write(response.content)

    obj = PyPDF2.PdfFileReader(local_path)
    PgOb = obj.getPage(page_number - 1)
    text = PgOb.extractText()

    if re.search(title, text) is None:
      raise Exception('Page not found')

  except Exception as err:
    print(err)
    errorMessage = f'The EAI Page not found error, the Url: {path}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return indicator