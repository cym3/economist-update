from pathlib import Path
from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Quarter, Indicator
from src.businessConfidenceBySector.infra.fetch.fetch import fetchBusinessConfidence
from src.businessConfidenceBySector.infra.download.pdf_page import downloadPdfPage

def businessConfidenceInfra(quarter: Quarter, indicator: Indicator):   
  name = indicator['db_name']
  path = str(Path(__file__).parents[1].joinpath(f'assets/{name}.pdf')) 
   
  file_url = fetchBusinessConfidence(quarter)

  if file_url is not None:

    path = downloadPdfPage(url=file_url, path=path, indicator=indicator)

    return path

  return None