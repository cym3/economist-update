from src.businessConfidenceAggregate.services.download.page_validator import validator
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from PyPDF2 import PdfReader, PdfFileWriter
import requests


def downloadPdfTable(url: str, path: str, indicator: Indicator):
  try:
    response = requests.get(url)

    with open(path, 'wb') as f:
      f.write(response.content)

    pdf_writer = PdfFileWriter()
    pdf = PdfReader(path)

    for page_number in range(pdf.getNumPages()):
      page = pdf.getPage(page_number)
      text = page.extract_text()

      is_valide_page = validator(text, indicator)

      if is_valide_page is True:
        pdf_writer.addPage(page)

        with open(path, 'wb') as fh:
          pdf_writer.write(fh)

  except Exception as err:
    print(err)
    errorMessage = f'Could not download the pdf file, the url is {url}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return path