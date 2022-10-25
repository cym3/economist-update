from pathlib import Path
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.infra.fetch.fetch import fetchTrades
from src.currentCurrencyTrades.infra.download.pdf_page import downloadPdfPage

def tradesInfra(indicator: Indicator):   
  db_name = indicator['db_name']

  folder_path = Path(__file__).parents[1].joinpath('assets')
  folder_path.mkdir(parents=True, exist_ok=True)
  path = folder_path.joinpath(f'{db_name}.pdf')
   
  file_url = fetchTrades()

  if file_url is not None:

    path = downloadPdfPage(url=file_url, path=path, indicator=indicator)

    return path

  return None