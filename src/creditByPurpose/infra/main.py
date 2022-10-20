from pathlib import Path
from src.creditByPurpose.domain.requiredFields.credit import DateCredit, Indicator
# from src.creditByPurpose.infra.fetch.fetch import fetchCreditByPurpose
# from src.creditByPurpose.infra.download.pdf_page import downloadPdfPage

def creditByPurposeInfra(date: DateCredit, indicator: Indicator):   
  name = indicator['db_name']
  file_url = str(Path(__file__).parents[1].joinpath(f'assets/{name}.xlsx')) 

  return file_url
   
  # file_url = fetchCreditByPurpose(quarter)

  # if file_url is not None:

  #   path = downloadPdfPage(url=file_url, path=path, indicator=indicator)

  #   return path

  # return None