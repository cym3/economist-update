from pathlib import Path
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from PyPDF2 import PdfReader, PdfFileWriter
import requests

page_number = 0

# Download the page containing the indicator table data
def downloadPdfPage(url: str, path: Path, indicator: Indicator):
  documentPath = str(path)

  try:
    response = requests.get(url)
    
    with open(documentPath, 'wb') as f:
      f.write(response.content)

    pdf_writer = PdfFileWriter()
    pdf = PdfReader(documentPath)

    page = pdf.getPage(page_number)
    pdf_writer.addPage(page)

    with open(documentPath, 'wb') as fh:
      pdf_writer.write(fh)

  except Exception as err:
    print(err)
    errorMessage = f'Could not download the pdf file, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return path