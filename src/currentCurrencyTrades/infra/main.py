from pathlib import Path
from src.currentCurrencyTrades.infra.fetch.fetch import fetchTrades
from src.currentCurrencyTrades.infra.download.pdf_page import downloadPdfPage

def tradesInfra(name: str):   
  path = str(Path(__file__).parents[1].joinpath(f'assets/{name}.pdf')) 
   
  file_url = fetchTrades()

  if file_url is not None:

    path = downloadPdfPage(url=file_url, path=path)

    return path

  return None