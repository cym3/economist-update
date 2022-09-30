from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from PyPDF2 import PdfReader, PdfFileWriter
import requests

# Download the page containing the indicator table data
def downloadPdfPage(url: str, path: str, indicator: Indicator):
  try:
    response = requests.get(url)

    with open(path, 'wb') as f:
      f.write(response.content)

    pdf_writer = PdfFileWriter()
    pdf = PdfReader(path)

    page_number = indicator['page_number']

    page = pdf.getPage(page_number)
    pdf_writer.addPage(page)

    with open(path, 'wb') as fh:
      pdf_writer.write(fh)

  except Exception as err:
    print(err)
    errorMessage = f'Could not download the pdf file, the url is {url}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return path