from pathlib import Path
from src.businessConfidenceAggregate.services.download.pdf_table import downloadPdfTable
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceAggregate.services.fetch.fetch import fetchBusinessConfidence
from datetime import datetime

def check_updateService(quarter: Quarter, indicator: Indicator):  
  name = indicator['db_name']
  path = str(Path(__file__).parents[1].joinpath(f'assets/{name}.pdf')) 
   
  fetch_result = fetchBusinessConfidence(quarter)

  if fetch_result is not None:
    url = fetch_result['url']

    path = downloadPdfTable(url=url, path=path, indicator=indicator)

    year = fetch_result['quarter']['year']
    month = fetch_result['quarter']['toMonth']

    now = datetime(year, month, 1)
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    scheduleCode = indicator['scheduleCode']

    howToUpdate = f"""
      Go to {name} system update, you will find ONE PDF file named '{name}.pdf', It should have just ONE PAGE, go to https://www.ilovepdf.com/ convert the pdf file to excel, download and rename to '{name}.xlsx'
      then add excel file in the {name} system update, and run the system.
    """

    task = {
      'scheduleCode': scheduleCode,
      'howToUpdate': howToUpdate,
      'date': new_date
    }

    return task

  return None
