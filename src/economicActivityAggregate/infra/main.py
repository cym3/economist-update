from pathlib import Path
from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.infra.fetch.fetch import fetchEconomicActivity
from src.economicActivityAggregate.infra.download.pdf_page import downloadPdfPage

def economicActivityInfra(date: DateEconomicActivity, indicator: Indicator):   
  name = indicator['db_name']
  path = str(Path(__file__).parents[1].joinpath(f'assets/{name}.pdf')) 
   
  file_url = fetchEconomicActivity(date, indicator)

  if file_url is not None:

    path = downloadPdfPage(url=file_url, path=path, indicator=indicator)

    return path

  return None