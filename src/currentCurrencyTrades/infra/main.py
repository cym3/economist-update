from pathlib import Path
from currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.infra.fetch.fetch import fetchTrades
from src.currentCurrencyTrades.infra.download.pdf_page import downloadPdfPage

def tradesInfra(indicator: Indicator):   
  db_name = indicator['db_name']
  path = str(Path(__file__).parents[1].joinpath(f'assets/{db_name}.pdf')) 
   
  file_url = fetchTrades()

  if file_url is not None:

    path = downloadPdfPage(url=file_url, path=path)

    return path

  return None